#!/usr/bin/env python

class LimitError(Exception):
    def __init__(self, msg):
        self._msg = msg
    def info(self):
        return self._msg

def type_limit(*typeLimit, **returnType):
    def test_value_type(func):
        def wrapper(*param, **kw):
            length = len(typeLimit)
            print("Len(typelimit):{}; len(param):{}".format(length, len(param)))
            if length != len(param):
                raise LimitError(
                    "The list of typeLimit and param must have the same2 length")
            for index in range(length):
                t = typeLimit[index]
                p = param[index]
                if not isinstance(p, t):
                    raise LimitError("The param %s should be %s,but it's %s now!" % (
                        str(p), type(t()), type(p)))
            res = func(*param, **kw)
            if "returnType" in returnType:
                limit = returnType["returnType"]
                if not isinstance(res, limit):
                    raise LimitError(
                        "This function must return a value that is %s,but now it's %s" % (limit, type(res)))
            return res
        return wrapper
    return test_value_type