import os,traceback,sys,Ice
import py2serv

class Sender(Ice.Application):
    def run(self,args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1

        test = py2serv.SenderPrx.checkedCast(\
            self.communicator().propertyToProxy('Sender.Proxy').ice_twoway().ice_timeout(-1).ice_secure(False))
        if not twoway:
            print(args[0] + ": invalid proxy")
            return 1

        c = None
        print("test")
        while c != 'x':
            try:
                sys.stdout.write("Number of messages: ")
                #sys.stdout.flush()
                c = sys.stdin.readline().strip()
                for i in range(0, int(c)):
                    print("msg #{} sent".format(i))
                    
            except KeyboardInterrupt:
                break
            except EOFError:
                break
            except Ice.Exception as ex:
                print(ex)
                
        return 0

app=Sender()
#app.run(sys.argv)
sys.exit(app.main(sys.argv, "sender.cfg"))

