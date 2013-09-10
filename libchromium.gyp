{
  'variables': {
    'use_prebuilt%': 0,
  },  # variables

  'target_defaults': {
    'direct_dependent_settings': {
    'include_dirs': [
      'src',
      'include',
    ],
    },
  },
  'includes': [
    'base.gypi',
    'net.gypi',
    'media.gypi',
    'sql.gypi',
    'jingle.gypi',
  ],
  'targets': [
  ]
}
