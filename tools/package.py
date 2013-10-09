#!/usr/bin/env python
# Copyright (c) 2013 Quanlong He. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
package.py -- Generate ipa file for itunes installation, ad-hoc or Store.
"""

import optparse
import os
import sys
import subprocess 

def Package(app, ipa, verbose):
  '''Package the app to ipa, save to current dir if ipa is relative path.
  '''
  # xcrun will save the output ipa to its working dir if ipa is a
  # relative path.
  if not os.path.isabs(ipa):
    ipa = os.path.join(os.getcwd(), ipa)

  if verbose:
    subprocess.call(['xcrun', '--sdk', 'iphoneos',
                    'PackageApplication', '-v', app, '-o', ipa])
  else:
    subprocess.call(['xcrun', '--sdk', 'iphoneos',
                    'PackageApplication', app, '-o', ipa])

def main(argv=None):
  parser = optparse.OptionParser(usage=__doc__)
  parser.add_option('-o', '--output',
                    metavar='IPA', default='output.ipa', dest='output',
                    help="Write the generated .ipa to IPA.")
  parser.add_option('-v', '--verbose',
                    action='store_true', default=False, dest='verbose')

  opts, args = parser.parse_args()
  print opts

  if not args:
    parser.print_help()
    sys.exit(1)

  Package(args[0], opts.output, opts.verbose)

if __name__ == '__main__':
  main()
