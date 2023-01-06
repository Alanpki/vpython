from vpython import *
import time

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.25 #球的大小
g = 9.8 #重力加速度的值
ball_1st_pos = vec(-15,5,0) #球的初始位置
ball_1st_v = vec(6,8,0) #球的速度
t = 0
path = 9

"""
 2. 畫面設定
"""
scene = canvas(title="FreeFall",width = 800,height = 600,center = vec(0,ball_1st_pos.y,0),background =vec(1,1,0.6))#運動的視窗大小
ball = sphere(radius = size, color = color.red, make_trail = True, trail_radius = 0.05) #球 大小是size make_trail讓行經的軌跡會留下痕跡
arr = arrow(color = color.blue,round=True, shaftwidth = 0.25) #箭頭一邊是直的盒形軸，另一邊有一個箭頭。 round讓箭頭的橫截面為圓形

ball.pos = ball_1st_pos #將設定的位子跟速度 指向球
ball.v = ball_1st_v
arr.pos = ball.pos #將設定的位子跟速度 指向箭頭
arr.axis = ball.v

dt = 0.001 #單位時間 越小模擬的越精準

"""
 3. 物體運動部分
"""
while ball.pos.y >= size : #碰到地板但不超過地板 球在y座標的位子要大於球的半徑
    rate(1000)

    ball.pos += ball.v*dt #球的位子=原本的位子加上速度*時間
    path += (ball.v.x**2 + ball.v.y**2 + ball.v.z**2)**0.5*dt #經過的路徑長
    ball.v.y -= g*dt #球的速度 -向下的加速度*時間
    arr.pos = ball.pos #箭頭的位子貼著球的位子
    arr.axis = (ball.v)/3 #箭頭的速度是球的速度除以三
    t += dt

displ = ((ball.pos.x - ball_1st_pos.x)**2 + (ball.pos.y - ball_1st_pos.y)**2 + (ball.pos.z - ball_1st_pos.z)**2)**0.5 #可算到球的位子
print(type(displ))
msg = text(text = 'Displacement = ' + str((round(displ,2))) + ' m' , pos = vec(-12,ball_1st_pos.y+4, 0), color = color.black) #位移
msg2 = text(text = 'Flying time = ' + str((round(t,2))) + ' sec' , pos = vec(-12, ball_1st_pos.y+2, 0), color = color.black) #經過的時間
msg3 = text(text = 'Path Length = ' + str((round(path,2))) + ' m', pos = vec(-12,ball_1st_pos.y, 0),color = color.black) #路徑長