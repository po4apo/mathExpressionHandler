import dataclasses


class MathModuleError(Exception):
    @dataclasses.dataclass()
    class MSGs:
        res_name = 'Uses reserved names'

    def __init__(self, *args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        if self.msg:
            return f'MathModuleError, {self.msg}'
        else:
            return f'MathModuleError occurred'
