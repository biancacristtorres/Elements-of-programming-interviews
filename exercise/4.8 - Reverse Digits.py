
num = input("What is your favorite number? ")
number = int(num)



def revert(x):
    result, x_remanining =0, abs(x)

    while x_remanining:
        result = result * 10 + x_remanining % 10
        x_remanining //=10
    return -result if x <0 else result    
    

result = revert(number)

print(result)
