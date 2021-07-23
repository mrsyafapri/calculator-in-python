import math


class Calculator:
    """Simple Calculator"""

    def __init__(self, mark=0.0):
        self.__mark = mark

    def addition(self, first_number, second_number):
        self.__mark = first_number + second_number
        return self.__mark

    def substraction(self, first_number, second_number):
        self.__mark = first_number - second_number
        return self.__mark

    def multiplication(self, first_number, second_number):
        self.__mark = first_number * second_number
        return self.__mark

    def division(self, first_number, second_number):
        self.__mark = first_number / second_number
        return self.__mark

    def modulus(self, first_number, second_number):
        self.__mark = first_number % second_number
        return self.__mark

    def exponentiation(self, first_number, second_number):
        self.__mark = first_number ** second_number
        return self.__mark

    def sin(self, number):
        self.__mark = math.sin(number)
        return self.__mark

    def cos(self, number):
        self.__mark = math.cos(number)
        return self.__mark

    def tan(self, number):
        self.__mark = math.tan(number)
        return self.__mark
