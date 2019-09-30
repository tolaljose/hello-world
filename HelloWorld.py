"""
HelloWorld.py
----------------

classes:
    1. Greeting
    2. Hello
    3. GoodBye
"""


class Greeting:
    """
    Greeting
    --------

    parents:
        -

    members (variables):
        -

    members (functions):
        1. constructor __init()___
        2. destructor __del__()
        3. get_greet()
        4. print_greet()
    """

    def __init__(self, greet_str=None):
        """
        1. constructor __init()___
            - note:
            - input:
            - return:
            - functionality:
        """
        self.greetings = greet_str

    def __del__(self):
        """
        2. destructor __del__()
            - note:
            - input:
            - return:
            - functionality:
        """
        print("Base Class destroyed")

    def greet(self):
        """
        3. _print()
            - note:
            - input:
            - return:
            - functionality:
        """
        print(self.greetings)


class Hello(Greeting):
    """
    Hello
    --------

    parents:
        1. Greeting

    members (variables):
        -

    members (functions):
        1. constructor __init()___
        2. destructor __del__()

    """

    def __init__(self, greet_str="Hello"):
        """
        - note:
        - input:
        - return:
        - functionality:
        """
        self.greetings = greet_str

    def __del__(self):
        """
        - note:
        - input:
        - return:
        - functionality:
        """
        print("Hello destroyed")
        super(Hello, self).__del__()


class GoodBye(Greeting):
    """
    GoodBye
    --------

    parents:
        1. Greeting

    members (variables):
        -

    members (functions):
        1. constructor __init()___
        2. destructor __del__()

    """

    def __init__(self, greet_str="Good Bye"):
        """
        - note:
        - input:
        - return:
        - functionality:
        """
        self.greetings = greet_str

    def __del__(self):
        """
        - note:
        - input:
        - return:
        - functionality:
        """
        print("GoodBye destroyed")
        super(GoodBye, self).__del__()


""""End of the script"""
