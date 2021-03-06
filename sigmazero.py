import sys,time

class SigmaZero:

    def __init__(self):
        self.sigmaZero()

    def sigmaZero(self):

        binary = "0b110011010001"

        if len(sys.argv)-1 == 1:
            arg = sys.argv[1]
            binary = int(arg)

        binary = binary.lstrip("-0b")
        leadingZeroes = '0'*(32-len(binary))
        binary = leadingZeroes + binary

        rotrText7 = "ROTR 7:  "
        rotrText18 = "ROTR 18: "
        shrText3 = "SHR 3:   "


        print("x:\t " + binary)
        print("\t " + 32*'-')
        print(rotrText7 + binary)
        print(rotrText18 + binary)
        print(shrText3 + binary)
        print("\t " + 32*'-')
        
        rotrText7List = list(binary)
        for _ in range(7):
            popped = rotrText7List.pop()
            rotrText7List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[4A')
            print(rotrText7+''.join(rotrText7List))
            print("",end='\033[3B')

        rotrText18List = list(binary)
        for _ in range(18):
            popped = rotrText18List.pop()
            rotrText18List.insert(0,popped)

            time.sleep(0.15)
            print("",end='\033[3A')
            print(rotrText18+''.join(rotrText18List))
            print("",end='\033[2B')

        shrText3List = list(binary)
        for _ in range(3):
            shrText3List.pop()
            shrText3List.insert(0,'0')
            print("",end='\033[2A')
            print(shrText3+''.join(shrText3List),end='\r')
            print("",end='\033[2B')
            time.sleep(0.2)

        result = 32*['0']
        pointer = 32*[" "]
        pointer[-1] = "↑"

        binArgs = [rotrText7List, rotrText18List, shrText3List]
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



        
            





SigmaZero()
        