{
  'variables': {
    'use_prebuilt_media%': '0',
  },
  'targets': [
    {
      'target_name': 'media',
      'conditions': [
        ['use_prebuilt_media == 1', {
          'type': 'none',
          'link_settings': {
            'libraries': [
              'prebuilt/ios/armv7/base/liballocator_extension_thunks.a',
              'prebuilt/ios/armv7/base/libbase.a',
              'prebuilt/ios/armv7/base/libbase_i18n.a',
              'prebuilt/ios/armv7/base/libbase_prefs.a',
              'prebuilt/ios/armv7/base/libbase_static.a',
              'prebuilt/ios/armv7/base/libdynamic_annotations.a',
              'prebuilt/ios/armv7/base/libevent.a',
              'prebuilt/ios/armv7/base/libicudata.a',
              'prebuilt/ios/armv7/base/libicui18n.a',
              'prebuilt/ios/armv7/base/libicuuc.a',
              'prebuilt/ios/armv7/base/libmodp_b64.a',
            ],
          },  # link_settings
        }, {  # else, use_prebuit_media == 1
          'type': '<(component)',
          'dependencies': [
            'src/media/media.gyp:media',
          ],
          'export_dependent_settings': [
            'src/media/media.gyp:media',
          ],
        }]  # end, use_prebuit_media == 1
      ],
    },  # target media.
  ]
}
