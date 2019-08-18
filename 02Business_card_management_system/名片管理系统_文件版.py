cards = []  # 定义一个的列表用于存放名片信息


def print_menu():
    """"完成打印功能菜单"""
    print("=" * 20)
    print("    名片管理系统")
    print(" 1:添加一个名片")
    print(" 2:删除一个名片")
    print(" 3:修改一个名片")
    print(" 4:查询一个名片")
    print(" 5:显示所有的名片")
    print(" 6:退出")
    print("=" * 20)


def add_card():
    """"完成添加一个名片的功能"""
    new_infor: dict = {"name": input("请输入一个名字："), "phone": input("请输入一个电话："), "address": input("请输入一个地址：")}

    cards.append(new_infor)
    print("添加成功！")


def delete_card():
    del_name = input("请输入要删除的名字：")
    for person in cards:
        if del_name == person["name"]:
            cards.remove(person)
            print("删除成功！")
            break
    else:
        print("找不到要删除的人！")


def update_card():
    name: str = input("请输入要修改的名字（只能通过名字来修改电话和住址）：")
    for person in cards:
        if name == person["name"]:
            phone = input("请输入新的的电话（直接回车则不修改）：")
            address = input("请输入新的的地址（直接回车则不修改）：")
            if phone:
                person["phone"] = phone
            if address:
                person["address"] = address
            print("修改成功")
            break
    else:
        print("找不到要修改的人！")


def find_card():
    """用来查询一个名片"""

    find_name: str = input("请输入要查询的名字（支持模糊查询）：")
    flag: int = 1
    for temp in cards:
        # 遍历名片中的所有名字，判断要查找的名字是否存在，不存在则打印查无此人
        if temp["name"].find(find_name) != -1:
            print("%s\t%s\t%s" % (temp["name"], temp["phone"], temp["address"]))
            flag = 0
    if flag:
        print("查无此人")


def show_all():
    print("姓名\t电话\t住址")
    for temp in cards:
        print("%s\t%s\t%s" % (temp["name"], temp["phone"], temp["address"]))


def save_file():
    """把已经添加的信息保存到文件中"""
    with open("back.data", "w", encoding="utf-8") as f:
        f.write(str(cards))


def load_file():
    global cards
    # 第一次打开时文件不存在会报异常
    try:
        with open("back.data", encoding="utf-8") as f:
            cards = eval(f.read())
            f.close()
    except FileNotFoundError:
        pass


def main():
    """"完成对整个程序的控制"""
    # 打印功能提示
    print_menu()
    # 加载文件信息
    load_file()
    while True:
        # 获取用户的选择
        num: str = input("请输入功能序号：")
        # 判断输入的是否为数字
        if not num.isdigit():
            print("请输入数字！")
            continue
        # 转换成数字类型
        num: int = int(num)
        # 增
        if num == 1:
            add_card()
            save_file()
        # 删
        elif num == 2:
            delete_card()
            save_file()
        # 改
        elif num == 3:
            update_card()
            save_file()
        # 查
        elif num == 4:
            find_card()
        elif num == 5:
            show_all()
        elif num == 6:
            break
        else:
            print("请按号输入！")
        print()


# 调用主函数
if __name__ == '__main__':
    main()
