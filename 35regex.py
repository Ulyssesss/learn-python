"""
\d    匹配一个数字
\w    匹配一个字母或数字
.     匹配任意字符
*     表示任意个字符
+     表示至少一个字符
?     表示0个或1个字符
{n}   表示n个字符
{n,m} 表示 n-m 个字符
\     转义
[]    表示范围，如 [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线
A|B   表示 A 或 B
^     表示行的开头
$     表示行的结束
\s    表示空格或Tab等空白符
正则表达式默认为贪婪模式，? 表示非贪婪模式
Match 对象的 group() 方法可提取出子串，group(0) 是原始字符串，group(1)、group(2) 分别为第 1、2 个子串
"""
import re
r = r'^\d{3}\-\d{3,8}$'
test = '010-12345'
if re.match(r, test):
    print('ok')
else:
    print('failed')

print('a b    c'.split(' '))
print(re.split(r'\s+', 'a b   c'))

m = re.match(r'^(\d+?)(0*)$', '102300')
print(m.groups())
print(m.group(1))
print(m.group(2))

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
