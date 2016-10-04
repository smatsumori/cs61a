test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(4, 6, 1))
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(3, 0, make_test_dice(4, 6, 1))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 35)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 71)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 7)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 0)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(1, 0, make_test_dice(3))
          5
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
