from io import TextIOWrapper

"""
This module handles all writing of the output.
The write(data, data_type) method is called by converter.py to write
the data to the desired output source
"""


def write_text(destination, text, end=''):
    with TextIOWrapper(destination) as out:
        print(text, file=out, end=end)

# json and html library don't append a newline at the end
write_string = lambda destination, text: write_text(destination, text, '\n')

# used to write xls and xlsx files
write_bytes = lambda destination, data: destination.write(data)

# Method to output the data for each type
OUTPUT = {'json': write_string,
          'html': write_string,
          'yaml': write_text,
          'csv':  write_text,
          'tsv':  write_text,
          'xls':  write_bytes,
          'xlsx': write_bytes}


def write(data, data_type, destination):
    data_writer = OUTPUT[data_type]
    data_writer(destination, getattr(data, data_type))
