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
          'dependencies': [
            'base',
          ],
          'link_settings': {
            'libraries': [
              'prebuilt/ios/armv7/net/libnet.a',
              'prebuilt/ios/armv7/net/libsdch.a',
              'prebuilt/ios/armv7/net/liburl_lib.a',
              'prebuilt/ios/armv7/net/libchrome_zlib.a',

              'prebuilt/ios/armv7/net/libnss_static.a',
              'prebuilt/ios/armv7/net/libcrcrypto.a',
              'prebuilt/ios/armv7/net/libcrnss.a',
              'prebuilt/ios/armv7/net/libcrnssckbi.a',
              'prebuilt/ios/armv7/net/libcrnspr.a',
              'prebuilt/ios/armv7/net/libcrssl.a',

              '$(SDKROOT)/usr/lib/libsqlite3.dylib',

              # export from net.gyp #1421 line.
              '$(SDKROOT)/System/Library/Frameworks/CFNetwork.framework',
              '$(SDKROOT)/System/Library/Frameworks/MobileCoreServices.framework',
              '$(SDKROOT)/System/Library/Frameworks/Security.framework',
              '$(SDKROOT)/System/Library/Frameworks/SystemConfiguration.framework',
              '$(SDKROOT)/usr/lib/libresolv.dylib',
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
