# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/13 下午8:37

import turtle

# 创建画笔
p = turtle.Pen()
# 设置画笔颜色为红色
p.pencolor('red')
# 三角形边长为200
width = 200
# 开始绘画
for i in range(3):
    # 画边长
    p.forward(width)
    # 向左偏转120度
    p.left(120)
# 结束绘画
turtle.done()



