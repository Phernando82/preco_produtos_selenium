# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
# jhonatan


def tirar_espaco_em_branco(valor):
    return valor.strip()


def processar_carateres_especiais(valor):
    return valor.replace(u"\u201c", '').replace(u"\u201d", '').replace(u"\u2014", '—')


class CitacaoItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor=MapCompose(
            tirar_espaco_em_branco, processar_carateres_especiais),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(',')
    )


def remover_aspas(valor):
    return valor.replace(u"\u2019", '')


def tornar_maisuculo(valor):
    return valor.upper()


class CitacaoGoodReadsItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, remover_aspas),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, tornar_maisuculo),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(';'),
    )
