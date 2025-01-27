import pytest
from scrapy.http import HtmlResponse
from ScrapeSwarm.spiders.httpbin.httpbin_spider import HttpBinSpider

@pytest.fixture
def response():
    url = 'https://httpbin.org/'
    body = '<html><body><h1>Test Page</h1></body></html>'
    return HtmlResponse(url=url, body=body, encoding='utf-8')

@pytest.fixture

def spider():
    return HttpBinSpider()

def test_parse(response, spider):
    result = list(spider.parse(response))
    assert len(result) == 1
    assert result[0].xpath('//h1/text()').get() == 'Test Page'

def test_spider_name(spider):
    assert spider.name == 'httpbin'

def test_start_requests(spider):
    start_urls = spider.start_urls
    assert len(start_urls) == 1
    assert start_urls[0] == 'https://httpbin.org/'

def test_parse_item(response, spider):
    result = list(spider.parse(response))
    assert len(result) == 1
    item = result[0]
    assert 'Test Page' in item.get('title')