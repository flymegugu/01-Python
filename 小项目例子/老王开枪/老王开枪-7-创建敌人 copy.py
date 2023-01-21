class Person(object):
    '''人类'''

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None
        self.hp = 100

    def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self, gun_temp, dan_jia_temp):
        gun_temp.baocun_danjia(dan_jia_temp)

    def naqiang(self, gun_temp):
        self.gun = gun_temp

    def __str__(self) -> str:
        if self.gun:
            return "%s的血量为：%d,他有枪,%s" % (self.name, self.hp, self.gun)
        else:
            return "%s的血量为：%d,他没有枪" % (self.name, self.hp)


class Gun(object):
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        self.danjia = None

    def baocun_danjia(self, dan_jia_temp):
        self.danjia = dan_jia_temp

    def __str__(self) -> str:
        if self.danjia:
            return "枪的信息%s,%s" % (self.name, self.danjia)
        else:
            return "枪的信息%s,枪里面没有子弹" % (self.name)


class Danjia(object):
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num
        self.zidan_list = []

    def baocun_zidan(self, zi_dan_temp):
        self.zidan_list.append(zi_dan_temp)

    def __str__(self) -> str:
        return "弹夹的信息为：%d/%d" % (len(self.zidan_list), self.max_num)


class Zidan(object):
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li


def main():
    laowang = Person("老王")
    ak47 = Gun("AK47")
    dan_jia = Danjia(20)
    for i in range(15):
        zi_dan = Zidan(10)
        laowang.anzhuang_zidan(dan_jia, zi_dan)

    laowang.anzhuang_danjia(ak47, dan_jia)


# test: 测试弹夹信息
    print(dan_jia)
    print(ak47)
    laowang.naqiang(ak47)
    # 测试老王d
    print(laowang)
    # 创建敌人
    gebi_laosong = Person("隔壁老宋")
    print(gebi_laosong)


if __name__ == "__main__":
    main()
