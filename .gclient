solutions = [
{ "name"        : "chromium_deps",
  "url"         : "http://src.chromium.org/svn/releases/28.0.1500.16",
  "deps_file"   : "DEPS",
  "managed"     : True,
  "safesync_url": "",
  "custom_deps" : {
    # this project is dead, http://gsutil.googlecode.com
    "build/third_party/gsutil": None,

    # Unused for ios
    "commit-queue": None,
    "depot_tools": None,
    "build/scripts/private/data/reliability": None,
    "build/scripts/gsd_generate_index": None,
    "build/scripts/command_wrapper/bin": None,
    "build/third_party/swarm_client": None,
    "build/third_party/lighttpd": None,
    "build": None,

    "src/webkit": None,
    "src/win8": None,
    "src/cc": None,
    "src/chrome": None,
    "src/chrome/test/data/perf/third_party/octane": None,
    "src/chrome_frame": None,
    "src/chromeos": None,
    "src/cloud_print": None,
    "src/content": None,
    "src/content/test/data/layout_tests/LayoutTests/fast/filesystem": None,
    "src/content/test/data/layout_tests/LayoutTests/fast/files": None,
    "src/courgette": None,
    "src/dbus": None,
    "src/net": None,
    "src/tools/deps2git": None,

    "src/printing": None,
    "src/media": None,

  },
  "hooks": [
    {
        "pattern": ".",
        "action": [],
    }
  ],
},
]

target_os = ['ios']
target_os_only = True
