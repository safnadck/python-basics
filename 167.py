# raisea atypeerror if x is not an integer

x = "hello"
if not type(x) in int:
    raise TypeError("only integer are allowed")