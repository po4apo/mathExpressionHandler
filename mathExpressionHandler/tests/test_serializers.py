import pytest
from rest_framework.serializers import ValidationError

from mathExpressionHandler.webAPI.serializers import expression_validator

valid_expressions = [
    ('4-2*a/(5*x-3)', '4-2*a/(5*x-3)'),
    ('4/2', '4/2'),
    ('4^b', '4^b'),
    ('sum(4/2)', 'sum(4/2)'),
    ('sum(4/2+2)', 'sum(4/2+2)'),
    ('1.2+6/df', '1.2+6/df'),
    ('-1.2+6/df', '-1.2+6/df'),
]

invalid_expressions = [
    ('4-2*a/_(5*x-3)', '_'),
    ('4-2*a.b/(5*x-3)', '.'),
    ('4-2*a,b/(5*x-3)', ','),
    ('os.system("rm -rf ./some_file")', '.'),
    ("__import__('os').system('clear')", '_'),
    ("_().__class__.__bases__[0]", '_'),
]


@pytest.mark.parametrize('expression, result', valid_expressions)
def test_expression_validator_with_valid_data(expression, result):
    validation_result = expression_validator(expression)
    assert result == validation_result


@pytest.mark.parametrize('expression, invalid_character', invalid_expressions)
def test_expression_validator_with_invalid_data(expression, invalid_character):
    with pytest.raises(ValidationError) as e:
        expression_validator(expression)
    assert e.value.args[0] == f'{invalid_character} is invalid character.'