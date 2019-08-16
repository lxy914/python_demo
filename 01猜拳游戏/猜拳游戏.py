# @Time : 2019/8/2 21:26 

# @Author : 柳欣雨

# @File : 猜拳游戏.py 

# @Software: PyCharm
import random

# 从键盘获取用户的输入
person = input('请输入：石头(0)、剪刀(1)、布(2)：')
# input 返回的是一个字符串类型，randint(0, 2)返回的是int类型，需要把person强制转换成int类型，类型一致才可以比较
person = int(person)
computer = random.randint(0, 2)

# 为了更友好的显示信息
if person == 0:
    print('玩家：石头')
elif person == 1:
    print('玩家：剪刀')
else:
    print('玩家：布')
if computer == 0:
    print('电脑：石头')
elif computer == 1:
    print('电脑：剪刀')
else:
    print('电脑：布')

# 如果出拳一样就是平局
if person == computer:
    print('你好厉害呀！居然和我打成平局！')

# 玩家：石头 电脑：剪刀
# 玩家：剪刀 电脑：布
# 玩家：布 电脑：石头   这三种情况下玩家赢

elif person == 0 and computer == 1 or person == 1 and computer == 2 or person == 2 and computer == 0:
    print('恭喜你，你赢了！')
# 其他情况都是玩家输
else:
    print('真遗憾，你输了！')
