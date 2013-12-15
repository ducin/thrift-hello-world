#!/usr/bin/python

import sys
sys.path.append('./gen-py')

from hello import HelloService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloHandler:

    def hello(self, name):
        print "hello called for %s" % (name)
        return "Hello, %s!" % (name)

handler = HelloHandler()
processor = HelloService.Processor(handler)
transport = TSocket.TServerSocket(port=12345)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'