import pytest
import os
import sys

class redirect:
    content = []

    def write(self,str):
        self.content.append( str)
    def flush(self):
        self.content = ""

global r
r = redirect()


r = redirect()
sys.stdout = r
print('test0')
print('test1')
print('test3')


# print directory redirected. The prompts and results are all stored in print.txt file

f = open('print.txt', 'w')
for i in range(len(r.content)):
    f.write(r.content[i])
# remove all \n symbols, leaving only strings of real content in list r.content
istr = ""
for istr in r.content:
    if istr == '\n':
        r.content.remove(istr)

length = len(r.content)
f.write(str(length))
f.close()


def test_0():
    assert r.content[0] == 'test0'

def test_1():
    if (len(r.content) >= 1):
        assert r.content[1] == 'test1'
    else:
        assert 1 == 0

def test_2():
    if (len(r.content) >= 2):
        assert r.content[2] == 'test2'
    else:
        assert 1 == 0

def test_noob():
    assert 1 == 1



