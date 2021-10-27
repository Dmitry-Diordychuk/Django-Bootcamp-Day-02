#!/usr/bin/python3
# coding: utf-8


import random
import beverages

class CoffeeMachine:
    def __init__(self):
        self.__serve_counter = 0

    class EmptyCup(beverages.HotBeverage):
        price = 0.90
        name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        """
        reset counter
        """
        self.__serve_counter = 0

    def serve(self, beverage):
        """
        Create an instance of class derived from Hot Beverage
        :param beverage: class derived from Hot Beverage
        :return: beverage or EmptyCup
        """
        if not issubclass(beverage, beverages.HotBeverage):
            raise Exception("Wrong class!")
        if self.__serve_counter >= 10:
            raise self.BrokenMachineException
        self.__serve_counter += 1
        rand = random.randrange(5)
        if rand == 3:
            return self.EmptyCup()
        return beverage()


if __name__ == '__main__':
    machine1 = CoffeeMachine()

    for i in range(2):
        hb = machine1.serve(beverages.HotBeverage)
        print(hb)

        coffee = machine1.serve(beverages.Coffee)
        print(coffee)

        tea = machine1.serve(beverages.Tea)
        print(tea)

        choco = machine1.serve(beverages.Chocolate)
        print(choco)

        cappuccino = machine1.serve(beverages.Cappuccino)
        print(cappuccino)

    try:
        tea = machine1.serve(beverages.Tea)
    except CoffeeMachine.BrokenMachineException as ex:
        print("Error:", ex)
        machine1.repair()

    for i in range(2):
        hb = machine1.serve(beverages.HotBeverage)
        print(hb)

        coffee = machine1.serve(beverages.Coffee)
        print(coffee)

        tea = machine1.serve(beverages.Tea)
        print(tea)

        choco = machine1.serve(beverages.Chocolate)
        print(choco)

        cappuccino = machine1.serve(beverages.Cappuccino)
        print(cappuccino)

    try:
        coffee = machine1.serve(beverages.Coffee)
    except CoffeeMachine.BrokenMachineException as ex:
        print("Error:", ex)
        machine1.repair()

    coffee = machine1.serve(beverages.Coffee)
    print(coffee)
