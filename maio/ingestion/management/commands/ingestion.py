import os
import json
import redis
import time
import logging
from django.core.management.base import BaseCommand

logger = logging.getLogger('root')


class Command(BaseCommand):
    help = 'Ingest data'

    def get_message_from_edge(self, file_name: str) -> dict:
        """
        Returns data from super complex undocumented system. Consider it
        non mutable (you can rename it, move it, but don't change the contents).
        :return: json converted to dictionary
        """
        logger.info("File Processing started.")
        yield json.load(open(file_name))

    def store_message_in_database(self, timestamp: str, message: str) -> bool:
        """
        Stores given CSV string in the proprietary database. Consider it non mutable
        (you can rename it, move it, but don't change the contents).
        :param timestamp: Datetime in the format: "2020-01-21T09:32:34" as string
        :param message: CSV represented as string
        :return: boolean result of the call
        """
        logger.info("Store message in database.")
        time.sleep(0.5)
        r = redis.Redis()
        r.set(timestamp, message)

    def add_arguments(self, parser):
        """
        This adds argument to django command
        """
        parser.add_argument('json_file_name', type=str, help='Name of json file')

    def handle(self, *args, **kwargs):
        """
        This handles the whole command
        """
        if not os.path.exists(kwargs['json_file_name']):
            raise IOError(f"{kwargs['json_file_name']} file does not exists.")

        for message in self.get_message_from_edge(kwargs['json_file_name']):
            values = message["Values"]
            csv_message = "%s,%s,%s,%s,%s,%s" % (
                values["FACTORY"],
                values["ZONE"],
                values["CELL"],
                values["MACHINE_GROUP"],
                values["MACHINE"],
                values["MACHINE_ID"],
            )
            self.store_message_in_database(values["TIMESTAMP"], csv_message)
        logger.info("Process finished successfully.")
