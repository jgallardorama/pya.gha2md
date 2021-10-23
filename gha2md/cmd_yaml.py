import click
import logging
from . import log_manager
import yaml


@click.command(name="yml")
@click.option("-f", "--filepath")
def command(filepath):

    logger = log_manager.get_logger(__name__)
    logger.debug("Running Command yaml")

    fruits_list = None

    with open(filepath) as f:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(f, Loader=yaml.FullLoader)
        print(fruits_list)

    sort_file = yaml.dump(fruits_list, sort_keys=True)
    print(sort_file)