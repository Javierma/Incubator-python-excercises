#Python excercise 2
#Author: Javier Martínez Arrieta

import re

regex_text=r"(?:(^switchport trunk allowed vlan )((?:[0-9]{1,4}\,|(?:[0-9]{1,4}$))+))"

all_vlans=list()
vlans_set=set()
common_vlans=list()
unique_vlans=list()

#Open file and read lines containing the command 'switchport allowed vlan...'
command_file=open("commands.txt",'r')
for line in command_file:
	match=re.search(regex_text,line)
	if match:
		all_vlans.append(match.group(2).split(','))
command_file.close()

#Add the VLAN to the set
for vlans_list in all_vlans:
	for vlan in vlans_list:
		vlans_set.add(vlan)

#Check if the VLAN is unique
count_times=0
for element in vlans_set:
	for vlans_list in all_vlans:
		count_times=count_times+vlans_list.count(element)
	if count_times>1:
		common_vlans.append(element)
	else:
		unique_vlans.append(element)
	count_times=0

i=0
for vlan in common_vlans:
	common_vlans[i]=int(vlan)
	i=i+1

i=0
for vlan in unique_vlans:
	unique_vlans[i]=int(vlan)
	i=i+1

common_vlans.sort()
unique_vlans.sort()

print 'Common VLANS: '+str(common_vlans)
print 'Unique VLANS: '+str(unique_vlans)

