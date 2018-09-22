"""

"""
import json
import os


def load(name):
    """
    This method creates and loads partner data.
    :param name: This base name of the partnerfile to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            # for entry in fin.readlines():
            #     data.append(entry.rstrip())
            data = json.load(fin)

    return data


def save(name, data):
    """
    Saves the data to the file "name"
    :param name: Name of the file to save to.
    :param data: the data you want to save to the file.
    :return: -
    """
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        # for entry in data:
        # fout.write(entry)
        json.dump(data, fout)


def save_temp(data):
    """
    Saves the data to the file "name"
    :param name: Name of the file to save to.
    :param data: the data you want to save to the file.
    :return: -
    """
    filename = get_full_pathname('partners_temp')
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        # for entry in data:
        # fout.write(entry)
        json.dump(data, fout)


def remove_temp():
    filename = get_full_pathname('partners_temp')
    os.remove(filename)


def temp_file_check():
    filename = get_full_pathname('partners_temp')
    if os.path.isfile(filename):
        return True
    else:
        return False


def get_full_pathname(name):
    """
    gets the full path of the file
    :param name: the file name
    :return: file path
    """
    filename = os.path.abspath(os.path.join('.', name + '.prtnrs'))
    return filename


def add_entry(data, format):
    """
    adds a name to the list
    :param name: the name to be added.
    :param data: the list to add the name to.
    :return: -
    """
    data.insert(format['index'], format)


def remove_entry(num, data):
    """
    removes a specified index from data
    :param num: the index to remove
    :param data: the list to remove the index from
    :return:
    """
    del data[num]
    for x in data:
        if x['index'] > num:
            x['index'] = x['index'] - 1
    return data
