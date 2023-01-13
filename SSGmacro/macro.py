# coding: utf-8

# v1.0
# finish time 2023-1-14 1:23

import time
import os
import pyautogui
import keyboard
# 后面两个不是标准库，运行的时候需要先用pip安装

# 运行配置
instance_number = 3     # 实例数，你是几开就填几
reset_key = 'B'         # reset热键，可以是符号，如果是字母要注意大小写
exit_delay = 0.2        # 切换实例延迟，电脑卡的就调大一点；如果你不用全屏玩游戏就设成-1

# 运行参数
reset_pressed = False
next_instance = 2


# 切换实例
def switch(next):
    pyautogui.hotkey('win', '1')
    pyautogui.hotkey('ctrl', str(next))
    pyautogui.hotkey('win', str(next+1))


# 按键检测
def key_press(key):
    global reset_pressed
    if key.name == reset_key:
        reset_pressed = True
        print('pressed')


keyboard.on_press(key_press)

# attempts文件
if os.path.exists('attempts.txt') is False:
    with open('attempts.txt', 'a') as fo_c:
        pass
    attempts_pri = 0
else:
    with open('attempts.txt', 'r', encoding='utf-8') as fo_r:
        attempts_pri = int(fo_r.readlines()[0])
print(f'attempts_pri:{attempts_pri}')

attempts = 0
times = 0   # 计时
while True:
    times += 1
    time.sleep(0.2)     # 循环暂停
    if reset_pressed is True:
        attempts += 1
        print(f'attempts:{attempts}')

        print(f'next:{next_instance}')

        # 切换延迟
        if exit_delay > 0:
            time.sleep(exit_delay)

        switch(next_instance)

        # 确定下一个实例
        if next_instance < instance_number:
            next_instance += 1
        elif next_instance == instance_number:
            next_instance = 1

        reset_pressed = False

    # 记录attempts
    if times % 300 == 0:
        attempts_total = attempts_pri + attempts
        print(f'attempts_total:{attempts_total}')
        with open('attempts.txt', 'w', encoding='utf-8') as fo_w:
            fo_w.write(str(attempts_total))
