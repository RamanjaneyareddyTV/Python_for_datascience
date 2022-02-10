# ----------------------------------------------------------------
# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number
# ----------------------------------------------------------------
# Algorithm
#
# ----------------------------------------------------------------

# If only one element in missing
array1 = [1,2,3,4,5,6,7]
array2 = [3,7,2,1,4,6]

missing_number = (sum(array1)- sum(array2))
print(missing_number)

# If only more than one element in missing

array3 = [1,2,3,4,5,6,7]
array4 = [3,7,2,4,6]
missing_array = []

for elem in array3:
    if elem not in array4:
        missing_array.append(elem)
print(missing_array)