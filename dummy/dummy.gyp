{
  'targets': [
    {
      'target_name': 'dummy',
      'type': 'executable',

      'sources': [
        'ios/AppDelegate.h',
        'ios/AppDelegate.m',
        'ios/ViewController.h',
        'ios/ViewController.mm',
        'ios/main.mm',
        'ios/cbase-Info.plist',
      ],
      'mac_bundle_resources': [
        'ios/MainStoryboard.storyboard',
        'ios/Default@2x.png',
      ],
      'dependencies': [
        '../libchromium.gyp:base',
        '../libchromium.gyp:net',
        '../libchromium.gyp:sql',
        # '../libchromium.gyp:media',
        # '../libchromium.gyp:jingle',
       ],
      'include_dirs': [
        '..',
      ],
      'conditions': [
        ['OS == "ios"', {
          'mac_bundle': 1,
          'include_dirs': [
            '.',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
              '$(SDKROOT)/System/Library/Frameworks/AVFoundation.framework',
              '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
            ]
          }, # link_settings
        }], # OS == "ios"

      ],
      'xcode_settings': {
        'INFOPLIST_FILE': 'ios/cbase-Info.plist',

        'IPHONEOS_DEPLOYMENT_TARGET': '6.0',

        # Require Code-signing.
        'CODE_SIGN_IDENTITY[sdk=iphoneos*]': 'iPhone Developer',

        # In Ad-hoc mode, common.gypi set this key to YES.
        'SKIP_INSTALL': 'NO',
        'WRAPPER_EXTENSION': 'app',
      }
    }, # Avamessenger target.
  ],
}
