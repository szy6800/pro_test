import scrapy


class TeSpider(scrapy.Spider):
    name = 'te'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page=4&ka=page-4']

    def parse(self, response):
        print(response.text)


