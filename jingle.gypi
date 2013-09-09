{
  'variables': {
    'use_prebuilt_jingle%': '0',
  },
  'targets': [
    {
      'target_name': 'notifier',
      'conditions': [
        ['use_prebuilt_jingle == 1', {
          'type': 'none',
          'dependencies': [
            'base',
          ],
          'link_settings': {
            'libraries': [
              'prebuilt/ios/armv7/jingle/libjingle.a',
          ],
          },  # link_settings
        }, {  # else, use_prebuit_jingle == 1
          'type': '<(component)',
          'dependencies': [
            'src/jingle/jingle.gyp:notifier',
          ],
          'export_dependent_settings': [
            'src/jingle/jingle.gyp:notifier',
          ],
        }]  # end, use_prebuit_jingle == 1
      ],
    },  # target jingle.
  ]
}
