#function for getting a list of numbers from user
def inputList(text):
    #incialization of a list of numbers
    numbers = []
    #function obtains values from user and tests if they pass the requirements
    while True:
        try:
            numbers = [float(num) for num in input(text).split()]
            if len(numbers) < 2:
                print("Input must be atleast two numbers")
            else:
                break
        except ValueError:
            print("Input wasn't numeric")
    #function prints out a list of numbers inputted by the user
    print(f"List of input values:\n{numbers}")
    #function returns a list of numbers inputted by the user
    return numbers

#function for getting a median from a list of numbers
def fMedian(list):
    #sort the list
    list.sort()
    #get the lenght of the list
    list_length = len(list)
    #if the lenght of the list is even the function returns the median as a value of a mean of numbers at indexes (list_lenght/2)-1 and list_lenght/2
    if list_length%2 == 0:
        num1 = list[int((list_length/2)-1)]
        num2 = list[int(list_length/2)]
        return (num1+num2)/2
    else:
        #if the length of the list is odd the function returns the median as a value of the number in the middle of the list  
        return list[list_length//2]

#get numbers from user
numbers = inputList("Input numbers to calculate their median (divide them by a spacebar):")

#call function to calculate the median
median = fMedian(numbers)

#print out the median of input values for user into the console
print(f"Median of input data is: {median}")