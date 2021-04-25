import sys,time

class SHA256:
    def __init__(self):
        self.SHA256()

    def SHA256(self):

        message = "abcdefghijk"

        if len(sys.argv)-1 == 1:
            message = sys.argv[1]

        print("input:\t " + message)

        bytes = []
        for c in message:
            bytes.append(ord(c))

        print("bytes:\t " + str(bytes))

        message = []
        for b in bytes:
            binString = bin(int(b)).lstrip('-0b')
            binString = (8-len(binString))*'0' + binString
            message.append(binString)

        message = ''.join(message)
        print("message: " + str(message))

        print("")
        print("---------")
        print("padding: ({} bits)".format(len(message)))
        print("---------")

        print("message: " + message,end='\r')
        time.sleep(3)
        print("message: " + message + '1',end='',flush=True)

        message = message + '1'

        print("",end='\033[2A\r')
        print("padding: ({} bits)".format(len(message)))
        print("",end='\033[1B')

        padding = (448 - len(message))*'0'
        
        message = message + padding

        printOut = "message: " + message

        for val in printOut:
            time.sleep(0.07)
            print(val,flush=True,end='')
        
        messageSizeBin = bin(len(message)).lstrip('-0b')
        message = message + padding

        padding = (64 - len(messageSizeBin))*'0'

        messageSizeBin = padding + messageSizeBin

        for val in messageSizeBin:
            time.sleep(0.004)
            print(val,end='',flush=True)

        message = message + messageSizeBin


        print("")

        








SHA256()