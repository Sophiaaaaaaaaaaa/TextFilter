# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:37:09 2019

@author: Sophia
"""
import re
'''
+ 匹配1次或多次的前面出现的正则表达式
? 匹配0次或1次前面出现的正则表达式
(?=.comm)一个字符串后面跟着.com才开始进行匹配
(?:...)这些匹配不会保存下来供后续使用和数据检索
. 匹配任意字符
*匹配0次或者多次前面出现的正则表达式
{N} 匹配N次前面出现的正则表达式
{M，N}匹配M~N次前面出现的正则表达式
[^...]不匹配此字符集中出现的任何一个字符
\d 匹配任何十进制数字
\w 匹配任何字母数字字符
\s 匹配任何空格字符

'''

pattern1='.python...'
pattern2='^ay$' 
'''$是结束符 ^和$连用可以只限制a开头y结尾'''
pattern3="b[aeiu]t"
pattern4="z.[0-9]"
pattern5="0?[1-9]"
'''可能存在前置为零的数字'''
pattern6="</?[^>]+>"
pattern7="(?:...)"
'''匹配一个不用保存的分组'''
pattern8="(?!.com)"
'''一个字符后面跟着.com之后才做匹配'''
pattern7="(?<=800-)[1-9]"
'''字符串前有800-时才进行匹配'''
pattern8="3\.14"
'''\转义字符  识别的是. 而不是任意字母'''
pattern9="[cr][23][dp][o2]"
'''任选四个括号中一个'''
pattern10="\w+@(\w+\.)?\w+\.com"
'''匹配域名 nobody@xxx.yyy.com'''
pattern11="\w+@(\w+\.)*\w+\.com"
'''匹配多个中间域名'''
m=re.match('(\w\w\w)-(\d\d\d)','abc-123')
print(m.group(2))
'''访问每个独立的子组'''
m.groups()
m=re.match('(a(b(c)))','abc')
print(m.groups())
m=re.findall('car','carry the barcardi to the car')
'''findall 匹配所有符合情况的字符串'''
print(re.sub('[ae]','X','abcdef'))
'''sub 用X分别代替a和e'''
