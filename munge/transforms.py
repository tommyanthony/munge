import inspect
import sys
import os

major_py_version = sys.version_info.major
"""
load_module is dependent on python version
http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
"""
if major_py_version == 3:
    from importlib.machinery import SourceFileLoader

    def load_module(module_name, file_path):
        return SourceFileLoader(module_name, file_path).load_module()
elif major_py_version == 2:
    import imp
    load_module = imp.load_source  # load_module function is imp.load_source
else:
    raise Exception("unknown python version")


def module_from_file(file_path):
    # FIXME we're assuming the file name and the module name are the same
    # are they always the same?
    file_name = os.path.splitext(os.path.basename(file_path))
    return load_module(file_name, file_path)


def find_transforms(module):
    def is_defined_function(func):
        return inspect.isfunction(func) and inspect.getmodule(func) == module
    for func_metadata in inspect.getmembers(module, is_defined_function):
        if func_metadata[0].startswith("transform"):
            yield func_metadata[1]


def load_transforms(file_path):
    return find_transforms(module_from_file(file_path))


def run_transforms(transforms, datasets):
    pass


def transform(file_path, datasets):
    transforms = load_transforms(file_path)
    return run_transforms(transforms, datasets)
