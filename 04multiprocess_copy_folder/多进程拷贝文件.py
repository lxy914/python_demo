import os
from multiprocessing import Pool, Manager
import time


def copyFileTask(names: str, old_folder_name: str, new_folder_name: str, queue):
    """完成拷贝一个文件的说明"""
    # print(names + "---start")
    fr = open(old_folder_name + "/" + names, "rb")
    fw = open(new_folder_name + "/" + names, "wb")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(names)
    time.sleep(0.5)
    # print(names + "---end")


def main():
    # 1.创建一个文件夹
    oldFolderName = input("请输入文件夹的名称：")
    newFolderName = oldFolderName + "-[复件]"
    # print(newFolderName)
    os.mkdir(newFolderName)
    # 2.获取old文件夹中所有的文件
    fileNames = os.listdir(oldFolderName)
    # print(fileNames)
    # 3.使用多进程的方式copy原文件中所有文件到新文件中
    pool = Pool(5)
    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask, (name, oldFolderName, newFolderName, queue))
    pool.close()
    # pool.join()

    num = 0
    allnum = len(fileNames)
    while num < allnum:
        num = queue.qsize()
        copyRate = num / allnum
        print("\rcopy的进度是%.2f%%" % (copyRate * 100), end="")
    print("\n已完成拷贝！")


if __name__ == '__main__':
    main()
