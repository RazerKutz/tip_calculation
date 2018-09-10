import os


def load(name):
    """
    This method creates and loads partner data.
    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', name + '.prtnrs'))
    return filename


def add_entry(text, data):
    data.append(text)


def remove_entry(text, data):
    new_data = []
    for line in data:
        if text != line:
            new_data.append(line)
    return new_data
