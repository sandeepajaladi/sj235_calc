"""Subtraction calculation that inherits value A and value B from the calculation class"""

from calc.calculation import Calculation

class Subtraction(Calculation):
        """Subtraction class has one method to get the result of A and B come from the parent class"""
    def get_result(self):
        """Get result from calculation"""
        return self.value_a - self.value_b
