import sys,time

class BigSigmaZero:

    def __init__(self):
        self.uSigmaZero()

    def uSigmaZero(self):

        binary = "0b110011010001"

        if len(sys.argv)-1 == 1:
            arg = sys.argv[1]
            binary = int(arg)

        binary = binary.lstrip("-0b")
        leadingZeroes = '0'*(32-len(binary))
        binary = leadingZeroes + binary

        rotrText2  = "ROTR 2:  "
        rotrText13 = "ROTR 13: "
        rotrText22 = "ROTR 22: "


        print("x:\t " + binary)
        print("\t " + 32*'-')
        print(rotrText2 + binary)
        print(rotrText13 + binary)
        print(rotrText22 + binary)
        print("\t " + 32*'-')
        
        rotrText2List = list(binary)
        for _ in range(2):
            popped = rotrText2List.pop()
            rotrText2List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[4A')
            print(rotrText2+''.join(rotrText2List))
            print("",end='\033[3B')

        rotrText13List = list(binary)
        for _ in range(13):
            popped = rotrText13List.pop()
            rotrText13List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[3A')
            print(rotrText13+''.join(rotrText13List))
            print("",end='\033[2B')

        rotrText22List = list(binary)
        for _ in range(22):
            popped = rotrText22List.pop()
            rotrText22List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[2A')
            print(rotrText22+''.join(rotrText22List),end='\r')
            print("",end='\033[2B')

        result = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"

        binArgs = [rotrText2List, rotrText13List, rotrText22List]
        for i in reversed(range(32)):
            currSum = 0
            for val in binArgs:
                currSum += int(val[i])
                if currSum > 1:
                    result[i] = '0'
                    break

            if currSum == 1:
                result[i] = '1'

            time.sleep(0.15)
            print('\t '+''.join(result) + '\n' + '\t ' + ''.join(pointer),end='\033[1A\r')
            pointer[i-1],pointer[i] = "↑"," "


        print('\t '+''.join(result))


BigSigmaZero()
        