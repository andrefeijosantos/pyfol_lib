class NameAlreadyDefinedException(Exception):
    def __init__(self, name):
        self.msg = name + " already defined"

    def __str__(self):
        return self.msg

class NameNotDefinedException(Exception):
    def __init__(self, name):
        self.msg = name + " not defined"

    def __str__(self):
        return self.msg

class InvalidNameException(Exception):
    def __init__(self, name):
        self.msg = name + " : invalid name"

    def __str__(self):
        return self.msg

class NoParamethersException(Exception):
    def __init__(self, tp):
        self.msg = tp + " needs at least one paramether (got 0)"

    def __str__(self):
        return self.msg

class NotInstanceOf(Exception):
    def __str__(self):
        return "wrong type"

class EntityIsNotInstaceOf(Exception):
    def __init__(self, tp):
        self.msg = f"argument is not instance of {tp}"

    def __str__(self):
        return self.msg