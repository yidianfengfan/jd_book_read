#�л��к���ʾ

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class HelloHD(Protocol):

    def connectionMade(self):
        self.transport.write("Hello This is HD's Test protocol\r\n") 
        self.transport.loseConnection()


# �������ʩչTwisted����Ĵ�����
factory = Factory()
factory.protocol = HelloHD

# ����������8025�˿ڣ������һ������1024�Ķ˿�
reactor.listenTCP(8025, factory)
reactor.run()
