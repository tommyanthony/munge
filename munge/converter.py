import tablib
from io import TextIOWrapper


def read_bytes(in_file):
    return in_file.read()


def read_text(in_file):
    return in_file.read().decode()


def write_text(output, text, end=""):
    with TextIOWrapper(output) as out:
        print(text, file=out, end=end)

# json library doesn't append a newline at the end, so we will
write_json = lambda output, text: write_text(output, text, "\n")


def write_bytes(output, data):
    output.write(data)

# Method to output the data for each type
OUTPUT = {"json": write_json,
          "html": write_text,
          "yaml": write_text,
          "csv":  write_text,
          "tsv":  write_text,
          "xls":  write_bytes,
          "xlsx": write_bytes}


def convert(data_type, in_file, out_file):
    data = read_bytes(in_file)
    data_set = tablib.import_set(data)
    writer = OUTPUT[data_type]

    # dynamically get the data type we want. ex: getattr(data_set, "html")
    writer(out_file, getattr(data_set, data_type))
