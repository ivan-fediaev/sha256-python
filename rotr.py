import sys,time
import collections

class RotateRight:

    def __init__(self):
        self.shiftRight()

    def shiftRight(self):
        binary = "0b110011"
        rr = 32

        if len(sys.argv)-1 >= 2:
            binary = bin(int(sys.argv[1]))
            rr = int(sys.argv[2])

        binary = binary.lstrip("-0b")
        leadingZeroes = '0'*(32-len(binary))
        binary = leadingZeroes + binary

        print(binary)

        binQueue = collections.deque(binary)
        for _ in range(rr):
            popped = binQueue.pop()
            binQueue.appendleft(popped)
            print(''.join(binQueue),end='\r')
            time.sleep(0.15)


        print(''.join(binQueue))


RotateRight()