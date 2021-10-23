import click
from . import log_manager

module_name = __name__


@click.group(name="cmd2")
def command():
    pass


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@command.command()
# Name Your Options
@click.option("-s", "--sos")
# Basic Value Options
@click.option("--n", required=True, type=int)
# Multi Value Options
@click.option("--pos", nargs=2, type=float)
# Tuples as Multi Value Options
@click.option("--item", type=(str, int), default=("hola", 3))
# Multiple Options
@click.option("--message", "-m", multiple=True)
# Counting
@click.option("-v", "--verbose", count=True, default=0)
# Boolean Flags
@click.option("--shout/--no-shout", default=False)
# Choice Options
@click.option("--hash-type", type=click.Choice(["MD5", "SHA1"], case_sensitive=False))
# Prompting
@click.option("--name", prompt=True)
# Password Prompts
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
# Yes Parameters
@click.option(
    "--yes",
    is_flag=True,
    callback=abort_if_false,
    expose_value=False,
    prompt="Are you sure you want to drop the db?",
)
def cmd2_a(
    sos: str = None,
    n: int = 0,
    pos="",
    item=None,
    message=None,
    verbose=None,
    shout=None,
    hash_type=None,
    name=None,
    password=None,
):
    logger = log_manager.get_logger(module_name)
    logger.debug(f"Running cmd2_a {sos} {n} {pos}")
    click.echo("." * n)
    # click.echo("%s / %s" % pos)
    click.echo("name=%s id=%d" % item)
    click.echo("\n".join(message))
    click.echo("Verbosity: %s" % verbose)
    click.echo(hash_type)
    click.echo("Hello %s!" % name)


#    click.echo("Encrypting password to %s" % password.encode("rot13"))


@command.command()
def cmd2_b():
    logger = log_manager.get_logger(module_name)
    logger.debug("Running cmd2_b")
