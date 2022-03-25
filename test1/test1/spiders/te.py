import scrapy
from scrapy.http import HtmlResponse
import jsonpath,json
from selenium import webdriver
# https://www.bilibili.com/video/BV1KJ41127MX?p=5
#访问
class TeSpider(scrapy.Spider):
    name = 'te'
    start_urls = ["https://www.ebidding.com/portal/html/index.html#page=main:announcement"]
    # allowed_domains = ['baidu.com']

    def __init__(self):
        super(TeSpider, self).__init__()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

    def close(self, spider):
        self.driver.quit()
        print('selenium 关闭')


    def parse(self, response):
        titles = response.xpath('//*[@id="a_head"]/li[position()>1]//*[@class="a_title"]/@title').getall()
        print(titles)
        # # 将我们得到的数据封装到一个 `ItcastItem` 对象
        # item = dict()
        # # xpath返回的是包含一个元素的列表
        # item['name'] = '1'
        # item['title'] = '3'
        # item['info'] = '2'
        #
        # # 直接返回最后数据
        # # print(items)
        # return item










