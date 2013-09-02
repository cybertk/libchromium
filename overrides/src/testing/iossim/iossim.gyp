# Override the original chromium iossim.gyp
# We are built for real device, we don't need iossim.
{
  'targets': [
    {
      'target_name': 'iossim',
      'type': 'none',
    }
  ]
}
