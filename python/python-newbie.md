Python入门
-----------

## 什么是Python？

Python是一门优雅而健壮的编程语言，它继承了传统编译语言的强大性和通用性，同时也
借鉴了简单脚本和解释语言的易用性。生于1989年，作者是Guido Van Rossum：

![Python之父](https://raw.github.com/isoft-linux/training/master/python/guido-van-rossum.png)

## 什么!是Python？

![蟒蛇](https://raw.github.com/isoft-linux/training/master/python/python.jpg)

## 为什么使用Python？

Ubuntu安装器[ubiquity](https://launchpad.net/ubiquity)、打印机设置[system-config-printer](http://cyberelk.net/tim/software/system-config-printer/)、大黄狗包管理器[yum](http://yum.baseurl.org/)、YUM替代[dnf](http://dnf.baseurl.org/)、协同打（RPM）包平台[koji](https://fedoraproject.org/wiki/Koji)、web开发框架[django](https://www.djangoproject.com/)等开源项目都在使用Python！
为了修复缺陷或[二次开发](https://github.com/isoft-linux/django-mama-cas)，需要简单了解Python。

![Python程序员薪水高](https://raw.github.com/isoft-linux/training/master/python/salaryrange.png)

## 如何入门？

Hello World

```
print("Hello World")
```

Hello World Gtk2

* [pygtk](http://www.pygtk.org/)

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

* [PyGI](https://wiki.gnome.org/Projects/PyGObject)

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

* [PyQt](https://sourceforge.net/projects/pyqt/)

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

游戏开发

* [PyGame](http://www.pygame.org/hifi.html)
* [Soya3](http://www.lesfleursdunormal.fr/static/informatique/soya3d/index_en.html)

* [热火吉他手](https://github.com/skyostil/fretsonfire)

![热火吉他手的截屏](https://raw.github.com/isoft-linux/training/master/python/fretsonfire.png)

* [巴拉萨尔野生动物园](http://www.lesfleursdunormal.fr/static/informatique/balazar_safari_photo/index_en.html)

![巴拉萨尔野生动物园的截屏](http://www.lesfleursdunormal.fr/static/_images/bsf/2/6.jpeg)

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

* 请把Gtk、Qt的Hello World例子改写成OOP风格

* 在终端上“画”Hello World

## 参考资料

* [Python核心编程第二版](http://isoft.zhcn.cc/~wuxiaotian/ebooks/Python%20%e6%a0%b8%e5%bf%83%e7%bc%96%e7%a8%8b%20%e7%ac%ac%e4%ba%8c%e7%89%88.pdf)
* [Python3程序开发指南](http://isoft.zhcn.cc/~wuxiaotian/ebooks/Python3%E7%A8%8B%E5%BA%8F%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97.pdf)
* [Python Success Stories](https://www.python.org/about/success/)
* [Python Manual](https://docs.python.org/2/)
* [15 Essential Python Interview Questions](https://www.codementor.io/python/tutorial/essential-python-interview-questions)
* [What Programming Language Should a Beginner Learn in 2016?](https://www.codementor.io/learn-programming/beginner-programming-language-job-salary-community)
