"""Testing Subtraction"""
from calc.calculations.divide import Divide

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (4.0, 2.0)
    divide = Divide(mynumbers)
    #Act
    #Assert
    assert divide.get_result() == 2
