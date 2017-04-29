#!/usr/bin/python

import sys,os

if len(sys.argv) != 2:
    print("Only one argument should be given, the number of commits to make.")
    sys.exit(1)

num_commits = int(sys.argv[1])
print("Creating %d commits" % int(sys.argv[1]))

for i in range(0,num_commits):
    os.system('echo blah >> a.txt')
    os.system('git add *.txt')
    os.system('git commit -m "automated commit"')


