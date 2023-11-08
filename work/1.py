f = open('../blidingtype/data/easy_words.txt', 'r', encoding='utf8')

print(*set(f.read().split()))