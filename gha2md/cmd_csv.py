import click
import logging
from . import log_manager
import csv
import io


@click.command(name="csv")
@click.option("-f", "--filepath")
def command(filepath):

    # RAW
    logger = log_manager.get_logger(__name__)
    logger.debug("Running Command csv")
    si = io.StringIO()
    cw = csv.writer(si)
    data = None
    with open(filepath, "r") as f:
        data = csv.reader(f, delimiter=";")

        for row in data:
            print(row)
            cw.writerow(row)

        print(si.getvalue().strip("\r\n"))

    # Dictionary
    si = io.StringIO()
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(si, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"first_name": "Baked", "last_name": "Beans"})
    writer.writerow({"first_name": "Lovely", "last_name": "Spam"})
    writer.writerow({"first_name": "Wonderful", "last_name": "Spam"})

    content = si.getvalue().strip("\r\n")
    print(content)

    reader = csv.DictReader(si)
    for row in reader:
        print(row["first_name"], row["last_name"])
