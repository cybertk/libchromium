libchromium
===========

Create .gclient with following content, replace the "demo" solution to your real project.

Note: The demo solution must come after libchromium, in order to get the correct hooks order.

    solutions = [
    { "name"        : "libchromium",
      "url"         : "http://github.com/cybertk/libchromium.git",
      "deps_file"   : "DEPS",
      "managed"     : True,
      "safesync_url": "",
    },
    { "name"        : "demo",
      "url"         : "http://github.com/cybertk/libchromium-demo.git",
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
