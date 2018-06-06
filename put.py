import os,json
import socket

class TCPClient(object):
    def __init__(self):
        self.client = socket.socket()
    def connect(self,ip,port):
        self.client.connect((ip,port))
    def help(self):
        msg = 'ls dir cd '
        print(msg)

    def interactive(self):
        while True:
            cmd = input('>>:').strip()
            if len(cmd) == 0:
                continue
            cmd_order = cmd.split()[0]
            if hasattr(self,'cmd_%s' % cmd_order):
                func = getattr(self,'cmd_%s' % cmd_order)
                func(cmd)
            else:
                self.help()
    def cmd_put(self,*args):
        cmd_split =  args[0].split()
        if len(cmd_split) >1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename":filename,
                    "size": filesize,
                    "overridden":True
                }
                self.client.send( json.dumps(msg_dic).encode("utf-8")  )
                print("send",json.dumps(msg_dic).encode("utf-8") )
                server_response = self.client.recv(1024)
                f = open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success...")
                    f.close()
            else:
                print(filename,"is not exist")

    def cmd_ls(self,*args):
        cmd_split = args[0].split()
        if cmd_split[0] == 'ls':
            msg_dic = {
                "action":"ls"
            }
            self.client.send(json.dumps(msg_dic).encode())
            server_responce = self.client.recv(1024).decode()
            print(server_responce)

    def cmd_get(self,*args):
        cmd_split = args[0].split()
        if cmd_split[0] == 'get':
            filename = cmd_split[1]
            msg = {
                "action":"get",
                "filename":filename
            }
            self.client.send(json.dumps(msg).encode())
            server_responce = self.client.recv(1024).decode()
            print(server_responce)
            server_dic = json.loads(server_responce)
            server_lis = list(server_dic.values())
            filesize = server_lis[1]
            self.client.send(b'200 ok')
            if os.path.isfile(filename):
                f = open(filename + '.new','wb')
            else:
                f = open(filename,'wb')
            responce_size = 0
            while responce_size < filesize:
                data = self.client.recv(1024)
                f.write(data)
                responce_size += len(data)
            else:
                print('file has received...')

ftp = TCPClient()
ftp.connect('localhost',9999)
ftp.interactive()



