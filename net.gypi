{
  'variables': {
    'use_prebuilt_net%': '0',
  },
  'targets': [
    {
      'target_name': 'net',
      'conditions': [
        ['use_prebuilt_net == 1', {
          'type': 'none',
          'link_settings': {
            'libraries': [
              'prebuilt/ios/armv7/net/libnet.a',
              'prebuilt/ios/armv7/net/libsdch.a',
              'prebuilt/ios/armv7/net/liburl_lib.a',
              'prebuilt/ios/armv7/net/libchrome_zlib.a',
            ],
          },  # link_settings
        }, {  # else, use_prebuit_net == 1
          'type': '<(component)',
          'dependencies': [
            'src/net/net.gyp:net',
          ],
          'export_dependent_settings': [
            'src/net/net.gyp:net',
          ],
        }]  # end, use_prebuit_net == 1
      ],
    },  # target net.
  ]
}
