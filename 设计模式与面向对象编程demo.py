# _*_coding:utf-8_*_
# created by Amuu on 2022/9/8


# class Payment:
#     def pay(self, money):
#         raise NotImplementedError


from abc import ABCMeta, abstractmethod


#  接口
class Payment(metaclass=ABCMeta):
    #  abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):  # Alipay 实现了 Payment 接口
    def __init__(self, huabei=False):
        self.huabei = huabei

    def pay(self, money):
        if self.huabei:
            print("huabei:", money)
        else:
            print("Alipay:", money)


class Wechatpay:
    def pay(self, money):
        print("Wechatpay:", money)


class Bankpay:
    def pay(self, money):
        print("Bankpay:", money)


p = Alipay()
p.pay(100)


class User:
    def show_name(self):
        pass


class VIPUser(User):
    def show_name(self):
        pass


u = User()


def shou_user(u):
    res = u.show_name()


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class tiger(LandAnimal):
    def walk(self):
        print("tiger")


"""
class qingwa(LandAnimal,WaterAnimal):
    def ..
"""

t = tiger()
print(t)


# 简单工厂模式
class PaymentFactory:
    def create_payment(self, money):
        if money == 'Alipay':
            return Alipay()
        elif money == 'Wechatpay':
            return Wechatpay()
        elif money == 'huabei':
            return Alipay(huabei=True)
        else:
            raise TypeError("No such payment named %s" % money)


pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)


#  工厂方法模式
class PaymentFactory2(metaclass=ABCMeta):
    @abstractmethod
    def create_payment2(self):
        pass


class AlipayPaymentFactory(PaymentFactory2):
    def create_payment2(self):
        return Alipay()


class WechatpayPaymentFactory(PaymentFactory2):
    def create_payment2(self):
        return Wechatpay()


class huabeiPaymentFactory(PaymentFactory2):
    def create_payment2(self):
        return Alipay(huabei=True)


class BankpayPaymentFactory(PaymentFactory2):
    def create_payment2(self):
        return Bankpay()


pf = BankpayPaymentFactory()
p = pf.create_payment2()
p.pay(100)


# 抽象工厂模式
# -----抽象产品-----

class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# -----抽象工厂-----

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# -----具体产品-----

class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("蛟龙CPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("IOS系统")


# -----具体工厂-----

class IPhoneFactory(PhoneFactory):
    def make_os(self):
        return IOS()

    def make_cpu(self):
        return AppleCPU()

    def make_shell(self):
        return AppleShell()


class MiFactory(PhoneFactory):
    def make_os(self):
        return Android()

    def make_cpu(self):
        return SnapDragonCPU()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    def make_os(self):
        return Android()

    def make_cpu(self):
        return MediaTekCPU()

    def make_shell(self):
        return SmallShell()


# -----客户端-----

class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


p1 = make_phone(IPhoneFactory())
p1.show_info()


#  建造者模式
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuider(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayerBuider):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = "漂亮隔膜"

    def build_leg(self):
        self.player.leg = "大长腿"


class MonsterBuilder(PlayerBuider):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "长毛胳膊"

    def build_leg(self):
        self.player.leg = "长毛腿"


class PlayerDirector:  # 控制不同组装顺序
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


#  客户端

builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)


#  单例模式
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
print(a.a)
b = MyClass(20)
print(a.a)
print(b.a)
print(id(a), id(b))


# ————————————————————————————————————————
#  适配器模式

class BankPay:
    def cost(self, money):  # 无pay方法
        print("Bankpay", money)


class LoongPay:
    def cost(self, money):  # 无pay方法
        print("Loongpay", money)


# #  类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)

#  对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


a = PaymentAdapter(LoongPay())
a.pay(100)


#  组合

class A:
    pass


class B:
    def __init__(self):
        self.a = A()


# ————————————————————————————————————————

#  桥模式

# class Shape:
#     pass
# class Line(Shape):
#     pass
# class Rectangle(Shape):
#     pass
# class Cricle(Shape):
#     pass
# class RedLine(Line):
#     pass
# class GreenLine(Line):
#     pass
# class BuleLine(Line):
#     pass

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色", shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色", shape.name)


shape = Rectangle(Red())
shape.draw()

shape1 = Circle(Green())
shape1.draw()


# ————————————————————————————————————————

#  组合模式
# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s,%s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s,%s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("---复合图形---")
        for g in self.children:
            g.draw()
        print("---复合图形---")


L = Line(Point(1, 1), Point(2, 2))
print(L)

p1 = Point(2, 3)
l1 = Line(Point(3, 4), Point(6, 7))
l2 = Line(Point(1, 5), Point(2, 8))
pic1 = Picture([p1, l1, l2])
pic1.draw()
p2 = Point(4, 4)
l3 = Line(Point(1, 1), Point(0, 0))
pic2 = Picture([p2, l3])
pic = Picture([pic1, pic2])
pic.draw()


# ————————————————————————————————————————
#  外观模式

# 子系统类
class CPU:
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止运行")


class Disk:
    def run(self):
        print("硬盘开始运行")

    def stop(self):
        print("硬盘停止运行")


class Memory:
    def run(self):
        print("内存开始运行")

    def stop(self):
        print("内存停止运行")


#  外观
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


computer = Computer()
computer.run()
computer.stop()


# ————————————————————————————————————————
#  代理模式

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r')
        print("读取文件内容")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        f.close()


# 虚代理

class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self:
            self.subj = RealSubject(self.filename)
        return self.subj.set_contene(content)


# 保护代理

class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限')


subj = RealSubject('test.txt')

subj2 = VirtualProxy('test.txt')
print(subj.get_content())
subj3 = ProtectedProxy('test.txt')
print(subj3.get_content())


# subj3.set_content("abc")

# ————————————————————————————————————————
#  责任链模式

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def hanle_leave(self, day):
        pass


class GeneralManager(Handler):
    def hanle_leave(self, day):
        if day <= 10:
            print('总经理准假%d天' % day)
        else:
            print('你还是辞职吧')


class Departmentamager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def hanle_leave(self, day):
        if day <= 5:
            print('部门经理准假%d天' % day)
        else:
            print('部门经理职权不足')
            self.next.hanle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = Departmentamager()

    def hanle_leave(self, day):
        if day <= 3:
            print('项目主管准假%d天' % day)
        else:
            print('项目主管职权不足')
            self.next.hanle_leave(day)


day = 7

h = ProjectDirector()
h.hanle_leave(day)


# ————————————————————————————————————————
#  观察者模式

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass


class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice):  # 具体发布者
    def __init__(self, company_info):
        super().__init__()
        self.__company_info = company_info

    @property  # 读
    def company_info(self):
        return self.__company_info

    @company_info.setter  # 写
    def company_info(self, info):
        self.__company_info = info
        self.notify()  # 推送


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice('初始公司信息')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年业绩非常好，给大家发奖金！"
print(s1.company_info)
print(s2.company_info)


# ————————————————————————————————————————
#  策略模式

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("快策略", data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("慢策略", data)


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = '[.....]'

s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()
# ————————————————————————————————————————
#  模块方法模式
from time import sleep


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self): # 原子操作/钩子操作
        pass

    def run(self):  # 模板方法
        self.stop()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()

class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('窗口开始运行')

    def stop(self):
        print('窗口结束运行')

    def repaint(self):
        print(self.msg)
MyWindow('hello').run()