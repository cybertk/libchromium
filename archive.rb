#!/usr/bin/ruby

require 'pathname'
require 'zip'

$libs = {
  'base' => [
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
  ],
  'net' => [
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
    'crssl',  # chromium libssl
  ]
}

def archive(version)

  zipfile_name = "libchromium-%s.zip" % version
  script_dir = Pathname.new File.dirname(__FILE__)
  lib_dir = script_dir + 'src/xcodebuild/Release-iphoneOS'
  src_dir = script_dir + 'src'

  # Delete if exist
  File.delete(zipfile_name) if File.exist?(zipfile_name)

  Zip::File.open(zipfile_name, Zip::File::CREATE) do |zipfile|
    # Archive libs
    $libs.each do |k, mod|
      mod.each do |lib|
        filename = 'lib%s.a' % lib
        zipfile.add('lib/' + filename, lib_dir + filename)
      end
    end

    # Archive headers
    Dir.glob(src_dir + "**/*.h").each do |header|
      filename = Pathname.new(header).relative_path_from(src_dir)
      filename = Pathname.new('include/chromium') + filename
      zipfile.add(filename, header)
    end
  end
end

#archive('0.1.0')
