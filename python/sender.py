import os
import traceback
import sys
import Ice
Ice.loadSlice('../ice/pyserv.ice')
import pyserv

class Sender(Ice.Application):
    def run(self, args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1
        #print("TEST")
        communicator = Ice.initialize(sys.argv)
        ##NEXT STEP
        #sender = pyserv.SenderPrx.checkedCast(communicator.stringToProxy("hello:tcp -h localhost -p 10002"))

        c = None
        while c != 'x':
            try:
                sys.stdout.write("(Enter 'x' to stop)\n")
                sys.stdout.write("Number of messages to send: ")
                #sys.stdout.flush()
                c = sys.stdin.readline().strip()
                if c == 'x':
                    pass # Nothing to do
                else:
                    for i in range(0, int(c)):
                        print("msg #{} sent".format(i))
                        #sender.send()
                        #oneway.sayHello(delay)
            except KeyboardInterrupt:
                break
            except EOFError:
                break
            except Ice.Exception as ex:
                print(ex)
        return 0

app = Sender()
status = app.main(sys.argv)
sys.exit(status)
