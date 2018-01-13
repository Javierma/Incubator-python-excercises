import re

regex_route=r"(^((?:[HRSBUoMPDEO\*])|(?:O\sE[12])|(?:i\sL\d))(?:\s)((?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])\.){3}(?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])))(?:\s\s\[)(\d+\/\d+)(?:\]\svia\s)((?:(?:\b2[0-5]{2}|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])\.){3}(?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])))\s,\s(\d{1,2}:\d\d:\d\d),\s(\w+$)|((C|L|S\*)(?:\s)((?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])\.){3}(?:(?:\b2[0-5]{2}|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])))(\s\s)((?:(?:\b25[0-5]|\b2[0-4][0-9]|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])\.){3}(?:(?:\b2[0-5]{2}|\b1[0-9]{2}|\b[0-9]{2}|\b[0-9])))(?:\s\sis directly connected,\s)(\w+$)))"

codes={'R':'RIP derived','O':'OSPF derived','C':'connected','L':'Local','S':'static','H':'NHRP','B':'BGP derived','*':'candidate default route','IA':'OSPF inter area route','i':'IS-IS derived','i ia':'IS-IS','U':'per-user static route','o':'on-demand routing','M':'mobile','P':'periodic downloaded static route','D':'EIGRP','EX':'EIGRP external','O E1':'OSPF external type 1 route','O E2':'OSPF external type 2 route','O N1':'OSPF NSSA external type 1 route','O N2':'OSPF NSSA external type 2 route','E':'EGP','i su':'IS-IS summary', 'i L1':'IS-IS level-1','i L2':'IS-IS level-2'}

ip_routes_file=open("ShowIpRoute.txt",'r')
for line in ip_routes_file:
	match=re.search(regex_route,line)
	#Check if route is dynamic
	if match and match.group(2) in codes:
		print '---------------------------------'
		print 'Protocol: ' + str(codes[match.group(2)])
		print 'Prefix: ' + str(match.group(3))
		print 'AD/Metric: ' + str(match.group(4))
		print 'Next hop: '+ str(match.group(5))
		print 'Last update: ' + str(match.group(6))
		print 'Outbound interface: ' + str(match.group(7))	
		print '---------------------------------'

	#Route is static, so the output format varies
	elif match and match.group(9) in codes:
		print '---------------------------------'
		print 'Protocol: None (directly connected)'
		print 'Prefix: ' + str(match.group(10))
		print 'AD/Metric: '
		print 'Next hop: '
		print 'Last update: '
		print 'Outbound interface: ' + str(match.group(13))	
		print '---------------------------------'

ip_routes_file.close()