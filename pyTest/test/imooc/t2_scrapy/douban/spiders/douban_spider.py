# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.response.html import HtmlResponse as xHtmlResposne
class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名,不能和项目名重复
    name = 'douban_spider'
    #  不再这个列表里的域名不被抓取
    allowed_domains = ['movie.douban.com']
    # 入口url, 传进调度器里面去.
    start_urls = ['https://movie.douban.com/top250']

    def gethtmlresponse(self,response)-> xHtmlResposne:
        isinstance(response,scrapy.http.response.html.HtmlResponse)
        return response

    def parse(self, response):
        if response and isinstance(response,scrapy.http.response.html.HtmlResponse):
            # response=self.gethtmlresponse(response)
            # response的类型 <class 'scrapy.http.response.html.HtmlResponse'>
            # response内容: <200 https://movie.douban.com/top250>

            print("response的类型",type(response))
            print("response内容:",response)
            print("responseText:",response.text)

        pass
