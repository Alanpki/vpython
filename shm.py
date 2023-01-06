"""
 VPython教學: 簡諧運動
 Ver. 1: 2022/11/10
 作者: 徐子期
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
m = 12               # 木塊質量 12 kg
size = 0.5            # 木塊邊長 0.5 m
R = 0.5               # 振幅 0.5 m
k = 3               # 彈性常數 3 N/m
L0 = R + size       # 彈簧原長
i = 0               # 木塊回到初位置的次數
t = 0               # 時間
dt = 0.002          # 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗、地板、木塊、彈簧
scene = canvas(title="Simple Harmonic Motion", width=800, height=400, x=0, y=0, background=vec(0, 0.6, 0.6)) #運動的視窗大小
floor = box(pos=vec(0, -(size+0.1)/2, 0), size=vec(2*L0, 0.1, R), texture=textures.metal) #地板的大小 pos中心為原點 texture材質 金屬
wall = box(pos=vec(-L0, 0, 0), size=vec(0.1, size, R), texture=textures.metal) #牆壁的位子
block = box(pos=vec(R+size/2, 0, 0), size=vec(size, size, size), texture=textures.wood, v=vec(0, 0, 0)) #方塊的大小
spring = helix(pos=vec(-L0, 0, 0), radius=0.3*size, thickness=0.05*size, color=color.yellow) #彈簧的設定 radius彈簧半徑 thickness彈簧線寬
spring.axis = block.pos - spring.pos - vec(size/2, 0, 0) #axis 從pos延伸彈簧的方向 = 方塊減彈簧
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=block.pos + vec(0, size, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.green) #表示速度的箭頭 綠色
arrow_a = arrow(pos=block.pos + vec(0, 2*size, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.magenta) #表示加速度的箭頭 洋紅色
# 繪圖部分
gd = graph(title="plot", width=600, height=450, x=0, y=400, xtitle="<i>t</i>(s)", 
           ytitle="blue: <i>x</i>(m), green: <i>v</i>(m/s), magenta: <i>a</i>(m/s<sup>2</sup>)") 
xt = gcurve(graph=gd, color=color.blue) #gcurve曲線
vt = gcurve(graph=gd, color=color.green)
at = gcurve(graph=gd, color=color.magenta)

"""
 3. 物體運動部分, 重覆3個週期
"""
while(i < 3):
    rate(1000)
# 計算彈簧長度、伸長量、回復力
    spring.axis = block.pos - spring.pos - vec(0.5*size, 0, 0)
    F = -k * (spring.axis - vec(L0, 0, 0))
# 計算木塊加速度, 更新速度、位置
    block.a = F/m
    block.v += block.a*dt
    block.pos += block.v*dt
# 更新代表速度、加速度的箭頭位置、方向、長度
    arrow_v.pos = block.pos + vec(0, size, 0)
    arrow_a.pos = block.pos + vec(0, 2*size, 0)
    arrow_v.axis = block.v
    arrow_a.axis = block.a
# 畫出 x-t, v-t, a-t 圖
    xt.plot(pos=(t, block.pos.x - size/2)) #gcurve 增加數據
    vt.plot(pos=(t, block.v.x))
    at.plot(pos=(t, block.a.x))
# 判斷木塊是否回到出發點, 計算回到出發點的次數
    if(block.pos.x > R + size/2 and block.v.x > 0):
        print(i, t)
        i += 1
# 更新時間
    t += dt