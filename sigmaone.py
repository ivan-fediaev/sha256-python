import sys,time

class SigmaOne:

    def __init__(self):
        self.sigmaOne()

    def sigmaOne(self):

        binary = "0b110011010001"

        if len(sys.argv)-1 == 1:
            arg = sys.argv[1]
            binary = int(arg)

        binary = binary.lstrip("-0b")
        leadingZeroes = '0'*(32-len(binary))
        binary = leadingZeroes + binary

        rotrText17 = "ROTR 17: "
        rotrText19 = "ROTR 19: "
        shrText10 = "SHR 10:  "


        print("x:\t " + binary)
        print("\t " + 32*'-')
        print(rotrText17 + binary)
        print(rotrText19 + binary)
        print(shrText10 + binary)
        print("\t " + 32*'-')
        
        rotrText17List = list(binary)
        for _ in range(17):
            popped = rotrText17List.pop()
            rotrText17List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[4A')
            print(rotrText17+''.join(rotrText17List))
            print("",end='\033[3B')

        rotrText19List = list(binary)
        for _ in range(19):
            popped = rotrText19List.pop()
            rotrText19List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[3A')
            print(rotrText19+''.join(rotrText19List))
            print("",end='\033[2B')

        shrText10List = list(binary)
        for _ in range(10):
            shrText10List.pop()
            shrText10List.insert(0,'0')
            print("",end='\033[2A')
            print(shrText10+''.join(shrText10List),end='\r')
            print("",end='\033[2B')
            time.sleep(0.2)

        result = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"

        binArgs = [rotrText17List, rotrText19List, shrText10List]
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


SigmaOne()
        