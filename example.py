def foo():
    """ foo """
    pass

    # valid comment
    """ invalid comment inside foo """
    """
    invalid comment block
    """

    def bar():
        """ bar """
        pass

        # valid comment
        """ invalid comment inside bar """


class Bar:
    """ Bar """
    # valid comment
    """ invalid comment inside Bar """

    def __init__(self):
        """ __init__ """
        print("__init__")

        # valid comment
        """ invalid comment inside __init__ """
