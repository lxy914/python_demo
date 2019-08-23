# @Time : 2019/8/19 15:51 

# @Author : 柳欣雨

# @File : 数字时钟.py 

# @Software: PyCharm
import time


class Clock:

    def __init__(self):
        # 获取当前系统时间
        t = time.localtime()
        self._hour = t.tm_hour
        self._minute = t.tm_min
        self._second = t.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return "%02d:%02d:%02d" % (self._hour, self._minute, self._second)


def main():
    clock = Clock()
    while True:
        # 将光标退到当前行首
        print("\r%s" % clock.show(), end="")
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
