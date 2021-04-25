import sys,time

class Choice:
    def __init__(self):
        self.choice()


    def choice(self):
        binArgs = ["0b111111110000000011111111",
        "0b1111111111111111",
        "0b11111111111111110000000000000000"]

        if len(sys.argv)-1 == 3:
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
            
            if binArgs[0][i] == '0':
                result[i] = binArgs[2][i]
            else:
                result[i] = binArgs[1][i]

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


Choice()          