import click
import logging

from .version import __version__

from . import command1
from . import command2
from .config import ConfigManager
from . import log_manager

from .other_commands import command3
from . import cmd_json, cmd_xml, cmd_yaml, cmd_csv


@click.group()
@click.version_option(__version__)
@click.option("--option1", help="Help option 1")
@click.option("--option2", type=click.Choice(["OPTION1", "OPTION2", ""]))
@click.option("--option3", help="Help option 2")
@click.option("-v", "--verbose", count=True, default=0)
@click.option("-c", "--configfile", default="")
def main_command(
    verbose: int,
    configfile: str = "",
    option1: str = "",
    option2: str = "",
    option3: str = "",
):
    cm = ConfigManager()
    cm.verbose = verbose
    logger = log_manager.init_log(__name__)
    logger.info(f"verbose {verbose}")

    if configfile != "":
        cm.load(configfile)


main_command.add_command(command1.command)
main_command.add_command(command2.command)
main_command.add_command(command3.command)
main_command.add_command(cmd_xml.command)
main_command.add_command(cmd_yaml.command)
main_command.add_command(cmd_json.command)
main_command.add_command(cmd_csv.command)


def start():
    main_command()


if __name__ == "__main__":
    start()