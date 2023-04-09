import json

import pytest
from rest_framework.test import APIClient

from conftest import valid_expressions, testdata_for_test_simple_exceptions, invalid_expressions

client = APIClient()


def byte_str_to_dict(byte_str) -> dict:
    return json.loads(bytes.decode(byte_str))


def generate_request(expression: str, variables: dict) -> dict:
    return {
        'expression': expression,
        'variables': variables
    }


def test_get():
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.parametrize('exception, vars, expected_result', testdata_for_test_simple_exceptions)
def test_successful_calculations(exception, vars, expected_result):
    data = generate_request(exception, vars)
    response = client.put('', data=data, format='json')
    result = byte_str_to_dict(response.content).get('result', None)
    assert response.status_code == 200
    assert result == expected_result


@pytest.mark.parametrize('expression', valid_expressions)
def test_successful_validation(expression):
    data = generate_request(expression, {'a': 1, 'x': 2})
    response = client.put('', data=data, format='json')
    assert response.status_code == 200


@pytest.mark.parametrize('expression, invalid_character', invalid_expressions)
def test_unsuccessful_validation_expression(expression, invalid_character):
    data = generate_request(expression, {'a': 1, 'x': 2})
    response = client.put('', data=data, format='json')
    content = byte_str_to_dict(response.content)
    assert response.status_code == 400
    assert {
               'detail': "ValidationError: {'expression': [ErrorDetail(string='" + f"{invalid_character}" + " is invalid character.', code='invalid')]}"} == content


def test_uses_reserved_vars():
    data = generate_request('cos(cos)', {'cos': 5})
    response = client.put('', data=data, format='json')
    content = byte_str_to_dict(response.content)
    assert response.status_code == 400
    assert content == {'detail': 'MathModuleError: Uses reserved names'}


def test_undefined_var():
    data = generate_request('cos(x)*z', {'y': 1})
    response = client.put('', data=data, format='json')
    content = byte_str_to_dict(response.content)
    assert response.status_code == 400
    assert content == {'detail': "NameError: name 'x' is not defined"}


def test_undefined_func():
    data = generate_request('sun(y)', {'y': 1})
    response = client.put('', data=data, format='json')
    content = byte_str_to_dict(response.content)
    assert response.status_code == 400
    assert content == {'detail': "NameError: name 'sun' is not defined"}


def test_unsuccessful_validation_vars():
    data = generate_request('4-2*a/(5*x-3)', {'a': '1das', 'x': 2})
    response = client.put('', data=data, format='json')
    content = byte_str_to_dict(response.content)
    expected_content = {'detail': "ValidationError: {'variables': {'a': [ErrorDetail(string='A valid number is "
                                  "required.', code='invalid')]}}"}
    assert response.status_code == 400
    assert content == expected_content
