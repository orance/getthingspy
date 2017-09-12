# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re

class CJPRESS:
    def __init__(self,baseUrl,tagID,pageNum):
        self.baseURL = baseUrl
        self.tagID = '&classification_id=' +str(tagID)
        self.file = None
        self.defaultTitle = u"长江大数据"
        self.pageNum = pageNum
    # 获取页面所有内容
    def getPage(self,pageNum):
        try:
            url = self.baseURL + 'topage=' +str(pageNum) + '&tag_id=' + self.tagID + '&sales_name=book'
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url,headers= headers)
            response = urllib2.urlopen(request)
            #print response.read()
            return response.read()
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接失败",e.reason
                return None
    # 获取书籍名称
    def getBookTitle(self,page):
        pattern = re.compile('<div class="book-title.*?>(.*?)</div>',re.S)
        titles = re.findall(pattern,page)
        if titles:
            return titles
        else:
            return
    #获取标签名称
    def getTagName(self,page):
        pattern = re.compile('<a href="first_level.aspx.*?>(.*?)</a>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
    #设置标题名称对应的文件
    def setFileTag(self,tag):
        if tag is not None:
            self.file = open(tag + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")


    #写入书籍名称信息
    def writeData(self,titles):
        content = []
        for title in titles:
            content = title + "|"
            self.file.write(content)

    #开始
    def start(self):
        indexPage = self.getPage(1)
        tag = self.getTagName(indexPage)
        self.setFileTag(tag)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print "该标签共有" + str(pageNum) + "页"
            for i in range(1,int(pageNum)+1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                titles = self.getBookTitle(page)
                self.writeData(titles)
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"

baseURL = 'http://www.cjpress.cn/default/book.aspx?'
tag_page= [(156,2),(157,8),(158,2),(159,7),(161,2),(167,2),(169,4),(170,7),(171,10),(179,20)]
for (tagID,pageNum) in tag_page:
    cjpress = CJPRESS(baseURL,tagID,pageNum)
    cjpress.start()