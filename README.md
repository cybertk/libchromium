libchromium
===========

#### Create .gclient with following content.

    solutions = [
    { "name"        : "demo",
      "url"         : "http://github.com/cybertk/libchromium-demo.git",
      "deps_file"   : "DEPS",
      "managed"     : True,
      "safesync_url": "",
    },
    { "name"        : "libchromium",
      "url"         : "http://github.com/cybertk/libchromium.git",
      "deps_file"   : "DEPS",
      "managed"     : True,
      "safesync_url": "",
    },
    ]

    target_os = ['ios']
    target_os_only = True

Checkout codes.
  $ gclient sync --nohooks

Configure environment
  $ . libchromium/env.sh

Generate projects
  $ gclient runhooks
