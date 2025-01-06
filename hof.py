# Higher-order functions 
# Wrapper => Wraps a function in some additional functionality

numbers = [10, 17, 20, 40] 

# A function that squares the numbers
# def squares(nums): 
#     result = []
#     for n in nums:
#       result.append(n ** 2)

#     return result
# print(squares(numbers))

# Builds a new list with the result of calling cb of each iteam in the list

def with_list(nums, cb):
    result = []
    for n in nums:
      result.append(cb(n))

    return result

def square(n):
    return n * n

def cube(n):
   return n ** 3

# Main
# print(with_list(numbers, cube))
print(list(map(lambda x: x * 2, numbers))) # diff b2n map and filter

# Filter even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))