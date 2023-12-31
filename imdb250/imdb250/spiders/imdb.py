import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv-250"]

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                'titulo': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo::text').get(),
                'nota': response.css('strong::text').get()
            }

    pass
