fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [i for i in fruits if i.startswith('a')]
newlist = [i if i != 'apple' else 'orange' for i in fruits]
print(newlist)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(*[[row[i] for row in matrix] for i in range(4)])
#  [1, 5, 9] [2, 6, 10] [3, 7, 11] [4, 8, 12]