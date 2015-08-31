import tablib
from io import TextIOWrapper
from tablib.formats import available

SUPPORTED = [format.title for format in available]
INPUT_FORMATS = {
    format.title: format.import_set
    for format in available if hasattr(format, "import_set")
}
INPUT_TYPES = INPUT_FORMATS.keys()


def read_bytes(in_file):
    return in_file.read()


def write_text(output, text, end=''):
    with TextIOWrapper(output) as out:
        print(text, file=out, end=end)

# json and html library don't append a newline at the end
write_string = lambda output, text: write_text(output, text, '\n')


def write_bytes(output, data):
    output.write(data)

# Method to output the data for each type
OUTPUT = {'json': write_string,
          'html': write_string,
          'yaml': write_text,
          'csv':  write_text,
          'tsv':  write_text,
          'xls':  write_bytes,
          'xlsx': write_bytes}


READER_TYPES = [lambda data: data,  # change nothing, read as binary data
                lambda data: data.decode()]  # decode data for txt documents


def convert(data_type, in_file, out_file):
    data = read_bytes(in_file)
    for reader in READER_TYPES:
        # try each reader until we find a way to import data
        data_set = tablib.import_set(reader(data))
        if data_set:
            break

    if data_set:
        # get the correct function to write the output data
        writer = OUTPUT[data_type]

        # dynamically get the data type we want. ex: getattr(data_set, 'html')
        writer(out_file, getattr(data_set, data_type))
    else:
        raise TypeError(
            "Could not detect input data type.\n"
            "Ensure the data provided from '%s' is of type: %s."
            % (in_file.name, ', '.join(INPUT_TYPES))
        )
