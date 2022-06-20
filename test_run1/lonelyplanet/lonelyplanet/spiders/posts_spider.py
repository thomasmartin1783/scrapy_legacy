import scrapy


class PostSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://www.hackerrank.com/blog/'
    ]

    def parse(self, response):
        for post in response.css('div.hr_post'):
            yield {
                'title': post.css('h3::text').get()
            }

        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # def parse(self, response):
    #     file_name = "posts.html"
    #     with open(file_name, 'wb') as file:
    #         file.write(response.body)
