import math

import pytest

from mathExpressionHandler.exceptions import MathModuleError
from mathExpressionHandler.logicApp.math_expression_handler import MathExpressionHandler

testdata_for_test_simple_exceptions = [
    ('cos(x)', {'x': 1}, math.cos(1)),
    ('sin(x)', {'x': 1}, math.sin(1)),
    ('tan(x)', {'x': 1}, math.tan(1)),
    ('4-2*a/(5*x-3)', {'a': 2.5, 'x': 0}, 5.666666666666667),
]


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
    assert e.value.name == "x"
