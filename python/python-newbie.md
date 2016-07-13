Python入门
-----------

## 什么是Python？

Python是一门优雅而健壮的编程语言，它继承了传统编译语言的强大性和通用性，同时也
借鉴了简单脚本和解释语言的易用性。生于1989年，作者是Guido Van Rossum：

![Python之父](https://raw.github.com/isoft-linux/training/master/python/guido-van-rossum.png)

## 为什么使用Python？

Ubuntu安装器[ubiquity](https://launchpad.net/ubiquity)、打印机设置[system-config-printer](http://cyberelk.net/tim/software/system-config-printer/)、大黄狗包管理器[yum](http://yum.baseurl.org/)、替代YUM[dnf](http://dnf.baseurl.org/)、协同打RPM包平台[koji](https://fedoraproject.org/wiki/Koji)、web开发框架[django](https://www.djangoproject.com/)等开源项目都在使用Python！
为了修复缺陷或[二次开发](https://github.com/isoft-linux/django-mama-cas)，需要简单了解Python。

## 如何入门？

Hello World

```
print "Hello World"
```

Hello World Gtk2

```
import pygtk
pygtk.require('2.0')
import gtk

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("delete-event", gtk.main_quit)
window.set_size_request(300, 200)
   
label = gtk.Label("Hello World")
window.add(label)
    
window.show_all()

gtk.main()
```

Hello World Gtk3

```
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_size_request(300, 200)
window.connect("delete-event", Gtk.main_quit)

label = Gtk.Label("Hello World")
window.add(label)

window.show_all()

Gtk.main()
```

Hello World Qt4

```
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
window.resize(300, 200)

label = QtGui.QLabel("Hello World")

window.setCentralWidget(label)
window.show()

app.exec_()
```

Hello World Qt5

```
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.resize(300, 200)

label = QtWidgets.QLabel("Hello World")

window.setCentralWidget(label)
window.show()

app.exec_()
```

## 考试题

* 实现print_directory_contents函数

```
def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    fill_this_in
```

* A0~A6的值

```
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
```

* list的值

```
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)
```

* 请把Gtk、Qt的Hello World例子改写成OOP风格

* OO

```
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()
```

## 参考资料

* [Python核心编程第二版](http://isoft.zhcn.cc/~wuxiaotian/ebooks/Python%20%e6%a0%b8%e5%bf%83%e7%bc%96%e7%a8%8b%20%e7%ac%ac%e4%ba%8c%e7%89%88.pdf)
* [Python3程序开发指南](http://isoft.zhcn.cc/~wuxiaotian/ebooks/Python3%E7%A8%8B%E5%BA%8F%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97.pdf)
* [Python Success Stories](https://www.python.org/about/success/)
* [Python 3 programs versus C gcc](http://benchmarksgame.alioth.debian.org/u64q/compare.php?lang=python3&lang2=gcc)
* [15 Essential Python Interview Questions](https://www.codementor.io/python/tutorial/essential-python-interview-questions)
