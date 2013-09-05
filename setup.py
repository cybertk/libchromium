#!/usr/bin/env python

import os
import shutil
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))
chromium_dir = os.path.abspath(os.path.join(script_dir, 'src'))
# Solution root directory.
root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

overrides_dir = os.path.abspath(os.path.join(script_dir, 'overrides'))
patches_dir = os.path.abspath(os.path.join(script_dir, 'patches'))

def Override(path):
  """Override chromium's original file with the file located at path."""
  dst_path = os.path.join(chromium_dir, os.path.relpath(path, overrides_dir))
  # Remove . and ..
  dst_path = os.path.abspath(dst_path)

  if os.path.isdir(path):
    if not os.path.exists(dst_path):
      os.mkdir(dst_path)
    for item in os.listdir(path):
      # Recursive override
      Override(os.path.join(path, item))

  else:
    shutil.copy(path, dst_path)
    print 'override', os.path.relpath(dst_path, chromium_dir)

def Patch(path):
  """Apply a patch aginst chromimu's origin source tree."""
  if os.path.isdir(path):
    for item in os.listdir(path):
      # Recursive override
      Patch(os.path.join(path, item))

  else:
    # Relative patch path.
    relpath = os.path.relpath(path, chromium_dir)
    subprocess.call(
        ['patch', '-N', '-s', '-d', chromium_dir, '-p0', '-i', relpath])

def CreateSym():
  """Create chromium shortcut. Chromium's source tree must live in src dir."""
  shortpath = os.path.join(root_dir, 'chromium')
  if not os.path.exists(shortpath):
    os.symlink(chromium_dir, shortpath)
  
Override(overrides_dir)
Patch(patches_dir)
CreateSym()

