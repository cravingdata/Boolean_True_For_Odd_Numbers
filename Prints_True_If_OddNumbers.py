numbers = [1, 5, 3, 11, 19, 17]
count = 0
for number in numbers:
    count += number % 2 == 1

print(len(numbers) == count)

# prints True ony if all numbers in list are odd. 
