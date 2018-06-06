import os,json
from core import get_dirsize
from conf import settings

def server_deal_put(self,*args):
    cmd_dic = args[0]
    filename = args["filename"]
    file_size = args["size"]
    f