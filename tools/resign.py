#!/usr/bin/env python
# Copyright (c) 2013 Quanlong He. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
resign-ipa.py -- Resign the ipa with new certificate and mobileprovision.
"""

"""
#!/bin/sh

# [1][http://stackoverflow.com/questions/6896029/re-sign-ipa-iphone]

CODE_SIGN_IDENTITY='iPhone Distribution: Thomas Sachson'
PROVISIONING_PROFILE='/Users/quanlong/projects/origin_pa/src/tools/ios_dev_group7.mobileprovision'

IPA=$1

# Unzip the IPA
unzip $IPA

APP=$(ls -d Payload/*.app)
# Remove old CodeSignature, we don't have CodeResources
rm -rf "$APP/_CodeSignature"

# Replace embedded mobile provisioning profile
cp "$PROVISIONING_PROFILE" "$APP/embedded.mobileprovision"

# Re-sign, Removed the Entitlement part (see alleys comment, thanks)
codesign -f -s "$CODE_SIGN_IDENTITY" --resource-rules "$APP/ResourceRules.plist" "$APP"

# Re-package
zip -qr "${IPA%%.ipa}.resigned.ipa" Payload
"""

import optparse
import os
import sys
import subprocess 
import zipfile
import tempfile
import glob
import shutil

def Resign(ipa, identity, provision, output, verbose):
  '''Resign the ipa with new identity and provision.
  '''
  # xcrun will save the output ipa to its working dir if ipa is a
  # relative path.
  if not os.path.isabs(ipa):
    ipa = os.path.join(os.getcwd(), ipa)

  # Fallback to default ipa name.
  if not output:
    output = os.path.splitext(ipa)[0]  + '.%s.resigned.ipa' \
                % os.path.splitext(os.path.basename(provision))[0]

  working_dir = tempfile.gettempdir()
  working_dir = os.path.join(os.getcwd(), "package")

  # Unzip the IPA
  zfile = zipfile.ZipFile(ipa,'r')
  zfile.extractall(working_dir)

  # Got app dir.
  app_dir = glob.glob(working_dir + '/Payload/*')[0]

  # Replace embedded mobile provisioning profile
  shutil.copy(provision, os.path.join(app_dir, 'embedded.mobileprovision'))

  # Re-sign, Removed the Entitlement part (see alleys comment, thanks)
  # codesign -f -s "$CODE_SIGN_IDENTITY" --resource-rules "$APP/ResourceRules.plist" "$APP"
  if verbose:
    subprocess.call([
          'codesign', '-f', '-v', '-s', identity,
          '--resource-rules', os.path.join(app_dir, 'ResourceRules.plist'),
          app_dir])
  else:
    subprocess.call([
          'codesign', '-f', '-s', identity,
          '--resource-rules', os.path.join(app_dir, 'ResourceRules.plist'),
          app_dir])

  # Zip the payload.
  f = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)
  for dirpath, dirnames, filenames in os.walk(working_dir):
    for filename in filenames:
      filepath = os.path.join(dirpath, filename)
      f.write(filepath, os.path.relpath(filepath, working_dir))
  f.close()

  print 'Resigned to', output

def main(argv=None):
  parser = optparse.OptionParser(usage=__doc__)
  parser.add_option('-s', '--sign',
                    metavar='IDENTITY', default='', dest='identity',
                    help="Write the generated .ipa to IPA.")
  parser.add_option('-p', '--provision',
                    metavar='PROVISION_FILE', default='', dest='provision',
                    help="Write the generated .ipa to IPA.")
  parser.add_option('-o', '--output',
                    metavar='IPA', default='', dest='output',
                    help="Write the generated .ipa to IPA.")
  parser.add_option('-v', '--verbose',
                    action='store_true', default=False, dest='verbose')

  opts, args = parser.parse_args()
  print opts

  if not args or not opts.identity or not opts.provision:
    parser.print_help()
    sys.exit(1)

  Resign(args[0], opts.identity, opts.provision, opts.output, opts.verbose)

if __name__ == '__main__':
  main()
