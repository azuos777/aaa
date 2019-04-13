import scrapy ##Importa o framework e as bibliotecas de Web Crawling Scrapy
from ..items import ProdutoItem ##Importa a Classe de armazenamento de dados dos Produtos do arquivo Items.py

class ProdSpider(scrapy.Spider): ## Cria a a classe da aranha principal que coleta os dados dos produtos
    name = 'prodspider' ## Nome da aranha
    page = 24 ## Paginação utilizado para seguir as paginas de produtos
    start_urls = ['https://www.shoptime.com.br/categoria/eletronicos/tv/smart-tv?limite=24&offset=0'] ## Url Inicial na coleta dos dados
    
    def parse(self, response): ##Metodo que pega os links dos produtos
        produtos = response.css ('a.card-product-url')
        for p in produtos: ##Loop Principal
            linkprod = p.css('::attr(href)').get()
            item = ProdutoItem()
            item['linkprod'] = response.urljoin(linkprod)
            print (linkprod)
            rame = scrapy.Request(url=response.urljoin(linkprod), callback=self.parseAme) ##após o methodo parseAme,grava os dados do ame e seguue para o proximo produto
            rame.meta['item'] = item
            yield rame ## grava
        nextPageLink = 'https://www.shoptime.com.br/categoria/eletronicos/tv/smart-tv?limite=24&offset='+ str(ProdSpider.page) ##Avança entre as paginas
        if ProdSpider.page < 48: ##numero de produtos que ele irá rastrear
            ProdSpider.page += 24
            yield response.follow(nextPageLink, callback=self.parse) ## pula para a proxima pagina e reinicia o loop

    def parseAme(self,response): ## Methodo que pega os valores do ame
        item = response.meta['item']
        valorame = response.css ('span.hMwkMY')[0].get()
        valorame = valorame.split() ##Quebra o texo
        #item['valorame'] = valorame[7] + ' ' + valorame[8]
        item['valorame'] = 'Este produto tem: ' + valorame[8] + ' de Cash-Back !' ## Seleciona a % de ame
        print(valorame)
        yield item ##Grava todos os dados obtidos.