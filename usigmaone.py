import sys,time

class BigSigmaOne:

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

        rotrText6  = "ROTR 6:  "
        rotrText11 = "ROTR 11: "
        rotrText25 = "ROTR 25: "


        print("x:\t " + binary)
        print("\t " + 32*'-')
        print(rotrText6 + binary)
        print(rotrText11 + binary)
        print(rotrText25 + binary)
        print("\t " + 32*'-')
        
        rotrText6List = list(binary)
        for _ in range(6):
            popped = rotrText6List.pop()
            rotrText6List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[4A')
            print(rotrText6+''.join(rotrText6List))
            print("",end='\033[3B')

        rotrText11List = list(binary)
        for _ in range(11):
            popped = rotrText11List.pop()
            rotrText11List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[3A')
            print(rotrText11+''.join(rotrText11List))
            print("",end='\033[2B')

        rotrText25List = list(binary)
        for _ in range(25):
            popped = rotrText25List.pop()
            rotrText25List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[2A')
            print(rotrText25+''.join(rotrText25List),end='\r')
            print("",end='\033[2B')

        result = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"

        binArgs = [rotrText6List, rotrText11List, rotrText25List]
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


BigSigmaOne()
        