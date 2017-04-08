# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

# se = [2]
b = [210, 211, 205, 146, 147, 148, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114
    , 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 85, 68, 70, 71, 72, 73, 74, 75, 76, 953,
     954, 955, 957, 958, 959, 960, 961, 962, 963, 964, 989, 990, 991, 992, 492, 493, 494, 495, 496, 497]
class TfengyunSpider(scrapy.Spider):
    name = "tfengyun"
    allowed_domains = ["tfengyun.com"]
    start_urls = (
        # 'http://www.tfengyun.com/',
    )


    def start_requests(self):
        for i in b:
            url = 'http://www.tfengyun.com/user.php?action=rank&sortid='+str(i) +'&offset=1&count=10000&orderby=1&province=&city='
            # url = 'http://www.tfengyun.com/user.php?action=rank&sortid='+str(i)+'&offset=1&count=100&orderby=1&province=&city='
            yield Request(url=url, callback=self.parse0)

    def parse0(self, response):
        selector = Selector(response)
        user_id = selector.xpath('//user_id/text()').extract()
        for a in user_id:
            f = open('id.txt', 'a')
            f.write("'http://weibo.cn/u/" + a +"',\n")
            f.close()
