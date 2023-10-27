from queue import LifoQueue

# Initializing a stack
lifo = LifoQueue()
lifo.put('1')
lifo.put('2')
lifo.put('3')
print(lifo.qsize())
print(lifo.get())
print(lifo.get())
print(lifo.get())

print(lifo.qsize())

