#!/usr/bin/python3
# coding: utf-8


class Intern:
    def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        """
        Do nothing
        """
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        """
        Make coffee
        :return: coffee
        """
        return Intern.Coffee()


if __name__ == '__main__':
    intern_Mark = Intern("Mark")
    intern_nobody = Intern()

    print(intern_Mark)
    print(intern_nobody)
    coffee = intern_Mark.make_coffee()
    print(coffee)
    try:
        intern_nobody.work()
    except Exception as ex:
        print(ex)
