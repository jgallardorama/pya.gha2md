import click
import logging
from . import log_manager


@click.command(name="cmd1")
def command():
    logger = log_manager.get_logger(__name__)
    logger.debug("Running Command 1")
