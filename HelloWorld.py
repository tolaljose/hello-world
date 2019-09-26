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
        self.greeting_str = greet_str

    def __del__(self):
        """
        2. destructor __del__()
            - note:
            - input:
            - return:
            - functionality:
        """


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
        self.greeting = Greeting(greet_str)

    def __del__(self):
        """
        - note:
        - input:
        - return:
        - functionality:
        """
        pass


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
        self.greeting = Greeting(greet_str)

    def __del__(self):
        """
        - note:
        - input:
        - return:
        - functionality:
        """
        del self.greeting


""""End of the script"""
