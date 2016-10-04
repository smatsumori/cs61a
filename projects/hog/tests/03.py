test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> select_dice(4, 24) == four_sided
          True
          >>> select_dice(16, 64) == four_sided
          False
          >>> select_dice(0, 0) == four_sided
          True
          >>> select_dice(50, 80) == four_sided
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max_dice(7, 10)
          1
          >>> max_dice(10, 7)
          1
          >>> max_dice(23, 44)
          1
          >>> max_dice(35, 35)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max_dice(7, 7)
          10
          >>> max_dice(40, 7)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
