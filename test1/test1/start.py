from scrapy.cmdline import execute


if __name__ == '__main__':
    execute(["scrapy", "crawl", "te"])
    # execute(["scrapy", "crawl", "DAV",'-o','a.csv'])