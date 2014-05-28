#!/usr/bin/env python
#
# Copyright (C) 2014 Quanlong He <kyan.ql.he@gmail.com>

import os
import shutil
import subprocess
import optparse
import sys

def Override(chromium_dir, overrides_dir, path=None):
  """Override chromium's original file with the file located at path."""
  if not path:
      path = overrides_dir

  dst_path = os.path.join(chromium_dir, os.path.relpath(path, overrides_dir))
  # Remove . and ..
  dst_path = os.path.abspath(dst_path)

  if os.path.isdir(path):
    if not os.path.exists(dst_path):
      os.mkdir(dst_path)
    for item in os.listdir(path):
      # Recursive override
      Override(chromium_dir, overrides_dir, os.path.join(path, item))

  else:
    print 'Override', os.path.relpath(dst_path, chromium_dir)
    shutil.copy(path, dst_path)

# Depracated
def Patch(chromium_dir, path):
  """Apply a patch aginst chromimu's origin source tree."""
  if os.path.isdir(path):
    for item in os.listdir(path):
      # Recursive override
      Patch(chromium_dir, os.path.join(path, item))

  else:
    # Relative patch path.
    relpath = os.path.relpath(path, chromium_dir)
    print 'Patch', relpath
    subprocess.call(
        ['patch', '-N', '-s', '-d', chromium_dir, '-p0', '-i', relpath])

def CreateSym(chromium_dir):
  """Create chromium shortcut. Chromium's source tree must live in src dir."""
  script_dir = os.path.dirname(os.path.realpath(__file__))
  # Link into include dir.
  shortpath = os.path.join(script_dir, 'include', 'chromium')
  if not os.path.exists(shortpath):
    os.symlink(chromium_dir, shortpath)

def Main():
    parser = optparse.OptionParser(usage='%prog')
    parser.add_option('--chromium_dir',
                      type='string',
                      action='store',
                      dest='chromium_dir',
                      help='Path of Chromium src dir')
    parser.add_option('--overrides_dir',
                      type='string',
                      action='store',
                      dest='overrides_dir',
                      help='Path stores overrides files')
    parser.add_option('--patches_dir',
                      type='string',
                      action='store',
                      dest='patches_dir',
                      help='Path stores patches')

    opts, args = parser.parse_args()

    # --chromium_dir is required
    if not opts.chromium_dir:
        print 'xx'
        sys.exit(1)

    if opts.overrides_dir:
        print "Overriding with", opts.overrides_dir
        Override(opts.chromium_dir, opts.overrides_dir)

    if opts.patches_dir:
        print "Patching with", opts.patches_dir
        Patch(opts.chromium_dir, opts.patches_dir)

    CreateSym(opts.chromium_dir)

if __name__ == '__main__':
    sys.exit(Main())
