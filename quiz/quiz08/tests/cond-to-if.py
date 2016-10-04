test = {
  'name': 'cond-to-if',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond-to-if '(cond (else 4)))
          4
          scm> (cond-to-if '(cond (else (+ x 2))))
          (+ x 2)
          scm> (cond-to-if '(cond ((< x 3) (+ x 3)) (else (- x 3))))
          (if (< x 3) (+ x 3) (- x 3))
          scm> (cond-to-if '(cond ((< x y) x) ((> x y) y) (else 0)))
          (if (< x y) x (if (> x y) y 0))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
