import file_manager

debug = True


def main():
    """
    Starts the program
    :return: -
    """
    partner = {'index': 0, 'name': '', 'hours': 0, 'tips': 0}

    partner_data = []
    print_header()
    # partner_data['partner'] = file_manager.load('partners')
    partner_list = file_manager.load('partners')
    for idx, x in enumerate(partner_list):
        partner = x
        partner_data.append(partner)
    if partner_data.__len__() == 0:
        # broken as of now.
        input_partners_manual(partner_data)
    if debug is True:
        print(partner_data)
    # init_index(partner_data)
    run_loop(partner_data)


def run_loop(data):
    """
    Main loop for getting the user's tip information
    :param data: The list of partners at the store
    :return: -
    """

    while True:
        cmd = input('[E]nter tip data, [R]emove Partners, [A]dd partners, [L]ist, or [Q]uit : ').lower()
        if cmd == 'e':
            sum_hours = 0
            # if the user enters -1 then the program closes nicely
            data = input_hours(data)
            if data is None:
                print('No data entered.')
                continue
            # print(data)
            # TODO Fix so that it handles unexpected results.
            total_money = float(input('Total tips: '))
            for x in data:
                sum_hours += x['hours']

            tips_per_hour = calc_tph(sum_hours, total_money)
            tips_per_hour = float("%.3f" % tips_per_hour)
            print(tips_per_hour)
            calc_idph(tips_per_hour, data)

            tip_total_under = calc_under(data)
            od = sort_dec(data)
            final_list = distribute_under(od, total_money, tip_total_under)

            if debug is True:
                checksum = 0
                for s in data:
                    checksum += int(s['tips'])
                print(checksum)
            final_list = sort_by_index(final_list)
            # pretty_print(final_list)
            pretty_print_plus(final_list, tips_per_hour)

        elif cmd == 'r':
            for idx, x in enumerate(data):
                print(idx + 1, x)
            print(
                'Please enter the name of the partner you need to remove\n'
                ' (Enter a -1 to cancel.)\n')

            while True:
                try:
                    cmd = int(input('Index: '))
                    if cmd < 0:
                        file_manager.save('partners', data)
                        break
                    else:
                        data = file_manager.remove_entry(cmd - 1, data)
                except ValueError:
                    print("you must enter an integer")

        elif cmd == 'a':
            new_partner = 'Empty'
            partner = {'name': '', 'hours': 0, 'tips': 0}
            print('Please enter the name of the new partner\n'
                  ' (type "print" to see current list)\n'
                  ' (type "done" when finished)')
            while new_partner != 'done' or new_partner != 'd':
                new_partner = input('Input: ')
                if new_partner == 'done' or new_partner == 'd' or new_partner == '-1':
                    file_manager.save('partners', data)
                    break
                elif new_partner == 'p' or new_partner == 'print':
                    for x in data:
                        print(x)
                    print('')
                else:
                    file_manager.add_entry(new_partner, data, partner)
        elif cmd == 'l':
            pretty_print(data)
        elif cmd == "q":
            print('quitting program.')
            if file_manager.temp_file_check() is True:
                file_manager.remove_temp()
            break
        else:
            print("oops that's not a command. Please try again.")
        print()


# This is if there is no file for the partners
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


def input_hours(data):
    # TODO Make it so the user can edit specific user data.
    """
    Gets the hours the each partners worked.
    :param data: A list of dictionaries that store the user data
    :return: Returns a list of hours.
    """
    h = [17.45, 8.30, 13.20, 4.05, 29.45, 14.15, 34.65, 31.65, 24.20, 13.65, 24.05, 36.45, 19.65, 23.30, 9.55, 12.85,
         22.95, 8.35, 8.15, 14.70]
    print('Please input the hours worked for each partner.'
          ' (Enter a -1 to cancel.)')
    hours = []
    if debug is True:
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


def calc_tph(total_hours, tip_amount):
    """
    This calculates tips per hour
    :param total_hours: The sum of the numbers entered by the user.
    :param tip_amount:  Total sum of money counted by the user.
    :return: amount or tips divided by the total hours worked.
    """
    return tip_amount / total_hours


# def calc_idph(tph, dictionary):
def calc_idph(tph, data):
    """
    Calculates each partners total tips.
    :param tph: The value calculated by calc_tph.
    :param data: A list of dictionaries that store the user data
    :return: Dictionary with partner name : total tips for the week
    """

    for x in data:
        # x['tips'] = "%.2f" % x['hours'] * tph
        x['tips'] = float("%.2f" % (x['hours'] * tph))
    # return data


def calc_under(data):
    """
    this sums the "total tips for week" for each partner with out the decimal value.
    :param data: A list of dictionaries that store the user data
    :return: Sum of the total tips with out decimals.
    """
    sum_tips = 0
    for x in data:
        sum_tips += int(x['tips'])

    return sum_tips


def sort_dec(data):
    """
    sorts the decimals in descending order.
    :param data: A list of dictionaries that store the user data
    :return: Dictionary with partner name : total tips for the week but sorted with higher decimals at the top.
    """
    return sorted(data, key=lambda kv: kv['tips'] % 1, reverse=True)


def distribute_under(data, money, money_under):
    """
    takes the total tips of the store and subtracts the calc_under amount from it to get the total money left over.
    :param data: A list of dictionaries that store the user data
    :param money: total money the store earned that week
    :param money_under: value returned from calc_under
    :return: the tips each partner will get for the week. Dictionary with partner name : total tips for the week
    """
    money = int(money)
    extra = money - money_under
    count = 0

    if debug is True:
        print('DEBUG: Before the rounding')
        print(data, type(data))

    for z in data:
        if count < extra:
            z['tips'] = int(z['tips']) + 1
            count += 1

    return data


def sort_by_index(data):
    return sorted(data, key=lambda kv: kv['index'])


def print_header():
    if debug is True:
        print('-------------------------')
        print('     Tip Calculation')
        print(' !!!Debugging Enabled!!!')
        print('-------------------------')
    else:
        print('-------------------------')
        print('     Tip Calculation')
        print('-------------------------')


def pretty_print(data):
    print('--------------------------------------------')
    for v in data:
        print("| {0:15} {1:>2} {2:<7} {3:>7}{4:<2}|".format(v['name'], 'Hours:', v['hours'], '$', int(v['tips'])))
        print('--------------------------------------------')


def pretty_print_plus(data, t_per_h):
    print('-----------------------------------------------------------')
    for v in data:
        print("| {0:15} {1:>2} {2:<7} {3:>7}{4:<3} {5:<7} {6:<3} |".format(v['name'], 'Hours:', v['hours'], '$',
                                                                         int(v['tips']), 'unrnd:',
                                                                         float("%.3f" % (v['hours'] * t_per_h))))
        print('-----------------------------------------------------------')


"""
DEBUGGING TOOLS
"""


def print_partners_plus_hours(partners, hours):
    """
    A debug tool.
    :param partners:
    :param hours:
    :return:
    """
    for x in range(0, len(partners)):
        print(partners[x] + ' : ' + hours[x])


def re_init(data):
    for x in data:
        x['hours'] = 0
        x['tips'] = 0
    file_manager.save('partners', data)


def init_index(data):
    count = 0
    for x in data:
        x['index'] = count
        count = count + 1
    file_manager.save('partners', data)


"""
END DEBUGGING TOOLS
"""

if __name__ == '__main__':
    main()
