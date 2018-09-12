''''ways to reverse strings in python(ascending order of speed)'''
#using a looop............layman

def reverse(input):
    rev = ""
    for i in range(len(input)-1,-1,-1):
        rev+=input[i]
    return rev

#by converting into a string 
def revstr1(input2):
    ls= list(input2)
    ls.reverse()
    return "".join(ls)

#using slicing.............. 'The Flash' of the methods
def revstr2(input3):
    return input3[::-1]

