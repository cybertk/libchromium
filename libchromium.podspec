Pod::Spec.new do |s|
  s.name             = "libchromium"
  s.version          = "0.1.0"
  s.summary          = "A short description of libchromium."
  s.homepage         = "https://github.com/cybertk/libchromium"
  s.license          = 'MIT'
  s.author           = { "Quanlong He" => "kyanhe@cienet.com.cn" }
  s.source           = { :http => "http://localhost:9914/libchromium-0.0.1.zip"}
  s.requires_arc     = false
  s.preserve_paths = 'include'
  s.vendored_libraries = 'lib/*.a'
  s.xcconfig = {
    'HEADER_SEARCH_PATHS' => "\
${PODS_ROOT}/#{s.name}/include \
${PODS_ROOT}/#{s.name}/include/chromium \
     ",
    'GCC_PREPROCESSOR_DEFINITIONS' => 'DISABLE_NACL CHROMIUM_BUILD USE_LIBJPEG_TURBO=1 ENABLE_INPUT_SPEECH ENABLE_EGLIMAGE=1 DISABLE_FTP_SUPPORT=1 NDEBUG NVALGRIND DYNAMIC_ANNOTATIONS_ENABLED=0'
  }

  s.subspec 'base' do |ss|
    ss.libraries =
      'base',
      'base_i18n',
      'base_prefs',
      'base_static',
      'dynamic_annotations',
      'event',
      'icudata',
      'icui18n',
      'icuuc',
      'modp_b64',
      'allocator_extension_thunks'
  end

  s.subspec 'net' do |ss|
    ss.dependency 'libchromium/base'
    ss.libraries =
      'net',

      # Dependencies
      'nss_static',
      'sdch',
      'googleurl',
      'chrome_zlib',  # chromium libzlib
      'crcrypto',  # chromium libcrypto
      'crnss',  # chromium libnss, IOS
      'crnssckbi',
      'crnspr',  # chromium libnspr
      'crssl'  # chromium libssl
  end

  s.subspec 'sql' do |ss|
    ss.dependency 'libchromium/base'
    ss.libraries =
      'sql'
  end

  s.subspec 'jingle' do |ss|
    ss.dependency 'libchromium/base'
    ss.dependency 'libchromium/net'
    ss.libraries =
      'expat',
      'jingle',
      'jingle_glue',
      'jingle_p2p_constants',
      'jsoncpp',
      'notifier'
  end

  s.subspec 'media' do |ss|
    ss.dependency 'libchromium/base'
    ss.libraries =
      'media',

      # Depedencies
      'png',
      'ui',
      'skia',
      'skia_opts_ios',
      'opus'
  end
end
