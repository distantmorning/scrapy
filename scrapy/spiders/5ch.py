import scrapy
from test1.items import Test1Item, chItem


class tieba(scrapy.Spider):
    """
    name:scrapy唯一定位实例的属性，必须唯一
    allowed_domains：允许爬取的域名列表，不设置表示允许爬取所有
    start_urls：起始爬取列表
    start_requests：它就是从start_urls中读取链接，然后使用make_requests_from_url生成Request，
                    这就意味我们可以在start_requests方法中根据我们自己的需求往start_urls中写入
                    我们自定义的规律的链接
    parse：回调函数，处理response并返回处理后的数据和需要跟进的url
    log：打印日志信息
    closed：关闭spider
    """
    # 设置name
    name = "spider5ch"
    # 设定域名
    # allowed_domains = ["baidu.com"]
    # 填写爬取地址
    start_urls = [
        "https://matsuri.5ch.net/test/read.cgi/voiceactor/1577690567/",
    ]

    # 编写爬取方法
    def parse(self, response):
        # 初始化item对象保存爬取的信息
        item = chItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        item['title'] = response.xpath("//span[contains(text(),' 次スレ立てたよ')]/text()").extract()[1]
        item['link'] = response.xpath("//span[contains(text(),' 次スレ立てたよ')]/a/@href").extract()
        yield item
