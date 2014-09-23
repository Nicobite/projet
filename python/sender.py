import os
import traceback
import sys
import Ice
Ice.loadSlice('pyserv.ice')
import py2serv

class Sender(Ice.Application):
    def run(self, args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1
        #print("TEST")
        twoway = py2serv.SenderPrx.checkedCast(\
            self.communicator().propertyToProxy('Hello.Proxy').ice_twoway().ice_timeout(-1).ice_secure(False))
        if not twoway:
            print(args[0] + ": invalid proxy")
            return 1
        oneway = py2serv.SenderPrx.uncheckedCast(twoway.ice_oneway())
        batchOneway = py2serv.SenderPrx.uncheckedCast(twoway.ice_batchOneway())
        datagram = py2serv.SenderPrx.uncheckedCast(twoway.ice_datagram())
        batchDatagram = py2serv.SenderPrx.uncheckedCast(twoway.ice_batchDatagram())

        secure = False
        timeout = -1
        delay = 0

        menu()

        c = None
        while c != 'x':
            try:
                sys.stdout.write("==> ")
                sys.stdout.flush()
                c = sys.stdin.readline().strip()
                if c == 't':
                    twoway.sayHello(delay)
                elif c == 'o':
                    oneway.sayHello(delay)
                elif c == 'O':
                    batchOneway.sayHello(delay)
                elif c == 'd':
                    if secure:
                        print("secure datagrams are not supported")
                    else:
                        datagram.sayHello(delay)
                elif c == 'D':
                    if secure:
                        print("secure datagrams are not supported")
                    else:
                        batchDatagram.sayHello(delay)
                elif c == 'f':
                    self.communicator().flushBatchRequests()
                elif c == 'T':
                    if timeout == -1:
                        timeout = 2000
                    else:
                        timeout = -1

                    twoway = py2serv.SenderPrx.uncheckedCast(twoway.ice_timeout(timeout))
                    oneway = py2serv.SenderPrx.uncheckedCast(oneway.ice_timeout(timeout))
                    batchOneway = py2serv.SenderPrx.uncheckedCast(batchOneway.ice_timeout(timeout))

                    if timeout == -1:
                        print("timeout is now switched off")
                    else:
                        print("timeout is now set to 2000ms")
                elif c == 'P':
                    if delay == 0:
                        delay = 2500
                    else:
                        delay = 0

                    if delay == 0:
                        print("server delay is now deactivated")
                    else:
                        print("server delay is now set to 2500ms")
                elif c == 'S':
                    secure = not secure

                    twoway = py2serv.SenderPrx.uncheckedCast(twoway.ice_secure(secure))
                    oneway = py2serv.SenderPrx.uncheckedCast(oneway.ice_secure(secure))
                    batchOneway = py2serv.SenderPrx.uncheckedCast(batchOneway.ice_secure(secure))
                    datagram = py2serv.SenderPrx.uncheckedCast(datagram.ice_secure(secure))
                    batchDatagram = py2serv.SenderPrx.uncheckedCast(batchDatagram.ice_secure(secure))

                    if secure:
                        print("secure mode is now on")
                    else:
                        print("secure mode is now off")
                elif c == 's':
                    twoway.shutdown()
                elif c == 'x':
                    pass # Nothing to do
                elif c == '?':
                    menu()
                else:
                    print("unknown command `" + c + "'")
                    menu()
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
