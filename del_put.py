import os,json
import socketserver

class MyTCPHander(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionResetError as e:
                print("err",e)
                break
    def put(self,*args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename + ".new","wb")
        else:
            f = open(filename , "wb")
        self.request.send(b"200 ok")
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded..." % filename)
    def ls(self,*args):
        HOME_PATH = os.listdir(os.getcwd())
        self.request.send(json.dumps(HOME_PATH).encode())
    def get(self,*args):
        cmd_split = args[0]
        cmd_list = list(cmd_split.values())
        filename = cmd_list[1]
        if os.path.isfile(filename):
            file_size = os.stat(filename).st_size
            msg_dic = {
                "filename":filename,
                "filesize":file_size
            }
            self.request.send(json.dumps(msg_dic).encode())
            client_responce = self.request.recv(1024).decode()
            print(client_responce)
            f = open(filename,'rb')
            for line in f:
                self.request.send(line)
            else:
                print('file uploaded...')
                f.close()

if __name__ == "__main__":
    IP,PORT = 'localhost',9999
    server = socketserver.ThreadingTCPServer((IP,PORT),MyTCPHander)
    server.serve_forever()