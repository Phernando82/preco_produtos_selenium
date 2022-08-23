# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class SQLitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect('proxies.db')
        self.cursor = self.connection.cursor()
        # Why do we create the db here?(because we want to create the db if it doesnt exist yet for that spider)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS proxies(
                ip_adress TEXT NOT NULL PRIMARY KEY,
                port NUMBER,
                code TEXT,
                country TEXT,
                anonimity TEXT,
                google TEXT,
                https TEXT,
                last_checked TEXT
            )
        """)

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        # talk about having to have both item names having the same name, so that means we gotta change the yield command(change to new names)
        self.cursor.execute("""
            INSERT OR IGNORE INTO proxies (ip_adress, port, code, country, anonimity, google, https, last_checked) values (?,?,?,?,?,?,?,?)
        """, (
            item.get('ip_adress'),
            item.get('port'),
            item.get('code'),
            item.get('country'),
            item.get('anonimity'),
            item.get('google'),
            item.get('https'),
            item.get('last_checked'),
        ))
        self.connection.commit()
        return item
