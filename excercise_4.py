access_template = ['switchport mode access', 'switchport access vlan {}', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan {}']

repeat_question=True
while repeat_question:
	interface_mode=raw_input('Enter interface mode (access/trunk): ')
	if interface_mode == 'access' or interface_mode == 'trunk':
		repeat_question=False

repeat_question=True
while repeat_question:
	interface_type_number=raw_input('Enter interface type and number: ')
	if interface_type_number[0] is 'f' or interface_type_number[0] is 'F' or interface_type_number[0] is 'g' or interface_type_number[0] is 'G' or interface_type_number[0] is 's' or interface_type_number[0] is 'S':
		repeat_question=False

repeat_question=True
while repeat_question:
	if interface_mode == 'access':
		vlan=raw_input('Enter VLAN number: ')

	else:
		vlan=raw_input('Enter allowed VLANs: ')	
	
	if int(vlan) >=0 and int(vlan) <=4094:
		repeat_question=False
		

print '\ninterface ' + interface_type_number
if interface_mode == 'access':
	print access_template[0]
	print access_template[1].format(vlan)
	print access_template[2]
	print access_template[3]
	print access_template[4]

else:
	print trunk_template[0]
	print trunk_template[1]
	print trunk_template[2].format(vlan)

