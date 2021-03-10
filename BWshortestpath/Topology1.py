# -*- coding:utf-8 -*-
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink

if '__main__' == __name__:
	# 宣告 Mininet 使用的 Controller 種類
    net = Mininet(controller=RemoteController)
	
	# 指定 Controller 的 IP 及 Port，進行初始化
    c0 = net.addController('c0',ip='127.0.0.1', port=6633)
	
	# 加入 Switch
    s1 = net.addSwitch('s1')
	
	# 加入主機，並指定 MAC
    h1 = net.addHost('h1', mac='00:00:00:00:00:01',ip='10.0.0.1')
    h2 = net.addHost('h2', mac='00:00:00:00:00:02',ip='10.0.0.2')
    h3 = net.addHost('h3', mac='00:00:00:00:00:03',ip='10.0.0.3')
	
	# 建立連線
    #net.addLink(s1, h1, port1=1, port2=1,cls=TCLink,bw=0.8)
    net.addLink(s1, h1, port1=1, port2=1, cls=TCLink, bw=40)
    #net.addLink(s1, h2, port1=2, port2=1)
    net.addLink(s1, h2, port1=2, port2=1, cls=TCLink, bw=10)
    net.addLink(s1, h3, port1=3, port2=1, cls=TCLink, bw=40)

    # 建立 Mininet
    net.build()
	
	# 啟動 Controller
    c0.start()
	
    # 啟動 Switch，並指定連結的 Controller 為 c0
    s1.start([c0])

	# 執行互動介面(mininet>...)
    CLI(net)
	# 互動介面停止後，則結束 Mininet
    net.stop()
