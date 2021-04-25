import sys,time



class AddBinary:

    def __init__(self):
        self.addBinaries()

    def addBinaries(self):
        binArgs = ["0b101010",
        "0b111111",
        "0b101001",
        "0b111111"
        ]

        if len(sys.argv)-1 >= 2:
            args = sys.argv[1:]
            intArgs = map(int,args)
            binArgs = list(map(bin,intArgs))
    
            
        maxLen = self.parseBinaries(binArgs)
        

        for i in range(len(binArgs)):
            if i == len(binArgs)-1:
                print(binArgs[i]+' +')
            else:
                print(binArgs[i])

        print('-'*32)

        carryOver = 0
        sum = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"
        for  i in reversed(range(32)):
            currSum = 0
            for val in binArgs:
                currSum += int(val[i])

            currSum += carryOver

            if currSum == 0 and 31-i>maxLen:
                break

            if currSum >= 1:
                if currSum == 1:
                    carryOver = 0
                    sum[i] = '1'
                elif currSum == 2:
                    carryOver = 1
                    sum[i] = '0'
                else:
                    carryOver = currSum-2
                    sum[i] = '1'
                    
            time.sleep(0.1)
            print(''.join(sum) + '\n' + ''.join(pointer),end='\033[1A\r')
            pointer[i-1],pointer[i] = "↑"," "
            time.sleep(0.2)
            

        print(''.join(sum))

        return ''.join(sum)
        


    
    def parseBinaries(self, binArgs):
        for i in range(len(binArgs)):
            binArgs[i] = binArgs[i].lstrip('-0b')

        maxLen = max(list(map(len,binArgs)))

        for i in range(len(binArgs)):
            currArg = binArgs[i]
            leadingZeroes = '0'*(32-len(currArg))
            binArgs[i] = leadingZeroes + binArgs[i]

        return maxLen

AddBinary()




