from rest_framework import serializers


class AlgebraicExpressionSerializer(serializers.Serializer):
    expression = serializers.CharField(max_length=100)
    variables = serializers.DictField(child=serializers.FloatField())

    def create(self, validated_data):
        return AlgebraicExpressionSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.expression = validated_data.get('expression', instance.expression)
        instance.variables = validated_data.get('variables', instance.variables)
        return instance
