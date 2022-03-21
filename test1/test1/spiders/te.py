import scrapy
from scrapy.http import HtmlResponse
import jsonpath,json
class TeSpider(scrapy.Spider):
    name = 'te'
    allowed_domains = ['baidu.com']
    start_urls = ["https://www.cnblogs.com/leijiangtao/p/4806683.html"]

    def parse(self, response):
        # 将我们得到的数据封装到一个 `ItcastItem` 对象
        item = dict()
        # xpath返回的是包含一个元素的列表
        item['name'] = '1'
        item['title'] = '3'
        item['info'] = '2'

        # 直接返回最后数据
        # print(items)
        return item










