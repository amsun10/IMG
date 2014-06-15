#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     
#
# Author:      Xiang
#
# Created:     15/06/2014
# Copyright:   (c) Xiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib,urllib2,cookielib
import re
import os
PAGE_COUNT = 14
class CImgParser:
    def __init__(self,):
        self.cj = cookielib.LWPCookieJar()
        self.Parser = None
        self.Opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.RequestURL = "http://tieba.baidu.com/p/2824768376?see_lz=1&pn=%d"

    def GetImgs(self,):
        Summary = []
        os.chdir(r"pics/")
        for i in range(PAGE_COUNT):
            URL = self.RequestURL % (i+1)
            request = urllib2.Request(URL)
            result = self.Opener.open(request).read()
            Summary.extend(self.ImgParser(result))
            self.DLImg(Summary)
            #print result
        pass
       
    def ImgParser(self,data):
        pat = """src="(http://imgsrc.baidu.com/forum/w%3D580[\s\S]*?)\""""
        pat = re.compile(pat)
        summary = pat.findall(data)
        return summary
        
    #downloading IMG from a list of Links    
    def DLImg(self,data):
        i = 0
        for link in data:
           url = r"%s" % link 
           fileName = link.split('/')[-1]          
           path = "%s.jpg" % i
           print r"Downloading %s" % link
           print path
           urllib.urlretrieve(url,path)
           print "OK"
           i+=1
           pass
        pass
def main():
    oYieldSummaryHandler = CImgParser()
    oYieldSummaryHandler.GetImgs()
    pass

if __name__ == '__main__':
    main()
