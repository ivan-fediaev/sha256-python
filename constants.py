import time,math

class Constants:
    def __init__(self):
        self.constants()


    def constants(self):
        numPrimes = 0 
        num = 2
        primeNums = []
        while numPrimes < 64:
            for i in range(2,num):
                if (num % i) == 0:
                    num += 1
                    break
            else:
                numPrimes += 1
                primeNums.append(num)
                num += 1

        constants = []
        for i,p in enumerate(primeNums):
            time.sleep(0.15)
            cubedPrime = str(p**(1./3.))
            print(str(i) + " = " + "∛{}".format(p) + " = " + cubedPrime,end='\r')
            
            cubedPrime = float(cubedPrime)
            fractional = cubedPrime - math.floor(cubedPrime)
            
            time.sleep(0.15)
            print(str(i) + " = " + "∛{}".format(p) + " = " + str(fractional),end='\r')

            constant = bin(math.floor(fractional*2**32)).lstrip('-0b')
            constant = (32-len(constant))*'0' + constant
            time.sleep(0.15)
            print(str(i) + " = " + str(constant))
            constants.append(constants)



        return constants









Constants()

