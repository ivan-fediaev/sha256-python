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
        
        time.sleep(1)
        rotrText7List = list(binary)
        for _ in range(7):
            popped = rotrText7List.pop()
            rotrText7List.insert(0,popped)

            time.sleep(1)
            print("",end='\033[3A')
            print(rotrText7+''.join(rotrText7List))
            print("",end='\033[2B')



SigmaZero()
        