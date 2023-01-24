#!/usr/bin/env python3

# standard library imports        
import shutil
import os

def main():
    """called at runtime"""
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input('What is the new name for kerrigan.obj? ')

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
