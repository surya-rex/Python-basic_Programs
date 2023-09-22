
"""Write a function that should have a single parameter
if I pass an argument it should say “HAI” and if I don’t give an argument it should say “BYE”."""


def fun(mess=None):
     if mess==None:
           return "Bye"
     else:
          return "Hai"
          
print(fun()) # Without Argument
print(fun("Hello")) # With Argument