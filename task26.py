list1 = [10, 2, 3, 5, 6, 7, 8]
even = 0
odd = 0
for num in list1:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, 'even numbers in the list')
print(odd, 'odd numbers in the list')