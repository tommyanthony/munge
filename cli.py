import click
import tablib
from io import TextIOWrapper


def read_bytes(in_file):
    return in_file.read()


def read_text(in_file):
    return in_file.read().decode()


def write_text(output, text, end=""):
    with TextIOWrapper(output) as out:
        print(text, file=out, end=end)

# JSON Writer doesn't append a newline at the end
write_json = lambda output, text: write_text(output, text, "\n")


def write_bytes(output, b):
    output.write(b)

"""
Current problems: csv, tsv importing
TODO
Add support for specifying import format
Come up with a name for my tablib
Add XML support
Move the logic out of the CLI interface
"""

OUTPUT = {"json": write_json,
          "html": write_text,
          "yaml": write_text,
          "csv":  write_text,
          "tsv":  write_text,
          "xlsx": write_bytes,
          "xlsx": write_bytes}


@click.command()
@click.argument("out_type", type=click.Choice(OUTPUT.keys()))
@click.option('--in_file', type=click.File('rb'), default="-")
@click.option('--out_file', type=click.File('wb'), default="-")
def convert(out_type, in_file, out_file):
    stuff = read_bytes(in_file)
    data = tablib.import_set(stuff)
    writer = OUTPUT[out_type]
    writer(out_file, getattr(data, out_type))
