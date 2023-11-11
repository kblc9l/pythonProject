import sys

# list1 = list(set([i.rstrip() for i in sys.stdin]))
# f1 = open('../blidingtype/data/medium_words.txt', 'r', encoding='utf8')
# s = f1.read().split(' ')
#
# f2 = open('../blidingtype/data/medium_words.txt', 'w', encoding='utf8')
# f2.write(' '.join(s + list1))


#
# print(*set(filter(lambda x: len(x) > 2, input().split(' '))))
# print()
# print(*set(filter(lambda x: len(x) <= 3, input().split(' '))))

print(*set(input().split(' ')))