import pytest
from rest_framework.serializers import ValidationError

from conftest import valid_expressions, invalid_expressions
from mathExpressionHandler.webAPI.serializers import expression_validator


@pytest.mark.parametrize('expression', valid_expressions)
def test_expression_validator_with_valid_data(expression):
    validation_result = expression_validator(expression)
    assert validation_result == None


@pytest.mark.parametrize('expression, invalid_character', invalid_expressions)
def test_expression_validator_with_invalid_data(expression, invalid_character):
    with pytest.raises(ValidationError) as e:
        expression_validator(expression)
    assert e.value.args[0] == f'{invalid_character} is invalid character.'
