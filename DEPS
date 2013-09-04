# When adding a new dependency, please update the top-level .gitignore file
# # to list the dependency's destination directory.

use_relative_paths = True

vars = {
  "github": "http://github.com/%s/%s.git",
  "googlecode_url": "http://%s.googlecode.com/svn",
  "chromium_git": "https://chromium.googlesource.com/",

  "chromium_svn": "http://src.chromium.org/svn/trunk",

  # http://src.chromium.org/svn/releases/31.0.1604.0/
  "chromium_revision": "218165",

  "gtm_revision": "625",
  "skia_revision": "10765",

  'google-toolbox-for-mac':
    'http://google-toolbox-for-mac.googlecode.com/svn',
}

deps_os = {
'ios': {
      'src/third_party/sfntly/cpp/src':
      None,
      'src/third_party/v8-i18n':
      None,
      'src/chrome/test/data/perf/frame_rate/content':
      None,
      'src/third_party/ots':
      None,
      'src/third_party/undoview':
      None,
      #'src/third_party/GTM':
      #Var("google-toolbox-for-mac") + '/trunk@616',
      'src/third_party/webgl_conformance':
      None,
      'src/third_party/hunspell_dictionaries':
      None,
      'src/third_party/scons-2.0.1':
      None,
      'src/third_party/webdriver/pylib':
      None,
      'src/chrome/test/data/perf/canvas_bench':
      None,
      'src/third_party/libexif/sources':
      None,
      'src/third_party/libphonenumber/src/phonenumbers':
      None,
      'src/third_party/libphonenumber/src/resources':
      None,
      'src/third_party/safe_browsing/testing':
      None,
      'src/third_party/libyuv':
      None,
      'src/third_party/snappy/src':
      None,
      'src/third_party/webrtc':
      None,
      'src/third_party/libjpeg_turbo':
      None,
      "src/third_party/nss":
      From("chromium_deps", "src/third_party/nss"),
      'src/third_party/bidichecker':
      None,
      'src/third_party/usrsctp/usrsctplib':
      None,
      'src/third_party/pylib':
      None,
      'src/chrome/test/data/extensions/api_test/permissions/nacl_enabled/bin':
      None,
      'src/third_party/smhasher/src':
      None,
      'src/third_party/hunspell':
      None,
      'src/native_client':
      None,
      #'src/testing/iossim/third_party/class-dump':
      #'/trunk/deps/third_party/class-dump@199203',
      'src/third_party/leveldatabase/src':
      None,
      'src/third_party/libsrtp':
      None,
      'src/third_party/ffmpeg':
      None,
      'src/native_client/src/third_party/ppapi':
      None,
      'src/tools/page_cycler/acid3':
      None,
      'src/build/util/support':
      None,
      'src/third_party/libphonenumber/src/test':
      None,
      'src/third_party/pymox/src':
      None,
      'src/third_party/angle_dx11':
      None,
      'src/third_party/webpagereplay':
      None,
      'src/third_party/yasm/source/patched-yasm':
      None,
      'src/third_party/angle':
      None,
      'src/v8':
      None,
      'src/third_party/libvpx':
      None,
      'src/third_party/swig/Lib':
      None,
   },
}

deps = {
  "../chromium_deps":
     File("http://src.chromium.org/svn/releases/30.0.1550.2/DEPS"),

  "src/chrome": None,
  "src/content": None,
  "src/browser": None,

  # We no not use iossim
  "src/testing/iossim":
    None,

  # Main source tree.
  #"src": From("chromium_deps", "src"),

  # depot_tools, include gyp, ninja etc.
  "depot_tools": From("chromium_deps", "depot_tools"),

  # Base depends on it?
  "src/third_party/icu": From("chromium_deps", "src/third_party/icu"),

  # src/testing dependencies.
  "src/testing/gtest": From("chromium_deps", "src/testing/gtest"),
  "src/testing/gmock": From("chromium_deps", "src/testing/gmock"),

  # Resource genereator, used by i18n.
  "src/tools/grit": From("chromium_deps", "src/tools/grit"),

  # src/build dependencies. gyp_chromium.
  "src/tools/gyp": From("chromium_deps", "src/tools/gyp"),

  # NSS, for SSLClientSocketNSS in net.
  "src/third_party/nss": From("chromium_deps", "src/third_party/nss"),

  # sdcn dependency, used in src/net.
  "src/sdch/open-vcdiff": From("chromium_deps", "src/sdch/open-vcdiff"),

  # Skia, media dependency.
  "src/third_party/skia/src": From("chromium_deps", "src/third_party/skia/src"),
  "src/third_party/skia/gyp": From("chromium_deps", "src/third_party/skia/gyp"),
  "src/third_party/skia/include":
     From("chromium_deps", "src/third_party/skia/include"),

  # opus audio codec, media dependency.
  "src/third_party/opus/src": From("chromium_deps", "src/third_party/opus/src"),
}

hooks = [
  {
    # configure overrides.
    "pattern": ".",
    "action": ["python", "libchromium/setup.py"],
  },
  {
    "pattern": ".",
    "action": ["python",
               "src/build/gyp_chromium",
               "demo/demo.gyp",
               "--depth=src"],
  }
]
