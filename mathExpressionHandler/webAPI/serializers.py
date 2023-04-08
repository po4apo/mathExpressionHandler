import re

from rest_framework import serializers
from rest_framework.serializers import ValidationError


def expression_validator(expression: str):
    re_pattern = r"([\d]+\.[\d]+|[\d+\-/\*^a-zA-Z)(])+"
    result = re.match(re_pattern, expression)
    if result is not None and len(expression) == result.regs[0][1]:
        return expression
    else:
        raise ValidationError(
            f'{expression[result.regs[0][1]] if result is not None else expression[0]} is invalid character.')


class AlgebraicExpressionSerializer(serializers.Serializer):
    expression = serializers.CharField(max_length=100, allow_null=False, validators=[expression_validator])
    variables = serializers.DictField(child=serializers.FloatField())

    def create(self, validated_data):
        return AlgebraicExpressionSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.expression = validated_data.get('expression', instance.expression)
        instance.variables = validated_data.get('variables', instance.variables)
        return instance
