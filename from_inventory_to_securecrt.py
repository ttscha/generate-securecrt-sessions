import pprint

'''

Sessions will come in the format

location,purpose,hostname,ip
'Waterloo,Distribution,dist02.mdf.wt01,172.19.236.30,6/28/2021,,,,,'

transform in securecrt format

hostname,protocol,folder,emulation,session_name
10.10.10.10,SSH2,Waterloo\core,XTerm,10.125.207.154:6543

'''

with open('temporary/from_inventory.csv') as f:
	inventory_old = f.read().splitlines()



result = []
result.append('hostname,protocol,folder,emulation,session_name\n')

for device in inventory_old:

	device_list = device.split(',')

	result.append(f'{device_list[3]},SSH2,{device_list[0]}\\{device_list[1]},XTerm,{device_list[2]} - {device_list[3]}\n')

pprint.pprint(result)

with open('temporary/result.txt', 'w') as f:
	for i in result:
		f.write(i)

