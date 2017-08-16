#coding:utf-8

import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

#Image         负责处理图片
#ImageDraw     负责处理画笔
#ImageFont     负责处理字体
#ImageFilter   负责处理滤镜

#项目思路：
    #1、定义一张图片
img = Image.new('RGB',(150,50),(255,255,255))
'''
第一个参数：代表采用RGB颜色模式
第二个参数：代表图片尺寸
第三个参数：具体的图片颜色

'''
    #2、创建画笔
draw = ImageDraw.Draw(img)
    #3、绘制线条和点
        #绘制线
for i in range(random.randint(1,10)):
    draw.line(
        #在绘制线条是有个特色：每条线两个点，每个点考x，y两个值来确定位置
        [(random.randint(1,150),random.randint(1,150)),
         (random.randint(1,150),random.randint(1,150))],fill = (0,0,0))
        #绘制点
for i in range(1000):
    draw.point([random.randint(1,150),random.randint(1,150)],fill = (0,0,0,))

    #4、绘制我们的文字
        #文字是随机产生的
        #文字的个数是一定的
            #定义要生成随机数的字母和数字
font_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
c_chars = ''.join(random.sample(font_list,5))
#random.sample 是在指定列表中随机选取指定个数元素
        #绘制字体
            #需要先进行字体定制
font = ImageFont.truetype('simhei.ttf',30)
draw.text((5,5),c_chars,font = font,fill = 'RED')
'''
第一个参数：代表文字位置，距离上和左的距离
第二个参数：代表文字的内容
第三个参数：代表字体
第四个参数：代表字体颜色
'''
    #5、定义扭曲的参数
params = [1-float(random.randint(1,2))/100,0,0,0,1-float(random.randint(1,2))/100,float(random.randint(1,2))/500,0.001,float(random.randint(1,1))/500]
    #6、使用滤镜
        #添加滤镜
img = img.transform((150,50),Image.PERSPECTIVE,params)
'''
第一个参数：扭曲的范围
第二个参数：扭曲的样式
第三个参数：扭曲的参数
'''
        #进行扭曲
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

img.show()