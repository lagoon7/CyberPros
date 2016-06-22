#!/usr/bin/python
import os
import datetime
import socket
import dpkt

f = open('2015-03-31-traffic-analysis-exercise.pcap')
pcap = dpkt.pcap.Reader(f)
# For each packet in the pcap process the contents
for timestamp, buf in pcap:

    eth = dpkt.ethernet.Ethernet(buf)
   
    ip = eth.data
    if ip.p==dpkt.ip.IP_PROTO_TCP: #Check for TCP packets
        TCP=ip.p
        #ADD TCP packets Analysis code here
        #proto = ip.p.get_proto()
        src = socket.inet_ntoa(ip.src)
        dst = socket.inet_ntoa(ip.dst)
        sourceport = str(ip.data.sport)
        destport = str(ip.data.dport)
        #print '[+] PROTO:' + socket.inet_ntoa(proto)
        print '[+] Src: ' + src + ' SrcPrt: ' + sourceport +' --> Dst: ' + dst + ' DstPrt: '+ destport
        #print '[+] Src: ' + src + ' --> Dst: ' + dst
        # Print out the timestamp in UTC
        print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))
    else:
         continue   

    
    '''
    #check whether IP packets: to consider only IP packets 
    if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
            continue
            #skip if it is not an IP packets 
    ip=eth.data
    if ip.p==dpkt.ip.IP_PROTO_TCP: #Check for TCP packets
           TCP=ip.data 
           #ADD TCP packets Analysis code here
    elif ip.p==dpkt.ip.IP_PROTO_UDP: #Check for UDP packets
           UDP=ip.data 
           #UDP packets Analysis code here

    
    
    
    
    '''