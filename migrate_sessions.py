'''

Mobaxterm to securecrt script
Only works with SSH connections at the moment

Instructions:
	1.Export sessions from mobaxterm
	2.Change name to sessions.txt
	3.Put file on same folder as this script
	4.Execute script
	5.Run guide on this page: https://www.vandyke.com/support/tips/importsessions.html to add the result.txt file sessions to secure crt


'''


import pprint

with open('sessions.txt', 'r') as f:
	#split file in blocks
	document = f.read().split('\r\n\r\n')

result = []
result.append('hostname,protocol,username,folder,emulation,session_name\n')




for folder in document:

	temp_result = []

	sessions = folder.splitlines()

	folder_name = sessions[1][7:].replace('\\','/')


	sessions_clean = sessions[3:]

	for session in sessions_clean:
		if session.find('=#109#0%') != -1:
			temp_result = []
			temp_result.append(folder_name)

			first_split = session.split('=#109#0%')
			
			temp_result.append(first_split[0])
			second_split = first_split[1].split('%22%')
			temp_result.append(second_split[0])


			i = [temp_result[2],'SSH2','ttscha',folder_name[12:],'XTerm',temp_result[1]]



			temp = ",".join(i)
			result.append(temp)


		if session.find('= #109#0%') != -1:
			temp_result = []
			temp_result.append(folder_name)

			first_split = session.split('= #109#0%')
			
			temp_result.append(first_split[0])
			second_split = first_split[1].split('%22%')
			temp_result.append(second_split[0])


			i = [temp_result[2],'SSH2','ttscha',folder_name[12:],'XTerm',temp_result[1]]



			temp = ",".join(i)
			result.append(temp)
			


with open('result2.txt','w') as d:
	for i in result:
		d.write(i)
		d.write('\n')
