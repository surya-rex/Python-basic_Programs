

""" Write a python function to create a least possible palindrome of the
given string (ip: ball op: ballab and ip: bala op: balab)"""

def process():
     val=input("Enter Something :")
     one=val[0]
     two=val[1]
     
     result=val+two+one
     return result
     
print(process())