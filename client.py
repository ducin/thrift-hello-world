#!/usr/bin/python

import sys
sys.path.append('./gen-py')

from hello import HelloService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 12345)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloService.Client(protocol)
    transport.open()
    print client.hello("pyWaw")
    transport.close()
except Thrift.TException, tx:
    print "%s" % (tx.message)
