import logging
from scrapy import signals
from itemadapter import is_item, ItemAdapter


class ScrapeSwarmSpiderMiddleware:
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
        # for i in range(0, 10):
        #     print('process_spider_input', i)

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
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapeSwarmDownloaderMiddleware:
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
        print("Body: ", request.body)
        print("Callback: ", request.callback)
        print("cb_kwargs: ", request.cb_kwargs)
        print("cookies: ", request.cookies)
        print("copy: ", request.copy)
        print("dont_filter: ", request.dont_filter)
        print("Encoding: ", request.encoding)
        print("Errorback: ", request.errback)
        print("Flags: ", request.flags)
        print("Headers: ", request.headers['User-Agent'])
        print("from_curl: ", request.from_curl)
        print("Meta : ", request.meta)
        print("Method: ", request.method)
        print("Priority: ", request.priority)
        print("Replace: ", request.replace)
        print("to_dict: ", request.__dict__)
        print("URL; ", request.url)

        # setup broswer agent, headers, cookies, meta, 
        # user_agent, browser-plugin, installed-fonts, 
        # screen-size, time-zone, language, IP address,
        # canvas fingerprint, webGL fingerprint,audio fingerprint,
        # media devices, battery status, http headers, 
        # mouse movements, keystrokes, javascripts variables 
        # 
        # 

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
