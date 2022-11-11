import numbers

class CalcError(Exception):
    pass

class Calc:
    def soma(self,op1,op2):
        self._check_type(op1)
        self._check_type(op2)
        return op1+op2

    def _check_type(self, op):
        if not isinstance(op,numbers.Number):
            raise CalcError()