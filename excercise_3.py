# -*- coding: utf-8 -*-
#Python excercise 3
#Author: Javier Martínez Arrieta

import re

regex_dynamic_route=r"(^((?:[HRBUoMPDEO\*])|(?:O\sE[12])|(?:i\sL\d))(?:\s+)((?:((?:\d|\.|\/)+))(?:\s+\[)(\d+\/\d+)(?:\]\svia\s)((?:\d|\.|\/)+))\s{0,},\s(\d{1,2}:\d\d:\d\d),\s((?:\w+(?:\/|$))+))"

regex_static_or_connected=r"(^(?:[CLS])\*{0,1})(?:\s+)((?:\d|\.|\/)+)(?:\s+)(?:(?:(?:is directly connected,\s+)((?:\w+(?:\/|$))+))|((?:\[)(\d+\/\d+)(?:\])(?:\s+via\s+)((?:\d|\.|\/)+)|(((?:\d|\.)+)(?:\s+is directly connected,\s+)((?:\w+(?:\/|$))+))))"


codes={'R':'RIP derived','O':'OSPF derived','C':'connected','L':'Local','S':'static','S*':'default static route','H':'NHRP','B':'BGP derived','*':'candidate default route','IA':'OSPF inter area route','i':'IS-IS derived','i ia':'IS-IS','U':'per-user static route','o':'on-demand routing','M':'mobile','P':'periodic downloaded static route','D':'EIGRP','EX':'EIGRP external','O E1':'OSPF external type 1 route','O E2':'OSPF external type 2 route','O N1':'OSPF NSSA external type 1 route','O N2':'OSPF NSSA external type 2 route','E':'EGP','i su':'IS-IS summary','i L1':'IS-IS level-1','i L2':'IS-IS level-2','*':'candidate default','U':'per-user static route','o':'ODR','P':'periodic downloaded static route','H':'NHRP','l':'LISP','a':'application route','+':'replicated route','%':'next hop override'}

ip_routes_file=open("ShowIpRoute.txt",'r')
for line in ip_routes_file:
	match=re.search(regex_dynamic_route,line)
	#Check if route is dynamic
	if match and match.group(2) in codes:
		print '---------------------------------'
		print 'Protocol: ' + str(codes[match.group(2)])
		print 'Prefix: ' + str(match.group(4))
		print 'AD/Metric: ' + str(match.group(5))
		print 'Next hop: '+ str(match.group(6))
		print 'Last update: ' + str(match.group(7))
		print 'Outbound interface: ' + str(match.group(8))	
		print '---------------------------------'
	
	#Route not dynamically learned, so the output format varies
	else:
		match=re.search(regex_static_or_connected,line)
		if match and match.group(1) in codes:
			if match.group(1) == 'C':
				print '---------------------------------'
				print 'Protocol: None ('+str(codes[match.group(1)])+')'
				print 'Prefix: ' + str(match.group(2))
				print 'AD/Metric: '
				print 'Next hop: '
				print 'Last update: '
				print 'Outbound interface: ' + str(match.group(9))	
				print '---------------------------------'
		
			elif match.group(1) == 'L':
				print '---------------------------------'
				print 'Protocol: None ('+str(codes[match.group(1)])+')'
				print 'Prefix: ' + str(match.group(2))
				print 'AD/Metric: '
				print 'Next hop: '
				print 'Last update: '
				print 'Outbound interface: ' + str(match.group(3))	
				print '---------------------------------'			
	
			elif match.group(1).startswith('S'):
				if '[' in line:
					print '---------------------------------'
					print 'Protocol: None ('+str(codes[match.group(1)])+')'
					print 'Prefix: ' + str(match.group(2))
					print 'AD/Metric: ' + str(match.group(5))
					print 'Next hop: ' + str(match.group(6))
					print 'Last update: ' 
					print 'Outbound interface: '	
					print '---------------------------------'		
	
				else:
					print '---------------------------------'
					print 'Protocol: None ('+str(codes[match.group(1)])+')'
					print 'Prefix: ' + str(match.group(2))
					print 'AD/Metric: '
					print 'Next hop: '
					print 'Last update: '
					print 'Outbound interface: ' + str(match.group(3))	
					print '---------------------------------'
	

ip_routes_file.close()
