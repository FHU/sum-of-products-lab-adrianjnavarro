#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return "Error"
    
    return sum(a * b for a, b in zip(list1, list2))
    

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    input_string1 = input()
    input_string2 = input()

    list1 = [int(char) for char in input_string1 if char.split()]
    list2 = [int(char) for char in input_string2 if char.split()]

    result = sum_of_products(list1, list2)
    print(result)

