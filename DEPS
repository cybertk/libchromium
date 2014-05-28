# When adding a new dependency, please update the top-level .gitignore file
# # to list the dependency's destination directory.

use_relative_paths = True

vars = {
  "github": "http://github.com/%s/%s.git",
  "googlecode_url": "http://%s.googlecode.com/svn",
}

deps_os = {
  'ios': {
    # NSS, for SSLClientSocketNSS in net.
    "src/third_party/nss": From("chromium_deps", "src/third_party/nss"),
  },
}

deps = {
  "../chromium_deps":
     File("http://src.chromium.org/svn/releases/28.0.1500.16/DEPS"),

  "src/chrome": None,
  "src/content": None,
  "src/browser": None,

  # We no not use iossim
  "src/testing/iossim":
    None,

  # Main source tree.
  "src": From("chromium_deps", "src"),

  # depot_tools, include gyp, ninja etc.
  "depot_tools": From("chromium_deps", "depot_tools"),

  "src/third_party/jsoncpp/source/include":
    "http://svn.code.sf.net/p/jsoncpp/code/trunk/jsoncpp/include@248",
  "src/third_party/jsoncpp/source/src/lib_json":
    "http://svn.code.sf.net/p/jsoncpp/code/trunk/jsoncpp/src/lib_json@248",

  # Base depends on it?
  "src/third_party/icu": From("chromium_deps", "src/third_party/icu"),

  # src/testing dependencies.
  "src/testing/gtest": From("chromium_deps", "src/testing/gtest"),
  "src/testing/gmock": From("chromium_deps", "src/testing/gmock"),

  # Resource genereator, used by i18n.
  "src/tools/grit": From("chromium_deps", "src/tools/grit"),

  # src/build dependencies. gyp_chromium.
  "src/tools/gyp": From("chromium_deps", "src/tools/gyp"),

  # sdcn dependency, used in src/net.
  "src/sdch/open-vcdiff": From("chromium_deps", "src/sdch/open-vcdiff"),

  # net dependency, used in src/net.
  "src/googleurl": From("chromium_deps", "src/googleurl"),

  # Skia, media dependency.
  "src/third_party/skia/src": From("chromium_deps", "src/third_party/skia/src"),
  "src/third_party/skia/gyp": From("chromium_deps", "src/third_party/skia/gyp"),
  "src/third_party/skia/include":
     From("chromium_deps", "src/third_party/skia/include"),

  # opus audio codec, media dependency.
  "src/third_party/opus/src": From("chromium_deps", "src/third_party/opus/src"),

  "src/third_party/libjingle/source":
    From("chromium_deps", "src/third_party/libjingle/source"),
}

hooks = [
  {
    # configure overrides.
    "pattern": "libchromium/",
    "action": ["python", "libchromium/setup.py", "--chromium_dir", "libchromium/src", "--overrides_dir", "overrides"],
  },
]
