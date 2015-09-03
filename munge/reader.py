import tablib

def read_bytes(in_file):
    return in_file.read()

READER_TYPES = [lambda data: data,  # change nothing, read as binary data
                lambda data: data.decode()]  # decode data for txt documents


def read(in_file):
    """
    Returns a tablib.dataset object if it can be created from the data
    Otherwise returns None
    """
    data = read_bytes(in_file)
    for reader in READER_TYPES:
        # try each reader until we find a way to import data
        data_set = tablib.import_set(reader(data))
        if data_set:
            return data_set
