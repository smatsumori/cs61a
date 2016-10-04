test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_swap(19)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(44)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(23)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(55)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(2) # Single digits have one unique digit
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(12)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> is_swap(65)
          False
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
