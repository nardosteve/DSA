# Sorts items in the array from the lowest to the highest
# companres then swaps from right to left
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array) # 8

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)