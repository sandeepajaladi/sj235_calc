"""Calculation history Class"""
class Calculations:
    history = []
    # pylint: disable=too-few-public-methods
    """This is the history static property"""
    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True

    """This is the count history static property"""
    @staticmethod
    def count_history():
        return len(Calculations.history)

    """This is the get last calculation  static property"""
    @staticmethod
    def get_last_calculation():
        return Calculations.history[-1]

    """This is a first calculation static property"""
    @staticmethod
    def get_first_calculation():
        return Calculations.history[-1]

    """This is a get calculation static property"""
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    """This is a add calculation static property"""
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
