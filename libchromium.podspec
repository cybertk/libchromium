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

  s.subspec 'Base' do |ss|
    # ss.header_dir       = 'chromium/base'
    # ss.preserve_paths = 'src/base'
    # ss.source_files = 'src/base/**/*.h'
    # ss.public_header_files = 'src/base/**/*.h'
    # ss.header_mappings_dir = 'base'
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
end
