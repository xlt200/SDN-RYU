from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo(Topo):
    def __init__(self):

        Topo.__init__(self)

        nhost = 4
        nswitch = 8
        host = [None];
        switch = [None];


        for i in range(nhost):
            NewHost = self.addHost("h{}".format(i+1))
            host.append(NewHost)

        for i in range(nswitch):
            NewSwitch = self.addSwitch("s{}".format(i+1))
            switch.append(NewSwitch)

        server = self.addHost("server",ip="10.0.0.5")

        # add server
        self.addLink(server,switch[1],port1=1,port2=1)
        
        # host to switch
        self.addLink(host[1],switch[4],port1=1,port2=4,cls=TCLink)
        self.addLink(host[2],switch[8],port1=1,port2=2,cls=TCLink)
        self.addLink(host[3],switch[8],port1=1,port2=3,cls=TCLink)
        self.addLink(host[4],switch[6],port1=1,port2=4,cls=TCLink)

        
        # switch to switch
        self.addLink(switch[1],switch[2],port1=2,port2=1,cls=TCLink,delay="10ms")
        self.addLink(switch[1],switch[3],port1=4,port2=1,cls=TCLink,delay="10ms")
        self.addLink(switch[1],switch[5],port1=3,port2=2,cls=TCLink,delay="20ms")
        self.addLink(switch[2],switch[4],port1=2,port2=1,cls=TCLink,delay="10ms")
        self.addLink(switch[2],switch[5],port1=3,port2=1,cls=TCLink,delay="20ms")
        self.addLink(switch[5],switch[3],port1=3,port2=2,cls=TCLink,delay="15ms")
        self.addLink(switch[5],switch[4],port1=4,port2=2,cls=TCLink,delay="20ms")
        self.addLink(switch[5],switch[6],port1=6,port2=2,cls=TCLink,delay="15ms")
        self.addLink(switch[5],switch[7],port1=5,port2=2,cls=TCLink,delay="20ms")
        self.addLink(switch[3],switch[6],port1=3,port2=1,cls=TCLink,delay="10ms")
        self.addLink(switch[6],switch[7],port1=3,port2=3,cls=TCLink,delay="10ms")
        self.addLink(switch[4],switch[7],port1=3,port2=1,cls=TCLink,delay="10ms")
        self.addLink(switch[7],switch[8],port1=4,port2=1,cls=TCLink,delay="0ms")
        #self.addLink(switch[1],switch[2],port1=2,port2=1)

topos = {'mytopo':(lambda:MyTopo())}
