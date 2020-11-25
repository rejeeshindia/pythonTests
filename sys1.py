#!#/usr/bin/env python3
import os


def mkdir(path,name):
    orig_path = os.getcwd()
    
    os.chdir(path)
    os.mkdir(name)
    os.chdir(orig_path)


if __name__ == '__main__':
    mkdir('/tmp','new')
