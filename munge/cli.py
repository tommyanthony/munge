import click
from munge import converter
from munge.writer import OUTPUT
ALL_OUTPUTS = OUTPUT.keys()


@click.command(help="""
This utility converts data files from one types to another.
The sole argument data_type is the type of the desired output.
The options allow data to be read and written to files instead of the default
stdin and stdout.
""")
@click.argument('data_type', type=click.Choice(ALL_OUTPUTS))
@click.option('-i', '--in_file', type=click.File('rb'), default='-',
              help='File to read data from, default is stdin.')
@click.option('-o', '--out_file', type=click.File('wb'), default='-',
              help='File to write data to, default is stdout.')
def convert(data_type, in_file, out_file):
    converter.convert(data_type, in_file, out_file)
