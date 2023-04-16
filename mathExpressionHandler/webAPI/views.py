import logging

from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from mathExpressionHandler.logicApp import MathExpressionHandler
from .serializers import AlgebraicExpressionSerializer
from mathExpressionHandler.exceptions import MathModuleError

logger = logging.getLogger(__name__)



class MathExpressionHandlerAPIView(APIView):
    http_method_names = ['get', 'put']
    RESULT = "result"
    DETAIL = 'detail'

    GET_MSG = {
        'header': "This is an api for processing mathematical expressions.",
        'explanation': "The expression allows numbers, variable names, signs of arithmetic operations, "
                       "exponentiation (including non-integer) ^, functions lg (decimal logarithm), "
                       "then ln (natural logarithm), trigonometric functions sin, cos, tan, asin, acos, atan.",
        'example': {"expression": "4-2*a/(5*x-3)", "variables": {"a": 2.5, "x": 0}}
    }

    def get(self, request, format=None):
        return Response(self.GET_MSG, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        logger.info(f'Got request: {request.data}')
        try:
            serializer = AlgebraicExpressionSerializer(data=request.data)
            if serializer.is_valid():
                logger.debug('Data is valid')
                meh = MathExpressionHandler(serializer.data['expression'], serializer.data['variables'])
                calculation_result = meh.calculate()
                logger.debug(f'Calculation is success. {calculation_result=}')
                return Response({self.RESULT: calculation_result}, status=status.HTTP_200_OK)

            return Response({self.DETAIL: f'ValidationError: {serializer.errors}'},
                                status=status.HTTP_400_BAD_REQUEST)

        except ParseError as e:
            return Response({self.DETAIL: f'ParseError: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)
        except NameError as e:
            return Response({self.DETAIL: f'NameError: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)
        except MathModuleError as e:
            return Response({self.DETAIL: f'MathModuleError: {e.args[0]}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e.__traceback__)
            raise e
