import click
from .. import log_manager


@click.group(name="cmd3")
def command():
    pass


@command.command()
def cmd3_a():
    logger = log_manager.get_logger(__name__)
    logger.debug("Running cmd3_a")


@command.command()
def cmd3_b():
    logger = log_manager.get_logger(__name__)
    logger.debug("Running cmd3_b")
