test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> always_roll_5 = always_roll(5)
          >>> # Be specific about the error type (AssertionError, rather than Error)
          >>> always_roll_5 == check_strategy(always_roll_5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def fail_15_20(score, opponent_score):
          ...     if score == 15 and opponent_score == 20:
          ...         return 100
          ...     return 5
          >>> # Be specific about the error type (AssertionError, rather than Error)
          >>> fail_15_20 == check_strategy(fail_15_20)
          AssertionError
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
