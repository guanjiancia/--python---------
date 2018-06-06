import sys

def progredd_bar(self,num,total):
    """
    进度条：用于显示上传和下载的进度

    """
    rate = num/total
    rate_num = int(rate * 100)
    r = "\r%s%d%%" % ("|" * rate_num,rate_num)   #/r表示重新回到当前行输出
    sys.stdout.write(r)   #输出没有换行符
    sys.stdout.flush()    #清空缓存