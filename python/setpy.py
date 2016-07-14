#!/usr/bin/env python

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
