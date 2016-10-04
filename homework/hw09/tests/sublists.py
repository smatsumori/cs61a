test = {
  'name': 'sublists',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (sublists (1 2 3) ?subs))
          Success!
          subs: (() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))
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
