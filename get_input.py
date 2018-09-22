import file_manager


def input_partners_manual(data):
    """
    This is used if there is no partners.prtnrs file.
    :param data: Empty list. User will populate this and then it will be saved back to partners.prtnrs.
    :return: list of partners to be used elsewhere
    """
    count = input('Number of partners: ')

    print(type(int(count)), ' ' + count)
    for x in range(0, int(count)):
        partner = {'name': '', 'hours': 0, 'tips': 0}
        partner['index'] = x
        partner['name'] = input('Partner Name: ')
        data.append(partner)
    file_manager.save('partners', data)
    return list


def input_hours(data, debug):
    # TODO Make it so the user can edit specific user data.
    """
    Gets the hours the each partners worked.
    :param data: A list of dictionaries that store the user data
    :return: Returns a list of hours.
    """
    print('Please input the hours worked for each partner.\n'
          ' (Enter a -1 to cancel.)')
    hours = []
    if debug is True:
        h = [17.45, 8.30, 13.20, 4.05, 29.45, 14.15, 34.65, 31.65, 24.20, 13.65, 24.05, 36.45, 19.65, 23.30, 9.55,
             12.85,
             22.95, 8.35, 8.15, 14.70]
        for val, x in enumerate(data):
            x['hours'] = h[val]

    elif file_manager.temp_file_check() is True:

        if input('Use data already entered (T,F): ').lower() == 't':
            data = file_manager.load('partners_temp')
            # print(data)
        else:
            for x in data:
                while True:
                    try:

                        cmd = float(input(x['name'] + ': '))
                        break
                    except ValueError:
                        print("you must enter an integer")
                if float(cmd) < 0:
                    return None
                else:
                    x['hours'] = float(cmd)

    else:
        for x in data:
            while True:
                try:

                    cmd = float(input(x['name'] + ': '))
                    break
                except ValueError:
                    print("you must enter an integer")
            if float(cmd) < 0:
                return None
            else:
                x['hours'] = float(cmd)
            """
            cmd = input(data[x] + ': ')
            if cmd.lower() == 'q':
                return None
            else:
                hours.append(float(cmd))
            """
        file_manager.save_temp(data)
    return data
