import click
import logging
from . import log_manager
from xml.etree import ElementTree
from xml.dom import minidom


@click.command(name="xml")
@click.option("-f", "--filepath")
def command(filepath):
    logger = log_manager.get_logger(__name__)
    logger.debug("XML")

    with open(filepath, "rt") as f:
        tree = ElementTree.parse(f)

    print(tree)

    root = tree.getroot()
    rough_string = ElementTree.tostring(root, "utf-8")
    reparsed = minidom.parseString(rough_string)

    print(reparsed.toprettyxml(indent="  "))
