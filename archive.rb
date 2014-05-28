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
  ]
}

def archive(version)

  zipfile_name = "libchromium-%s.zip" % version
  script_dir = Pathname.new File.dirname(__FILE__)
  lib_dir = script_dir + 'src/xcodebuild/Release-iphoneOS'
  src_dir = script_dir + 'src'

  Zip::File.open(zipfile_name, Zip::File::CREATE) do |zipfile|
    # Archive libs
    $libs['base'].each do |lib|
      filename = 'lib%s.a' % lib
      zipfile.add('lib/' + filename, lib_dir + filename)
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
