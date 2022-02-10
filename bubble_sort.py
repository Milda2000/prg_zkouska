#function for getting a list of numbers from user
def inputList(text):
    #incialization of the list
    numbers = []
    #function obtains values from user and tests if they pass the requirements
    while True:
        try:
            numbers = [float(num) for num in input(text).split()]
            if len(numbers) < 2:
                print("Input must be at least two numbers")
            else:
                break
        except ValueError:
            print("Input wasn't numeric")
    #function prints out a list of numbers inputted by the user
    print(f"List of input values:\n{numbers}")
    #function returns a list of numbers inputted by the user
    return numbers

def bubbleSort(list):
    #get the length of the list
    length = len(list)
    #function goes through the elements in the list as many times as they are elements in the list (minus one) 
    for i in range(length-1):
        #function goes through all of the elements in the list (except the last one), compares them to the value of the element on the right and if needed swaps them
        for j in range(length-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    #function returns the sorted list
    return list

#get numbers from user
numbers = inputList("Input numbers that are supposed to be sorted (divide them by spacebar):")

#use of bubble sort to sort the input values
sorted_numbers = bubbleSort(numbers)

#print out a list of sorted numbers for user into the console
print(f"Sorted numbers:\n{sorted_numbers}")