# -*- coding: gbk -*-
import urllib
import re

print "-" * 15, "��ȡ����Hosts�ű�����", "-" * 15
print "-" * 12, "��ȡ��Դ������Ч-make by calm", "-" * 13
print "����������Դ�����Ե�..."
hostSrcURL = "https://github.com/racaljk/hosts/blob/master/hosts"
html = urllib.urlopen(hostSrcURL).read()
# print html
print "���ڻ�ȡ���µ�Host�ļ��У����Ե�..."

patten = re.compile(r"<tr.*?<td.*?</td>.*?<td.*?>(.*?)</td>.*?</tr>", re.I | re.S | re.X)
match = patten.findall(html)
print "����������洴��һ���µ�hosts�ļ�������д��..."
f = open("C:\Users\calm\Desktop\hosts", 'w+')
# print "���ڸ���Host�ļ�..."
for item in match:
    f.write(item + "\n")
    print item
f.write("\n")
f.close()
print "����������洴��һ���µ�hosts�ļ���д��ɹ�!"
print ""
