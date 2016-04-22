# encoding: utf-8
"""
    给一个字符串以w或W开头的单词后面添加s
    比如：word is a Word what b c wre
    变成: words is a Words what b c wres
    用到的其实是sub(pattern, repl, string, count=0, flags=0)
    里的第二个参数可以是callable
"""
import re
input_str = 'word abc Word ww'
def repl(m):
    return m.group(0)+'s'

def rev(s):
    new_str=re.sub(r'[wW]\w+\b', repl, s)
    print new_str

rev(input_str)

