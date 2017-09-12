# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re

class CJPRESS:
    def __init__(self,baseUrl,tagID,pageNum):
        self.baseURL = baseUrl
        self.tagID = '&tag_id=' +str(tagID)
        self.file = None
        self.defaultTitle = u"长江大数据"
        self.pageNum = pageNum
    # 获取页面所有内容
    def getPage(self,pageNum):
        try:
            url = self.baseURL + 'topage=' +str(pageNum) + self.tagID + '&classification_id=&sales_name=book'
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
            content = title + "|\n"
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
tag_page= [(3868,1),(3827,2),(3829,1),(3830,2),(3833,1),(3835,2),(3836,2),(3838,2),(3894,3),(3843,1),(3850,1),(3854,1),(3855,1),(3856,1),(3857,1),(3858,1),(3859,1),(3860,2),(3870,5),(3871,1),(3872,2),(3873,5),(3874,1),(3875,1),(3876,2),(3877,2),(3878,1),(3879,2),(3882,3),(3885,8),(3888,3),(3891,7)]
for (tagID,pageNum) in tag_page:
    cjpress = CJPRESS(baseURL,tagID,pageNum)
    cjpress.start()