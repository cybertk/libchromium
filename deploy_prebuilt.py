#!/usr/bin/env python

import os
import shutil

script_dir = os.path.dirname(os.path.realpath(__file__))
chromium_dir = os.path.abspath(os.path.join(script_dir, 'src'))
# Solution root directory.
root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

base_libs = [
  'base',
  'base_i18n',
  'base_prefs',
  'base_static',

  # Dependencies.
  'dynamic_annotations',
  'event',
  'icudata',
  'icui18n',
  'icuuc',
  'modp_b64',
  'allocator_extension_thunks',
]

net_libs = [
  'net',
]

libs = {
  'base': base_libs,
  'net': net_libs,
}

deploy_dir = os.path.join(script_dir, 'prebuilt')
ios_libs_dir = os.path.join(chromium_dir, 'xcodebuild', 'Debug-iphoneos')

def Copy(libs, to_path):
  # Create dir if it's not exist.
  if not os.path.exists(to_path):
    os.makedirs(to_path)

  for item in libs:
    shutil.copy(item, to_path)
    print 'Deploy', item

def GetLibs(dir, libs):
  items = []
  for item in libs:
    lib = 'lib' + item + '.a'
    items.append(os.path.join(dir, lib))

  return items

def Deploy(module):
  if os.path.exists(ios_libs_dir):
    dir = os.path.join(deploy_dir, 'ios', 'armv7', module)
    Copy(GetLibs(ios_libs_dir, libs[module]), dir)

for module in libs:
  Deploy(module)
