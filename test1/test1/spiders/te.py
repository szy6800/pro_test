import scrapy


class TeSpider(scrapy.Spider):
    name = 'te'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.text)

        print('测试上传')
        print("测试拉去")
        print("啦啦啦啦")

