import os
import click

import yaml

from gha2md.appinfra.applogging import LogManager

from .version import __version__

from gha2md.commands import cmd_build 
from gha2md.appinfra import appconfig


@click.group()
@click.version_option(__version__)
# TOREMOVE
# @click.option("--option1", help="Help option 1")
# @click.option("--option2", type=click.Choice(["OPTION1", "OPTION2", ""]))
# @click.option("--option3", help="Help option 2")
@click.option("-v", "--verbose", count=True, default=0)
@click.option("-n", "--no-color", "no_color", is_flag=True,
              default=False, help="Disables terminal formatting sequences in the output. ")
@click.option("-c", "--configfile", default="")
@click.option("--config-item", "config_items", type=click.Tuple([str, str]), multiple=True)
def main_command(
    verbose: int,
    config_items,
    no_color,
    configfile: str = ""
):
    cm = appconfig.ConfigManager()
    cm.set_config_value("verbose", verbose)
    cm.set_config_value("no_color", no_color)

    lm = LogManager()
    lm.clear()
    logger = lm.get_logger(__name__)
    logger.info(f"verbose {verbose}")

    if configfile and os.path.isfile(configfile):
        logger.info(f"Load configuration {configfile}")
        cm.load(configfile)

    if config_items:
        for key, value in list(config_items):
            if key:
                cm.set_config_value(key, value)

    config_dump_string = yaml.safe_dump(cm.config)
    logger.debug(f"Configuration loaded\n{config_dump_string}")


main_command.add_command(cmd_build.command)

# TOREMOVE
# main_command.add_command(command2.command)
# main_command.add_command(command3.command)
# main_command.add_command(cmd_xml.command)
# main_command.add_command(cmd_yaml.command)
# main_command.add_command(cmd_json.command)
# main_command.add_command(cmd_csv.command)


def start():
    main_command()


if __name__ == "__main__":
    start()