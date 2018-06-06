import os,json
from conf import settings
from core import progress_bar

def client_put(self,*args):
    """
    用于处理客户端上传功能
    """
    cmd_split = args[0].split()
    if len(cmd_split) > 1:
        filename = cmd_split[1]
        if os.path.isfile(filename):
            file_size = os.stat(filename).st_size
            msg_dic = {
                "action":"put",
                "filename":filename,
                "size":file_size,
                "overridden":True
            }
            self.client.send(json.dumps(msg_dic).encode())
            server_responce = json.loads(self.client.recv(1024).decode())
            print(server_responce)
            if server_responce == settings.LOGIN_STATE["file_no_exit"] or \
                server_responce == settings.LOGIN_STATE["dir_no_eixt"]:
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                    send_size = f.tell()
                    progress_bar.progredd_bar(self,send_size,file_size)
                else:
                    print("file upload success")
                    f.close()
            elif server_responce == settings.LOGIN_STATE["size_empty"]:
                print("server_responce:磁盘空间不足")
        else:
            print(filename,"is not exist")
