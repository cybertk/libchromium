#!/usr/bin/env python

import os
import shutil

script_dir = os.path.dirname(os.path.realpath(__file__))
chromium_dir = os.path.abspath(os.path.join(script_dir, os.pardir, 'chromium'))

overrides_dir = os.path.abspath(os.path.join(script_dir, 'overrides'))

def Override(path):
  dst_path = os.path.join(chromium_dir, os.path.relpath(path, overrides_dir))
  dst_path = os.path.abspath(dst_path)

  if os.path.isdir(path):
    if not os.path.exists(dst_path):
      os.mkdir(dst_path)
    for item in os.listdir(path):
      # Recursive override
      Override(os.path.join(path, item))

  else:
    shutil.copy(path, dst_path)
    print 'Override', dst_path

Override(overrides_dir)
