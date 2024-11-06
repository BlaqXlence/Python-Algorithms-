def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """
    
    for i in range(len(lst)):  # Number of rows
        for j in range(len(lst[0])):  # Number of cols
            if lst[i][j] == number:  # If number is found
                return True
            
    return False  # If number is not found

lst = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [27, 29, 30, 31],
        [32, 33, 39, 50]
    ]

print(find_in(lst, 30))
