import click
from munge import converter


"""
Current problems: csv, tsv importing
TODO
Add support for specifying import format
Come up with a name for my tablib
Add XML support
Move the logic out of the CLI interface
"""


@click.command()
@click.argument("data_type", type=click.Choice(converter.OUTPUT.keys()))
@click.option('-i', '--in_file', type=click.File('rb'), default="-")
@click.option('-o', '--out_file', type=click.File('wb'), default="-")
def convert(data_type, in_file, out_file):
    converter.convert(data_type, in_file, out_file)
