"""Divide calculation that inherits the value A and value B from the calculation class"""

from calc.calculation import Calculation

class Divide(Calculation):
    """Divide class has a method to get the result of calculation from the parent class"""
    def get_result(self):
        """Returns result from the function"""
        result = 1.0
        for value in self.values:
            if self.value <= 0:
                return "Error"
            return self.value / result
