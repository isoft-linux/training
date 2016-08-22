Python入门
-----------

## 什么是Python？

Python是一门优雅而健壮的编程语言，它继承了传统编译语言的强大性和通用性，同时也
借鉴了简单脚本和解释语言的易用性。生于1989年，作者是Guido Van Rossum：

![Python之父](https://raw.github.com/isoft-linux/training/master/python/guido-van-rossum.png)

## 什么不是Python？

![蟒蛇](https://raw.github.com/isoft-linux/training/master/python/python.jpg)

## 为什么使用Python？

Ubuntu安装器[ubiquity](https://launchpad.net/ubiquity)、打印机设置[system-config-printer](http://cyberelk.net/tim/software/system-config-printer/)、大黄狗包管理器[yum](http://yum.baseurl.org/)、YUM替代[dnf](http://dnf.baseurl.org/)、[libvirt](http://libvirt.org/)前端[virt-manager](https://virt-manager.org/)、协同打（RPM）包平台[koji](https://fedoraproject.org/wiki/Koji)、web开发框架[django](https://www.djangoproject.com/)等开源项目都在使用Python！
为了修复缺陷或[二次开发](https://github.com/isoft-linux/django-mama-cas)，需要简单了解Python。

Python程序员薪水***高***！

![Python程序员薪水高](https://raw.github.com/isoft-linux/training/master/python/salaryrange.png)

## 如何入门？

### Hello World

```
print("Hello World")
```

### 运算符 && 位操作

```
+       -       *       **      /       //      %
<<      >>      &       |       ^       ~
<       >       <=      >=      ==      !=      <>

x = int(2)      #       00000000000000000000000000000010
y = int(3)      #       00000000000000000000000000000011
#------------------------------------------------------------------------------
print(x ** y)   # POW
print(x // y)   # MOD
print(x | y)    # OR    00000000000000000000000000000011 -> 3
print(x ^ y)    # XOR   00000000000000000000000000000001 -> 1
print(x & y)    # AND   00000000000000000000000000000010 -> 2
print(x << y)   # LS    00000000000000000000000000010000 -> 16
print(x >> 1)   # RS    00000000000000000000000000000001 -> 1

'''
Two's complement
https://en.wikipedia.org/wiki/Two%27s_complement
'''
print(~x)       # INV   11111101 <- 11111100 + 1 <- NEG(00000011) -> -3
'''
Signed number representations
https://en.wikipedia.org/wiki/Signed_number_representations
'''
n = int(-37)
print(bin(n))   # 10100101
print(n.bit_length())
m = int(-1)
print(bin(m))   # 11111111
print(m.bit_length())
```

编译[leslie_bin.cpp](https://github.com/isoft-linux/training/blob/master/python/leslie_bin.cpp)运行看效果。

### 关键字

```
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try
```

### float

```
def testFloat():
    a = float(1.0 / 81)
    b = float(0.0)
    for i in range(729):
        b += a;
    print("%.15g" % (b));   # *NOT* 9.00002288818359 in C/C++

testFloat() # 8.99999999999996
```

### 复数

```
print(complex(1, 1))    # (1+1j)
```

### list

```
lists = []
for i in range(13):
    lists.append(i)
lists.append(12)
lists.append(12)
print(lists)        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12]
print(set(lists))   # set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
lists.reverse()
print(lists)        # [12, 12, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lists.sort()
print(lists)        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12]
lists.pop()
print(lists)        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]
lists.pop()
print(lists)        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(len(lists))   # 13
lists[:] = []
print(lists)        # []

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
print(matrix)       # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

### tuple

```
tup = ('Python', 83, ('Linux', 'KDE'))
print(tup)      # ('Python', 83, ('Linux', 'KDE'))
print(tup * 3)  # ('Python', 83, ('Linux', 'KDE'), 'Python', 83, ('Linux', 'KDE'), 'Python', 83, ('Linux', 'KDE'))
```

### set

```
sets = {'Martin Gräßlin', 'David Faure', 'Sebastian Kügler'}
print(sets)
a = set('abracadabra')
b = set('alacazam')
print(a)        # set(['a', 'r', 'b', 'c', 'd'])
print(b)        # set(['a', 'c', 'z', 'm', 'l'])
print(a - b)    # set(['r', 'b', 'd'])
print(a | b)    # set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])
print(a & b)    # set(['a', 'c'])
print(a ^ b)    # set(['b', 'd', 'm', 'l', 'r', 'z'])
```

### dictionary

```
dict = {'Name': 'Martin Gräßlin', 'Age': 27, 'Project': 'KWin'}
print(dict)
dict['Age'] = 21
print(dict)
print(dict.has_key('Home'))
dict['Home'] = 'Germany'
print(dict.has_key('Home'))
for k, v in dict.items():
    print(k, v)
```

### if

```
if __name__ == "__main__":
    print("The if statement is used for conditional execution")
else:
    print("Being imported from another module")
```

### while

```
i = 3
while i:
    if i == 1:
        break
    print("The while statement is used for repeated execution as long as an expression is true")
    i = i - 1
```

### for

```
def generator(r=3):
    for i in range(r):
        if i == 0:
            continue
        print("The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable objec")
        yield i * i

for i in generator():
    print(i)
```

### try ... except ... finally

```
try:
    1 / 0
except:
    print("The try statement specifies exception handlers and/or cleanup code for a group of statements")
finally:
    print("If finally is present, it specifies a ‘cleanup’ handler")
```

### with

```
try:
    with open("/dev/input/mice", 'r') as fptr:
        pass
except:
    print("The with statement is used to wrap the execution of a block with methods defined by a context manager")
```

### def func()

```
def func(c=None):
    return {
            'a': "case 'a':",
            'b': "case 'b':",
            }.get(c, "default:")
print(func("c"))
```

### class obj(object)

```
class obj(object):
    def __init__(self):
        print(sys._getframe().f_code.co_name)

    def __del__(self):
        print(sys._getframe().f_code.co_name)

obj1 = obj()
del obj1
obj1 = None

class Father(object):
    __mAttr = 100

    def __init__(self):
        print("\033[31mCalling father constructor\033[0m")

    def __del__(self):
        print("\033[31mCalling father destructor\033[0m")

    def fatherMethod(self):
        print("\033[31mCalling father method\033[0m")

    def setAttr(self, attr):
        self.__mAttr = attr

    def getAttr(self):
        print("\033[31mCalling father getAttr %d\033[0m" % (self.__mAttr))

    def myMethod(self):
        print("\033[31mCalling father method\033[0m")
        
class Mother(object):
    __mAttr = 101

    def __init__(self):
        print("\033[31mCalling mother constructor\033[0m")

    def __del__(self):
        print("\033[31mCalling mother destructor\033[0m")

    def motherMethod(self):
        print("\033[31mCalling mother method\033[0m")

    def setAttr(self, attr):
        self.__mAttr = attr

    def getAttr(self):
        print("\033[31mCalling mother getAttr %d\033[0m" % (self.__mAttr))

    def myMethod(self):
        print("\033[31mCalling mother method\033[0m")

class Child(Father, Mother):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        print("Calling child constructor")

    def __add__(self, r):
        return Child(self.a + r.a, self.b + r.b)

    def __str__(self):
        return 'Child (%d, %d)' % (self.a, self.b)

    def childMethod(self):
        print("Calling child method")

    def myMethod(self):
        print("Calling child method")

c = Child()
c.childMethod()
c.fatherMethod()
c.setAttr(300)
c.getAttr()
c.myMethod()

c1 = Child(2, 10)
c2 = Child(5, -2)
print(c1 + c2)
```

Python的基本语法、数据结构、类、常用函数... 请查看[Python Manual](https://docs.python.org/2/)

### Hello World Gtk2

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

### Hello World Gtk3

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

### Hello World Qt4

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

### Hello World Qt5

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

### 游戏开发

* [PyGame](http://www.pygame.org/)
* [Soya3](http://www.lesfleursdunormal.fr/static/informatique/soya3d/index_en.html)

* [热火吉他手](https://github.com/skyostil/fretsonfire)

![热火吉他手的截屏](https://raw.github.com/isoft-linux/training/master/python/fretsonfire.png)

* [巴拉萨尔野生动物园](http://www.lesfleursdunormal.fr/static/informatique/balazar_safari_photo/index_en.html)

![巴拉萨尔野生动物园的截屏](http://www.lesfleursdunormal.fr/static/_images/bsf/2/6.jpeg)

### 科学计算

* [SciPy](https://www.scipy.org/)
* [NumPy](http://www.numpy.org/)
* [Matplotlib](http://matplotlib.org/)
* [SymPy](http://www.sympy.org/)
* [pandas](http://pandas.pydata.org/)

![SciPy信号处理](https://www.packtpub.com/sites/default/files/Article-Images/7702OS_05_03.png)

## 绑定

### 为什么要绑定？

* Linux下大量的库使用C/C++开发
* Python很***慢***！

![C/C++与Python速度对比](https://isoft-linux.org/wp-content/uploads/2016/07/cc-programs-versus-python-3-186-1.png)

所以PyGtk、SciPy、NumPy等使用C开发，为Python提供绑定。

### 如何写一个最简单的绑定？

* leslie_tz.c

- Python与C数据类型之间的转换，例如：[PyInt_FromLong](https://docs.python.org/2/c-api/int.html#c.PyInt_FromLong)
- 定义在XXX_methods[]中的函数指针[PyCFunction](https://docs.python.org/2/c-api/structures.html#c.PyCFunction)
- 定义在XXX_Type中的函数指针[PyTypeObject](https://docs.python.org/2/c-api/type.html#c.PyTypeObject)
- initXXX构造函数[PyMODINIT_FUNC](https://docs.python.org/2/extending/newtypes.html)
- [PyArg_ParseTuple](https://docs.python.org/2/c-api/arg.html#c.PyArg_ParseTuple)解析Python脚本传递的参数
- 数据类型检测，例如：[PyTuple_Check](https://docs.python.org/2/c-api/tuple.html#c.PyTuple_Check)
- 多线程锁PyGILState_STATE, [PyGILState_Ensure](https://docs.python.org/2/c-api/init.html#c.PyGILState_Ensure), [PyGILState_Release](https://docs.python.org/2/c-api/init.html#c.PyGILState_Release)
- 在C中调用Python（脚本）函数[PyEval_CallFunction](http://starship.python.net/crew/mwh/toext/calling-python-from-c.html)
- 引用计数、垃圾回收[Py_INCREF](https://docs.python.org/2/c-api/refcounting.html#c.Py_INCREF), [Py_XDECREF](https://docs.python.org/2/c-api/refcounting.html#c.Py_XDECREF), [Py_DecRef](https://docs.python.org/2/c-api/refcounting.html#c.Py_DECREF)

```
#include <Python.h>
#include <time.h>

#define INT(v) PyInt_FromLong(v)

static PyObject *gmtoff(PyObject *self, PyObject *args);

static PyMethodDef leslie_tz_methods[] = 
{
    {"gmtoff", gmtoff, 0, "Leslie timezone get gmtoff"}, 
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initleslie_tz() 
{
    PyObject *m = NULL;

    m = Py_InitModule("leslie_tz", leslie_tz_methods);
    if (!m)
        return;
}

static PyObject *gmtoff(PyObject *self, PyObject *args) 
{
    time_t cur_time = time(NULL);
    struct tm *local_tm = localtime(&cur_time);

    return INT(local_tm->tm_gmtoff / 3600);
}
```

* setup.py

```
from setuptools import setup, Extension
import os
import commands

leslie_tz_mod = Extension('leslie_tz', sources = ['leslie_tz.c'])

setup(name='leslie_tz',
      version='0.1',
      ext_modules = [leslie_tz_mod],
      description='Leslie TimeZone Python Binding.',
      long_description ="""Leslie TimeZone Python Binding.""",
      author='Leslie Zhai',
      author_email='xiang.zhai@i-soft.com.cn',
      license='GPL-3',
      url="https://github.com/isoft-linux/training/tree/master/python",
      download_url="git@github.com:isoft-linux/training.git",
      platforms = ['Linux'],
)
```

* hellotz.py

```
import sys
import time
try:
    import leslie_tz
except ImportError:
    if sys.version_info.major != 3:
        print("--------Please Install Leslie TimeZone Python Binding--------")
        print("```sudo python2 setup.py install```")
        print("-------------------------------------------------------------")

if sys.version_info.major == 3:
    print(int(time.localtime().tm_gmtoff / 3600))
else:
    print(leslie_tz.gmtoff())
```

## 参考资料

* [Python核心编程第二版](http://isoft.zhcn.cc/~wuxiaotian/ebooks/Python%20%e6%a0%b8%e5%bf%83%e7%bc%96%e7%a8%8b%20%e7%ac%ac%e4%ba%8c%e7%89%88.pdf)
* [Python3程序开发指南](http://isoft.zhcn.cc/~wuxiaotian/ebooks/Python3%E7%A8%8B%E5%BA%8F%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97.pdf)
* [Python Success Stories](https://www.python.org/about/success/)
* [Python Manual](https://docs.python.org/2/)
* [15 Essential Python Interview Questions](https://www.codementor.io/python/tutorial/essential-python-interview-questions)
* [What Programming Language Should a Beginner Learn in 2016?](https://www.codementor.io/learn-programming/beginner-programming-language-job-salary-community)
* [The Joy of SciPy](http://www.slideshare.net/kammeyer/the-joy-of-scipy)
