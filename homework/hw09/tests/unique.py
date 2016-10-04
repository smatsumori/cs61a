test = {
  'name': 'unique',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (unique (1 2 3)))
          Success!
          logic> (query (unique ()))
          Success!
          logic> (query (unique (1 2 3 3 4)))
          Failed.
          logic> (query (unique (1 2 3 1)))
          Failed.
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      logic> (load hw09.logic)
      """,
      'teardown': '',
      'type': 'logic'
    }
  ]
}
