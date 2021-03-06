import sys,time

class Majority:
    def __init__(self):
        self.majority()

    def majority(self):
        binArgs = ["0b101010",
        "0b111111",
        "0b101000"]

        if len(sys.argv)-1 >= 2:
            args = sys.argv[1:]
            intArgs = map(int,args)
            binArgs = list(map(bin,intArgs))

        self.parseBinaries(binArgs)

        for i in range(len(binArgs)):
            print(binArgs[i])

        print('-'*32)

        result = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"

        for i in reversed(range(32)):
            currZeros,currOnes = 0,0
            for val in binArgs:
                if val[i] == '1':
                    currOnes += 1
                else:
                    currZeros += 1

            if currZeros > currOnes:
                result[i] = '0'
            else:
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
        
Majority()