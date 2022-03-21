# Scrapy settings for test1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'test1'

SPIDER_MODULES = ['test1.spiders']
NEWSPIDER_MODULE = 'test1.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'test1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
'cookie': 'acw_tc=0bdd346a16470998056824718e01a1e0667563651cacea778ae2e4fee9e8b3; lastCity=101010100; sid=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1647099806; __zp_seo_uuid__=afa47b28-3bfb-49ca-95f6-8e8f31d16101; __g=sem_pz_bdpc_dasou_title; __l=r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Furl%3D000000jr2Ikf9sSJf_8IwGOY9v3s69Oc2TGH2ueHiHN4KGWFGGFHMTmX2lV_DUh7Gt3Tp5nPiPHfJjQUGEft5MVlxFK6t1wRVYGZj_cTTvALv1Q0D7Gb9_0_J6jSzqydO2G8lubZqDI8YMp0Hs1ADzFl-S2Tvmqbne3PHmKsLzVGLw6n7KyspKh72BQL61X522tlAH1V19izOC4ibEUmYePYDK8T.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqmhq1Tqpkko60ThPv5HD0IgF_gv-b5HDdn1ndnHD1P1m0UgNxpyfqnHfvnW0znHn0UNqGujYknHnkPWfvr0KVIZK_gv-b5HDznWT10ZKvgv-b5H00pywW5R9awfKspyfqnfKWpyfqn0KWThnqnWT3rHb%26ck%3D6012.2.79.316.189.354.184.172%26dt%3D1647099803%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26tpl%3Dtpl_12273_25897_22126%26l%3D1533511376%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C%2525E7%25259B%2525B4%2525E6%25258E%2525A5%2525E8%2525B0%252588%2525EF%2525BC%252581%2526linkType%253D&l=%2Fwww.zhipin.com%2Fjob_detail%2F7b0119a9b872b5c80Xx93Nm0E1Q~.html&s=3&g=%2Fwww.zhipin.com%2Fbeijing%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; __c=1647099806; __a=81015083.1647099806..1647099806.11.1.11.11; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1647100044; __zp_stoken__=f71cdC3MTPRBPJgkZHwN9JQEQYFMMGwMiKToVAQQfICoraRIPISh1EX95Rxpxall1QV0HGHogCgxEb09Ab3hQeSk7WW5yGT1XF3Y6D1QNXyIEOkJYBQJoVkVEXg1cWQQ%2FA2Q1bGAACwV4IR0%3D',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'

}
SELENIUM_TIMEOUT = 30

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'test1.middlewares.Test1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'test1.middlewares.Test1DownloaderMiddleware': 543,
   # 'test1.middlewares.SeleniumMiddleware': 300,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# LOG_FILE = './demo.log'
# LOG_LEVEL = 'ERROR'
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'test1.pipelines.Test1Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
