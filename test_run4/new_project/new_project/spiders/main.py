import imp
from os import link
import scrapy
# from .link import links
# from .links_6_books import links_books
# links = links_books
from .links_7_lifestyle import links_lifestyle
links = links_lifestyle


class PostSpider(scrapy.Spider):
    name = "comments"
    start_urls = [
        # "https://trickbd.com/uncategorized/744566#comments"
        "https://trickbd.com/lifestyle/783981#comments"
    ]

    global inc
    inc = 0

    global links

    def parse(self, response):
        global inc
        for post in response.css('ol.commentlist li'):
            a = post.css('.trickbd-comment-content::text').get()
            with open("comments_7_lifestyle.csv", 'ab') as file:
                foo = f"\"{a}\",\n"
                file.write(foo.encode('utf8'))

        inc = inc + 1
        # if inc < len(links):
        if(inc % 10 == 0):
            print("="*50, inc, "="*50)
        if inc < len(links):
            next_page = links[inc]
            print(next_page)
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
