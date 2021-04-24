import sys,time

class ShiftRight:

    def __init__(self):
        self.shiftRight()

    def shiftRight(self):
        binary = "0b10101010101010101010101010101010"
        shr = 32

        if len(sys.argv)-1 >= 2:
            binary = bin(int(sys.argv[1]))
            shr = min(int(sys.argv[2]),32)

        binary = binary.lstrip("-0b")
        leadingZeroes = '0'*(32-len(binary))
        binary = leadingZeroes + binary

        print(binary)

        binList = list(binary)
        for _ in range(shr):
            binList.pop()
            binList.insert(0,'0')
            print(''.join(binList),end='\r')
            time.sleep(0.2)


        print(''.join(binList))



ShiftRight()



        
        
