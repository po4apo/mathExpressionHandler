import math

valid_expressions = [
    '4-2*a/(5*x-3)',
    '4/2',
    '4^a',
    'tan(4/2)',
    '1.2+6/a',
    '-1.2+6/a',
    '- 1.2 + 6/a ',


]

invalid_expressions = [
    ('4-2*a/_(5*x-3)', '_'),
    ('4-2*a.b/(5*x-3)', '.'),
    ('4-2*a,b/(5*x-3)', ','),
    ('os.system("rm -rf ./some_file")', '.'),
    ("__import__('os').system('clear')", '_'),
    ("_().__class__.__bases__[0]", '_'),
    ('4**b', '**'),

]

testdata_for_test_simple_exceptions = [
    ('cos(x)', {'x': 1}, math.cos(1)),
    ('sin(x)', {'x': 1}, math.sin(1)),
    ('tan(x)', {'x': 1}, math.tan(1)),
    ('4-2*a/(5*x-3)', {'a': 2.5, 'x': 0}, 5.666666666666667),
]
