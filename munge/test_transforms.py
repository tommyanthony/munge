def transform_text(one, two, three):
    return one + 1, two, three


def transform_numbers(one, two, three):
    return one, two, three + two


def transform_test(one, two, three):
    return one, two, three


def transform_new_format(table1, table2, table3):
    """
    Each table is a dictionary of {
        row_title: value
    }
    """
    if table1["name"] == table2["name"] == table3["name"]:
        table1.update(table2)
        table1.update(table3)
        return table1


def run_transforms(transforms, row):
    kwargs = row
    for transform in transforms:
        result = transform(**kwargs)
        kwargs = {"one": result[0], "two": result[1], "three": result[2]}
        print(kwargs)
    return kwargs
