"""Multiplication calculation that inherits the value A and value B from the calculation class"""

from calc.calculation import Calculation

class Multiplication(Calculation):
    """Multiplication class has a method to get the result of the calculation from the parent class"""
    def get_result(self):
        """Returns result from the function"""
        return self.value_a * self.value_b
