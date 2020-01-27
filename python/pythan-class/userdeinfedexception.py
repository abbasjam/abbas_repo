print ("User Defined Exception")
print ("----------------------")
class TooSmallValue(Exception):
    pass
class TooLargeValue(Exception):
    pass
try:
    x=int(input("enter the Mark:"))
    if x<0:
        raise TooSmallValue
    if x>100:
        raise TooLargeValue
    print ("Wow!!!!!!!!! you have given the mark within the range!!!")
except TooSmallValue:
    print ("Negative Mark is not Allowed!!!!!!!!!!!!")
except TooLargeValue:
    print ("Mark >100 is not Allowed!!!!!!!!!!!!!!!!!!!!")

