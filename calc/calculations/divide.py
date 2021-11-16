"""Divide Class"""
from calc.calculations.calculation import Calculation


class Divide(Calculation):
    """divide calculation object"""
    def get_result(self):
        """get the divide results"""
        result = 1.0
        for value in self.value:

            if self.value <= 0:
                return "Error"
            return self.value / result

