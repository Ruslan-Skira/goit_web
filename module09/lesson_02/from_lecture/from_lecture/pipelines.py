# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import datetime

class FromLecturePipeline:
    def process_item(self, item, spider):
        return item

class AddScrapedDatePipeline:
    def process_item(self, item, spider):
        current_utc_datetime = datetime.datetime.utcnow()
        item['scraped_date'] = current_utc_datetime.isoformat()
        return item
