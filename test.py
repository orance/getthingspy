# _*_ coding:utf-8 _*_
import re
titles = '<a href="first_level.aspx?classification_id=&tag_id=3836">长江水资源保护规划</a>'
pattern = re.compile('<a href="first_level.aspx.*?>(.*?)</a>',re.S)
result = re.search(pattern,titles)
print result.group(1).strip()