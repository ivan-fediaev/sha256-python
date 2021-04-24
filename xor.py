import sys,time 

class XOR:

    def __init__(self):
        self.xorBinaries()

    def xorBinaries(self):
        binArgs = ["0b1001010",
        "0b111111",
        ]

        if len(sys.argv)-1 >= 2:
            args = sys.argv[1:]
            intArgs = map(int,args)
            binArgs = list(map(bin,intArgs))

        maxLen = self.parseBinaries(binArgs)

        for i in range(len(binArgs)):
            print(binArgs[i])

        print('-'*32)

        result = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"

        for i in reversed(range(32)):
            if 31-i>maxLen:
                break

            currSum = 0 
            for val in binArgs:
                currSum += int(val[i])
                if currSum > 1:
                    result[i] = '0'
                    break
            if currSum == 1:
                result[i] = '1'

            time.sleep(0.15)
            print(''.join(result) + '\n' + ''.join(pointer),end='\033[1A\r')
            pointer[i-1],pointer[i] = "↑"," "
            time.sleep(0.15)


        print(''.join(result))
                




    
    
    def parseBinaries(self, binArgs):
        for i in range(len(binArgs)):
            binArgs[i] = binArgs[i].lstrip('-0b')

        maxLen = max(list(map(len,binArgs)))

        for i in range(len(binArgs)):
            currArg = binArgs[i]
            leadingZeroes = '0'*(32-len(currArg))
            binArgs[i] = leadingZeroes + binArgs[i]

        return maxLen


XOR()