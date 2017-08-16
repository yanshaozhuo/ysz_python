import random

class random_len:
    def __init__(self,length,times):
        self.length = length
        self.times = times
    def random_length(self):
        char = 'ABCDEFGHIJKLMNOPQRSTUVWXZYabcdefghijklmnopqrstuvwxyz0123456789'
        with open('随机码.txt','a+') as f:
            '''
            #第一种方式：
            for each in range(int(self.times)):
                str = ''.join(random.sample(char,int(self.length)))
                print(str)
                f.write(str)
                f.write('\n')
            '''

            #第二种方式：
            for each in range(int(self.times)):
                str = ''
                length_long = len(char) - 1
                for i in range(int(self.length)):
                    str+= char[random.randint(0,length_long)]
                print(str)
                f.write(str)
                f.write('\n')


m = input('请输入随机序列长度：')
n = input('需求数量：')
p = random_len(m,n)
p.random_length()