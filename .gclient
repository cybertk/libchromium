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
    "build/third_party/swarm_client": None,
    "build/third_party/lighttpd": None,
    "build": None,

    "webkit": None,
    "win8": None,
    "chrome": None,
    "chrome/test/data/perf/third_party/octane": None,
    "chromeos": None,
    "content": None,
    "content/test/data/layout_tests/LayoutTests/fast/filesystem": None,
    "content/test/data/layout_tests/LayoutTests/fast/files": None,

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
