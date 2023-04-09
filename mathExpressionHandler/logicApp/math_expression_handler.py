from .default_variables import default_variables
from mathExpressionHandler.exceptions import MathModuleError as MME


class MathExpressionHandler:
    def __init__(self, expression: str, variables: dict, loger=None):
        self.prepare_expression(expression)
        self._vars = self.__merge_variables(default_variables, variables)
        self._loger = loger

    def calculate(self):
        return eval(self._expression, {'__builtins__': {}}, self._vars)

    def __merge_variables(self, default_vars, user_vars):
        if not (self.__intersection_list(user_vars.keys(), default_vars.keys())):
            return {**default_variables, **user_vars}
        else:
            raise MME(MME.MSGs.res_name)

    def __intersection_list(self, list1, list2):
        return set(list1).intersection(list2)

    def prepare_expression(self, expression):
        expression = expression.replace('^', '**').replace(' ', '')

        self._expression = expression
