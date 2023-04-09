import pytest

from conftest import testdata_for_test_simple_exceptions
from mathExpressionHandler.exceptions import MathModuleError
from mathExpressionHandler.logicApp.math_expression_handler import MathExpressionHandler


@pytest.mark.parametrize("exception, vars, expected_result", testdata_for_test_simple_exceptions)
def test_exceptions(exception, vars, expected_result):
    meh = MathExpressionHandler(exception, vars)
    result = meh.calculate()
    assert result == expected_result


def test_uses_reserved_vars():
    with pytest.raises(MathModuleError) as e:
        MathExpressionHandler('cos(cos)', {'cos': 5})

    assert MathModuleError.MSGs.res_name == e.value.msg


def test_undefined_var():
    result = None
    with pytest.raises(NameError) as e:
        meh = MathExpressionHandler('cos(x) * z', {'y': 1})
        result = meh.calculate()

    assert result is None
    assert e.value.args[0] == "name 'x' is not defined"
