from smb.SMBConnection import SMBConnection

userid = 'zesst'
password= 'drevnochtets'
client_machine_name = 'haha'
remote_machine_name = 'diskstation'
server_ip = '192.168.1.102'

conn = SMBConnection(userid, password, client_machine_name, remote_machine_name, use_ntlm_v2 = True)
conn.connect(server_ip, 139)
filelist = conn.listPath('Video', '/')

for file in filelist:
	print(file.filename)

