"""
    Given an array of integers, return a new array such that each element at index i of the new array 
    is the product of all the numbers in the original array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
def generate_array_old(input_array):
    """
        Easy mode: sum all elements and then divide by the element to get the desired.
    """
    result = []
    for index in range(0, len(input_array)):
        result.append(reduce(lambda a, b: a * b, input_array[:index] + input_array[index + 1:]))
    return result

def generate_array(input):
    return [reduce(lambda a, b: a * b, input[:x] + input[x+1:]) for x in range(len(input))]

