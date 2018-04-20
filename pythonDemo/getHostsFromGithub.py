# -*- coding: gbk -*-
import urllib
import re

print "-" * 15, "获取最新Hosts脚本程序", "-" * 15
print "-" * 12, "获取资源可能无效-make by calm", "-" * 13
print "正在连接资源，请稍等..."
hostSrcURL = "https://github.com/racaljk/hosts/blob/master/hosts"
html = urllib.urlopen(hostSrcURL).read()
# print html
print "正在获取最新的Host文件中，请稍等..."

patten = re.compile(r"<tr.*?<td.*?</td>.*?<td.*?>(.*?)</td>.*?</tr>", re.I | re.S | re.X)
match = patten.findall(html)
print "已在你的桌面创建一个新的hosts文件，正在写入..."
f = open("C:\Users\calm\Desktop\hosts", 'w+')
# print "正在更新Host文件..."
for item in match:
    f.write(item + "\n")
    print item
f.write("\n")
f.close()
print "已在你的桌面创建一个新的hosts文件，写入成功!"
print ""
