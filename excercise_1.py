#Python excercise 1

import re


def convert_binary_to_int(octect):
	net_addr_octect=int(octect[0])*128+int(octect[1])*64+int(octect[2])*32+int(octect[3])*16+int(octect[4])*8+int(octect[5])*4+int(octect[6])*2+int(octect[7])*1
	return net_addr_octect

regex_ip_addr = r"^(?:(?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])\.){3}(?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])$))"
regex_netmask = r"^(?:(?:\/(?:[1-2][0-9]|3[0-2]|[8-9])))$"

repeat_question=True

while repeat_question:
	ip_addr=raw_input ('Enter IP address: ')
	matches = re.search(regex_ip_addr, ip_addr)
	if matches:

		octects=ip_addr.split('.')
		print '    '+'\t\t    '.join(octects)
		bin_octects=list()
		for octect in octects:
			bin_octects.append(format(int(octect),'08b'))
		print '\t'.join(bin_octects)
		repeat_question=False

repeat_question=True
while repeat_question:
	netmask=raw_input ('Enter the subnet mask in decimal format (i.e. /24):')
	matches = re.search(regex_netmask, netmask)
	if matches:
		netmask=int(netmask.split('/')[1])
		netmask_bin=list()
		repeat_question=False

#Convert netmask to binary format
ones_groups=netmask/8
ones_bits=netmask%8
i=0
#For groups where all are ones just write 255 in binary
while i < ones_groups:
	netmask_bin.append(format(255,'08b'))
	i=i+1
i=0
j=7
num=0

#Get the binary number of the group where octect is not 0 or 255
while i < ones_bits:
	num=num+pow(2,j)
	i=i+1
	j=j-1
netmask_bin.append(format(num,'08b'))
ones_groups=ones_groups+1

#For groups where all are zeros just write 0 in binary
while ones_groups<4:
	netmask_bin.append(format(0,'08b'))
	ones_groups=ones_groups+1


#Get network address
net_addr=list()
net_addr_octect=str()
broadcast_address=list()
broadcast_address_octect=str()
i=0
group=0
while group < 4:
	while i < 8:
		if(netmask_bin[group][i]=='1'):
			net_addr_octect=net_addr_octect+bin_octects[group][i]
			broadcast_address_octect=broadcast_address_octect+bin_octects[group][i]
		else:
			net_addr_octect=net_addr_octect+'0'	
			broadcast_address_octect=broadcast_address_octect+'1'
		i=i+1
	net_addr.append(net_addr_octect)
	broadcast_address.append(broadcast_address_octect)
	group=group+1
	net_addr_octect=str()
	broadcast_address_octect=str()
	i=0


print 'Network address is '+str(convert_binary_to_int(net_addr[0]))+'.'+str(convert_binary_to_int(net_addr[1]))+'.'+str(convert_binary_to_int(net_addr[2]))+'.'+str(convert_binary_to_int(net_addr[3]))+'/'+str(netmask)
print 'Broadcast address is '+ str(convert_binary_to_int(broadcast_address[0]))+'.'+str(convert_binary_to_int(broadcast_address[1]))+'.'+str(convert_binary_to_int(broadcast_address[2]))+'.'+str(convert_binary_to_int(broadcast_address[3]))+'/'+str(netmask)
