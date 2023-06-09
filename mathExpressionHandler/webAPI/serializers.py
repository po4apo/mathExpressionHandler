import re

from rest_framework import serializers
from rest_framework.serializers import ValidationError


def expression_validator(expression: str):
    re_pattern = r'([\d]+\.[\d]+|[\d+\-/ \*^a-zA-Z)(])+'
    result = re.match(re_pattern, expression)
    if result is not None and len(expression) == result.regs[0][1]:
        result = re.findall(r'[*]{2}', expression)
        if len(result) == 0:
            return
        else:
            raise ValidationError(
                f'{result[0]} is invalid character.')
    else:
        raise ValidationError(
            f'{expression[result.regs[0][1]] if result is not None else expression[0]} is invalid character.')


class AlgebraicExpressionSerializer(serializers.Serializer):
    expression = serializers.CharField(max_length=100, allow_null=False, validators=[expression_validator])
    variables = serializers.DictField(child=serializers.FloatField())

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
