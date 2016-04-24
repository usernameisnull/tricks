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

def rev2(s):
    """
    第二种方案
    让sub的第二个参数为string，而不是callable，更好
    """
    new_str = re.sub(r'\b([wW]\w+)\b', r'\1s', s)
    return new_str

print rev2(input_str)


def rev3(s):
    """
    第三种方案
    sub的第二个参数使用\g<1>,比起第二个方案的好处是，如果我要在单词的末尾
    添加‘0’，那么第二个方案就会出问题\10，会认为是第10个匹配组
    """
    new_str = re.sub(r'\b[wW]\w+\b', r'\g<1>s', s)
    return new_str

print rev2(input_str)

# raise error, "invalid group reference"
#print re.sub(r'\b([wW]\w+)\b', r'\10', input_str)
print re.sub(r'\b([wW]\w+)\b', r'\g<1>0', input_str)

    
