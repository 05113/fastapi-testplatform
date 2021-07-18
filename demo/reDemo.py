import re

a = 'll{warehouseID}kk{aaaa}'

res = re.compile('{.*?}')

print(re.findall('{.*?}',a))
k = res.match(a)

# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。

# . 字符正则 只匹配除换行符的任意字符
print(re.search('.','a\nb').group()) #search匹配一次字符串
print(re.findall('.' , 'a\nb'))  #匹配a,b findall是匹配字符串所有的匹配

# ^ 字符正则 匹配开头以^后边的所有字符,如果没有返回none
print(re.findall('^abcd' , 'kkkabcdabcd')) #字符串开头为kkks,所以返回none匹配不上
print(re.findall('^abcd' , 'abcda')) #返回abcd
print(re.findall('^abcd.' , 'abcdalmnb')) #返回abcda 因为匹配开头abcd加'.'的任意匹配,所以匹配abcda

# $ 字符正则 同^规则,只不过是匹配尾部
print(re.findall('abcd$' , 'kkkabcd'))
print(re.findall('^kk.ll$','kkall')) #返回kkall,匹配开头字符kk加上'.'的任意匹配 再加上字尾的ll
print(re.findall('^kk.ll$','kkabll')) #返回none匹配不到,字尾匹配不到

# * 字符正则
print(re.findall('a*' , "abcd"))

# + 字符正则 对他前面的字符串匹配一次或任意次
print(re.findall('ab+' , 'ab')) #返回 ab
print(re.findall('ab+' , 'abb')) #返回 abb
print(re.findall('ab+' , 'labc')) #返回 ab , 从a开始匹配后边配任意b,因为c不同所以结束匹配
print(re.findall('.*','abcdaaa')) #字符串是啥返回啥,.代表任意字符，再加上*任意匹配
print(re.findall('.*}','abcdaaa')) #返回none,与上面不同的是多个'}',字符串没有'}',所以匹配不上

# ? 字符正则 对它前面的字符只匹配0次或一次

print(re.findall('ab?','abb')) #返回ab,b只匹配一次
print(re.findall('ab?','a')) #返回a,b相当于匹配0次
print(re.findall('ab?','ac')) #返回a,b相当于匹配0次
print(re.findall('.*?}','aa}aa}')) #匹配到第一个aa},因为'?'只匹配一次或0次,所以第一个'}'代表结束
print(re.findall('.*}','aa}aa}')) #匹配aa}aa}



print(k)

print(re.findall('{(.*?)}','{aaa}/{kkk}'))
print(re.sub(r'{.*?}' , '1' , '{aaa}/{bbb}'))
# print(re.sub('{.*?}','kkk','{aaa}/{kkk1}'))
#
# pattern = '{(.*?)}'
# result = re.match(pattern,'{aaa}/{bbb}')
# print(result.group(1))
print(re.search('\$(.+)}|\$(.+),','kkkkkkk$a}').group(1))

print(re.search('\$(.+)','$key1').group(1))

k = '<div class="nam">中国</div>'
print(re.findall('.*?>(.*?)<',k))
a = "not 404 found 张三 99 深圳"


