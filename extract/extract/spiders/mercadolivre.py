import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino#D[A:tenis%20corrida%20masculino]"]


    # Atributos para paginação (Aqui define-se a quantidade de páginas que quer retornar)
    current_page = 1
    end_page = 10


    def parse(self, response):

        products = response.css('div.poly-card__content')

        for product in products:
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'title': product.css('h2.poly-component__title-wrapper a.poly-component__title::text').get(),
                'rating': product.css('div.poly-component__reviews span.poly-reviews__rating::text').get(),
                'total_reviews': product.css('div.poly-component__reviews span.poly-reviews__total::text').get(),
                'old_price': product.css('div.poly-component__price s.andes-money-amount.andes-money-amount--previous.andes-money-amount--cents-comma span.andes-money-amount__fraction::text').get(),
                'old_cents': product.css('div.poly-component__price s.andes-money-amount.andes-money-amount--previous.andes-money-amount--cents-comma span.andes-money-amount__cents::text').get(),
                'new_price': product.css('div.poly-component__price div.poly-price__current span.andes-money-amount__fraction::text').get(),
                'new_cents': product.css('div.poly-component__price div.poly-price__current span.andes-money-amount__cents.andes-money-amount__cents--superscript-24::text').get()
            }

        # Condição de paginação
        if self.current_page < self.end_page:

            self.current_page += 1
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a.andes-pagination__link::attr(href)').get()
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)
