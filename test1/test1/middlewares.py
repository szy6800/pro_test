# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from requests.adapters import HTTPAdapter
import requests
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse

class Test1SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Test1DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        driver = spider.driver
        driver.get(request.url)
        text = driver.page_source
        return HtmlResponse(url=request.url, body=text, request=request, status=200,
                            encoding='utf-8')

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# class SeleniumMiddleware(object):
#     def process_request(self,request,spider):
#         chrome_options = Options()
#         chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
#         # chrome_options.add_argument("--headless")
#         chrome_options.headless = True
#         chrome_options.add_argument('window-size=1400x1015')  # 指定浏览器分辨率
#         chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
#         chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
#         chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
#         chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#         chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
#         chrome_options.add_argument('--start-maximized')  # 浏览器最大化
#         chrome_options.add_argument('--window-size=1280x1024')  # 设置浏览器分辨率（窗口大小）
#         chrome_options.add_argument('log-level=3')
#         chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
#         chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
#         chrome_options.add_argument('--disable-javascript')  # 禁用javascript
#         chrome_options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
#         chrome_options.add_argument('–disable-software-rasterizer')
#         chrome_options.add_argument('--disable-extensions')
#         chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
#                                     f'/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
#         chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#         chrome_options.add_experimental_option('useAutomationExtension', False)
#         browser = webdriver.Chrome(options=chrome_options)
#         browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#             "source": """
#             Object.defineProperty(navigator, 'webdriver', {
#               get: () => undefined
#             })
#           """
#         })
#         #driver.maximize_window()
#         browser.get(request.url)
#         time.sleep(3)
#         text = browser.page_source
#         # print(text)
#         browser.quit()
#         # https://doc.scrapy.org/en/latest/topics/request-response.html
#         # 查看 HtmlResponse 对象结构
#         return HtmlResponse(url=request.url,encoding='utf-8',body=text,request=request)


