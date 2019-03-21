# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.response.html import HtmlResponse as xHtmlResposne
from pyTest.test.imooc.t2_scrapy.douban.items import DoubanItem
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
            # print("response内容:",response)
            # print("responseText:",response.text)
            # 绝对路径.
            xpath_movieList_abs="/html/body/div[3]/div[1]/div/div[1]/ol/li"
            # 相对路径
            xpath_movieList_rel="//ol[@class='grid_view']//li"
            xpath_movieId="/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[1]/em"
            xpath_movieName="/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]"
            movieList=response.xpath(xpath_movieList_abs)
            movieList_real=response.xpath(xpath_movieList_rel)
            movieid=response.xpath(xpath_movieId)
            movieName=response.xpath(xpath_movieName)
            print(movieid,movieName)

            for itemMovie in movieList:
                # itemMovie,变量无法智能提示了.
                douban_item=DoubanItem()
                # douban_item['movieId'] = itemMovie.xpath("./div/div/em")
                itempic=itemMovie.xpath("./div[@class='item']/div[@class='pic']")
                itemInfo=itemMovie.xpath("./div[@class='item']/div[@class='info']")
                douban_item['movieId'] = itempic.xpath("./em/text()").get()
                douban_item['movieName'] = itemInfo.xpath("./div/a/span").get()
                douban_item['movieLink'] = itemInfo.xpath("./div/a/@href").get()
                picaddress=itempic.xpath("./a")
                print(id,picaddress)
                yield itemMovie


# 豆瓣xpath:
#  movie-id : /html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[1]/em
#  movie-name: /html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]  最后一个span数组是电影的多个名称.
#
