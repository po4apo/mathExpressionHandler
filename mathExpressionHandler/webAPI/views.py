from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mathExpressionHandler.logicApp import MathExpressionHandler
from .serializers import AlgebraicExpressionSerializer

RESULT_NAME = "result"

GET_MSG = {
    'header': "This is an api for processing mathematical expressions.",
    'explanation': "The expression allows numbers, variable names, signs of arithmetic operations, "
                   "exponentiation (including non-integer) ^, functions LG (decimal logarithm), "
                   "then LN (natural logarithm), trigonometric functions sine, cosine, tan, ASIN, acos, Atan.",
    'example': {"expression": "4-2*a/(5*x-3)", "variables": {"a": 2.5, "x": 0}}
}


class MathExpressionHandlerAPIView(APIView):

    def get(self, request, format=None):
        return Response(GET_MSG, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        serializer = AlgebraicExpressionSerializer(data=request.data)

        if serializer.is_valid():
            meh = MathExpressionHandler(serializer.data['expression'], serializer.data['variables'])

            return Response({RESULT_NAME: meh.calculate()}, status=status.HTTP_200_OK)
        return Response({RESULT_NAME: f"ValidationError: {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
