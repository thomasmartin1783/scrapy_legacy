from re import I
from xml.etree.ElementInclude import include
import scrapy


class PostSpider(scrapy.Spider):
    name = "comments"

    start_urls = [
        # 'https://trickbd.com/category/android-custom-rom,android-phone-review,android-root,android-tips,android-xposed-framework,apps-review/page/71'
        # 'https://trickbd.com/category/pdf-books'
        'https://trickbd.com/category/lifestyle'
    ]

    global uri
    # uri = 'https://trickbd.com/category/android-custom-rom,android-phone-review,android-root,android-tips,android-xposed-framework,apps-review/page/'
    # uri = 'https://trickbd.com/category/pdf-books/page/'
    uri = 'https://trickbd.com/category/lifestyle/page/'
    global url_s
    url_s = []
    global inc
    inc = 0

    def parse(self, response):
        url_s = []
        for link in response.css('div.featured_post .box'):
            link = link.css('li a').getall()[-3].split('"')[1]
            url_s.append(link)

        for link in url_s:
            print(link)
        next_ref = response.css('a.next').attrib['href'].split('=')[-1]
        print("#"*100)
        print(next_ref)

        file_name = "links_7_lifestyle.csv"
        with open(file_name, 'a') as file:
            for i in url_s:
                file.write(f"\"{i}\",\n")

        # print(next_page)
        if next_ref is not None:
            next_page = uri + next_ref
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
