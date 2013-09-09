{
  'variables': {
    'use_prebuilt_sql%': '0',
  },
  'targets': [
    {
      'target_name': 'sql',
      'conditions': [
        ['use_prebuilt_sql == 1', {
          'type': 'none',
          'dependencies': [
            'base',
          ],
          'link_settings': {
            'libraries': [
              'prebuilt/ios/armv7/sql/libsql.a',
          ],
          },  # link_settings
        }, {  # else, use_prebuit_sql == 1
          'type': '<(component)',
          'dependencies': [
            'src/sql/sql.gyp:sql',
          ],
          'export_dependent_settings': [
            'src/sql/sql.gyp:sql',
          ],
        }]  # end, use_prebuit_sql == 1
      ],
    },  # target sql.
  ]
}
