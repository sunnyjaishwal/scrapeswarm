# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapeswarmPipeline:
    def process_item(self, item, spider):
        return item

import sqlite3

class SQLitePipeline:

    def open_spider(self, spider):
        # Open the SQLite3 database connection
        self.connection = sqlite3.connect('scrapy_data.db')
        self.cursor = self.connection.cursor()
        
        # Create a table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scraped_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT
            )
        ''')

    def close_spider(self, spider):
        # Close the SQLite3 database connection
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        # Insert scraped data into the database
        self.cursor.execute('''
            INSERT INTO scraped_data (title) VALUES (?)
        ''', (item['title'],))
        return item
