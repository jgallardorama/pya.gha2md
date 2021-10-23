import click
import logging
from . import log_manager
import json


@click.command(name="json")
@click.option("-f", "--filepath")
def command(filepath):

    logger = log_manager.get_logger(__name__)
    logger.debug("Running Command json")

    with open(filepath) as json_file:
        data = json.load(json_file)

        sort_file = json.dumps(data, indent=4)
        print(sort_file)