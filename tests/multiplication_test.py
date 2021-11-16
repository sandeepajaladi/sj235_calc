"""Testing Subtraction"""
from calc.calculations.multiplication import Multiplication

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0, 2.0)
    multiplication = Mutiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 2
