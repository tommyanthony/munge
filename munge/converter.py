from tablib.formats import available

from munge.reader import read
from munge.writer import write

SUPPORTED = [format.title for format in available]
INPUT_FORMATS = {
    format.title: format.import_set
    for format in available if hasattr(format, "import_set")
}
INPUT_TYPES = INPUT_FORMATS.keys()


def convert(data_type, in_file, out_file):
    data_set = read(in_file)
    if data_set:
        # dynamically get the data type we want. ex: getattr(data_set, 'html')
        write(data_set, data_type, out_file)
    else:
        raise TypeError(
            "Could not detect input data type.\n"
            "Ensure the data provided from '%s' is of type: %s."
            % (in_file.name, ', '.join(INPUT_TYPES))
        )
