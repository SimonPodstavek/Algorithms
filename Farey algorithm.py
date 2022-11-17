# Farey algorithm to convert any number into a fraction
# Inputs are: Number being converted, Number of iterations, Whole number range that the converted number is a part of 
# Output: Number in a fraction format, Deviation from the number


def find_fraction(number: float,iterations: int, integer_range: list) -> list:
    fraction_set=[[integer_range[0],1],[1,integer_range[1],1]]
    for x in range(0,iterations):
        mediant=(fraction_set[0][0]+fraction_set[1][0])/(fraction_set[0][1]+fraction_set[1][1])
        fraction_set.insert(1,[(fraction_set[0][0]+fraction_set[1][0]),(fraction_set[0][1]+fraction_set[1][1])])
        if x+1 != iterations: 
            if mediant > number:
                fraction_set.pop()
            else:
                fraction_set.pop(0)
        else:

            return fraction_set[1],abs((fraction_set[1][0]/fraction_set[1][1])-number)


n=0.336944434029
print(find_fraction(n,45,[0,1]))
