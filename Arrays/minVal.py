# Current Array
my_array = [10, 2, 3, 4, 7, 20, 21, 30]

# Setting the current array to the 1st element in the array
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest Value:', minVal)
