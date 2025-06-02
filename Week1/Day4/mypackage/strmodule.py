#  FIND THE LENGHT OF STRING
def strlen(str):
    count = 0
    for char in str:
        count+=1
    return count

#REVERSE STRING FUNCTION
def strreverse(str):
    reverse = " "
    for char in str:
        reverse = char+reverse
    return reverse    