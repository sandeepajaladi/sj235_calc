"""Testing Subtraction"""
from calc.calculations.multiply import Multiply

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0, 2.0)
    multiply = Mutiply(mynumbers)
    #Act
    #Assert
    assert multiply.get_result() == 2
