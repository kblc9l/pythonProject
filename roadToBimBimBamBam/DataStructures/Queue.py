from queue import Queue

fifo = Queue()
fifo.put('1')
fifo.put('1')
fifo.put('1')
fifo.put('1')
print(fifo.qsize())
print(fifo.get())
print(fifo.get())
print(fifo.get())
print(fifo.get())
print(fifo.qsize())
