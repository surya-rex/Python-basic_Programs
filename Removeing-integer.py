import re

str=input("Enter Value : ")

pattern=r'[0-9]'

res=re.sub(pattern,"",str)

print ("After removing numbers: ", res )