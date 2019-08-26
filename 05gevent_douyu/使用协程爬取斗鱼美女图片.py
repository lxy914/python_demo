# @Time : 2019/8/26 16:49 

# @Author : 柳欣雨

# @File : 使用协程爬取斗鱼美女图片.py

# @Software: PyCharm
import gevent
import json
from urllib import request
from gevent import monkey

# 使用gevent打补丁，耗时操作自动替换成gevent提供的模块
monkey.patch_all()
# 图片存放的目录
ROOT = "./images/"
# 设置请求头，防止被反爬虫的第一步
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 "
}


def download(img_src):
    # 把每个链接最后的/dy1去掉
    img_src: str = img_src.replace("/dy1", "")
    # 提取图片名
    file_name: str = img_src.split("/")[-1]
    response = request.urlopen(request.Request(img_src, headers=header))
    # 保存到本地
    with open(ROOT + file_name, "wb") as f:
        f.write(response.read())
    print(file_name, "下载完成！")


if __name__ == '__main__':

    req = request.Request("https://www.douyu.com/gapi/rknc/directory/yzRec/1", headers=header)
    # 把json数据转换成python中的字典
    json_obj = json.loads(request.urlopen(req).read().decode("utf-8"))
    tasks = []
    for src in json_obj["data"]["rl"]:
        tasks.append(gevent.spawn(download, src["rs16"]))
    # 开始下载图片
    gevent.joinall(tasks)
