import click
import logging
from gha2md.appinfra import applogging
from gha2md.process import docbuilder, scanner, parser


@click.command(name="build")
@click.option("-s", "--source-dir", "source_dir", required=True)
def command(source_dir):
    logger = applogging.LogManager().get_logger(__name__)

    logger.info("Running Scan")
    action_dirs = scanner.scan(source_dir)

    logger.info("Running Scan")
    doc_items = parser.parse(action_dirs)

    logger.info("Running Build")
    for doc_item in doc_items:
        logger.info(f"build documentation {doc_item.source_dir}")
        docbuilder.build(doc_item, source_dir)

    