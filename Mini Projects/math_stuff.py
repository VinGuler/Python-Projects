### interesting math functions ###

# n! <- Non Recursive
def ace(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1  
    return result

# n! <- Recursive
def ace2(n):
    if n == 0:
        return 1
    else:
        return n * ace2(n-1)

# x^n
def power(x, n):
    i = 1
    result = 1
    while i <= n:
        result *= x
        i += 1
    return result

# f'(x)
# Calculating the 1st derivative from simple math functions
''' Letting the user know how i want to get the function '''
def derivative():
    print("Please enter a function this way : a_x^n_+_b_x^m_+_c")
    func_before = input("")
    func_after = derivative_logic(func_before)
    return func_after

''' The main logic and stuff '''
def derivative_logic(f):
    # Splitting the given string to a list of values
    func = f.split("_")
    # Multiplyer of the first power
    a = int(func[0])
    # First x to the first power
    x2 = func[1]
    temp = x2.split("^")
    # First X
    fx = temp[0]
    #First Power
    fpow = int(temp[1])
    # First sign
    fsign = func[2]
    # Multiplyer of the second power
    b = int(func[3])
    # Second x to the second power
    x1 = func[4]
    temp = x1.split("^")
    # Second x
    sx = temp[0]
    # Second Power
    spow = int(temp[1])

    # Whatever 'a' was, it's being multiplyed by the first power
    a *= fpow
    # Power goes down by one
    fpow -= 1
    # Whatever 'b' was, it's being multiplyed by the first power
    b *= spow
    # Power goes down by one
    spow -= 1
    # Last object of the function (free from x) 
    c = 0

    # Creating the derivative in a string form
    if spow == 0 and fpow != 0:
        derivated_func = str(a) + "_" + fx + "^" + str(fpow) + "_" + fsign + "_" + str(b)
    elif spow != 0 and fpow != 0:
        derivated_func = str(a) + "_" + fx + "^" + str(fpow) + "_" + fsign + "_" + str(b) + "_" + sx + "^" + str(spow)
    elif spow == 0 and fpow == 0:
        derivated_func = str(a) + "_" + fsign + "_" + str(b)
    elif spow != 0 and fpow == 0:
        derivated_func = str(a) + "_" + fsign + "_" + str(b) + "_" + sx + "^" + str(spow)

    return derivated_func


# creating Fibonachi, function accepts number of itarations.
# for example, fib(3) will return 1, 1, 2.
# fib(5) will return 1, 1, 2, 3, 5.
def fib(n):
    root1 = 1
    root2 = 1
    temp = 0
    print(root1)
    print(root2)
    while n > 2:
        temp = root2 + root1
        print(temp)
        root1 = root2
        root2 = temp     
        n -= 1

# Check Wether a sum of to numbers is in a given ORDERED list
# For example: sum = 4 in [1, 2, 3,, 4] => True
# For example: sum = 5 in [1, 3, 5] => False 
def search_sum(num_list, wanted_sum):
    # Indeces
    first = 0
    last = len(num_list) - 1
    # While we have both the first and last indeces not on the same spot
    while first != last:
        # If we found the wanted sum -> Success -> break out of the loop
        if num_list[first]+num_list[last] == wanted_sum:
            print("The pair is : " + str(num_list[first]) + ", " + str(num_list[last]))
            break
        # else
        # if the current numbers sum < wanted -> move the first index forwards
        # if the current numbers sum < wanted -> move the last index backwards
        else:
            if num_list[first]+num_list[last] < wanted_sum:
                first += 1
            elif num_list[first]+num_list[last] > wanted_sum:
                last -= 1
    # If we reached the same place in the list, the list doesn't have the sum
    if first == last:
        print("No pair was found")
        
                
                




    
    
    
