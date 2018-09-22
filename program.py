import file_manager
import get_input
import calculate

debug = False


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
        get_input.input_partners_manual(partner_data)
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
            data = get_input.input_hours(data, debug)
            if data is None:
                print('No data entered.')
                continue
            # print(data)
            # TODO Fix so that it handles unexpected results.
            total_money = float(input('Total tips: '))
            for x in data:
                sum_hours += x['hours']

            tips_per_hour = calculate.tph(sum_hours, total_money)
            tips_per_hour = float("%.3f" % tips_per_hour)
            print(tips_per_hour)
            calculate.itph(tips_per_hour, data)

            tip_total_under = calculate.under(data)
            od = calculate.sort_dec(data)
            final_list = calculate.distribute_under(od, total_money, tip_total_under, debug)

            if debug is True:
                checksum = 0
                for s in data:
                    checksum += int(s['tips'])
                print(checksum)
            final_list = sort_by_index(final_list)
            # pretty_print(final_list)
            pretty_print_plus(final_list, tips_per_hour)

        elif cmd == 'r':
            # TODO:ERROR When removing index positions it you remove pos 1 and then 2 you will get an error,
            # because all the indacies have changed.
            for idx, x in enumerate(data):
                print(idx + 1, x)
            print(
                'Please enter the name of the partner you need to remove\n'
                ' (Enter a -1 to cancel.)\n')

            while True:
                try:
                    cmd = int(input('Index: '))
                    if cmd < 0:
                        if debug is True:
                            print("Would save here.")
                            break
                        else:
                            file_manager.save('partners', data)
                            break
                    else:
                        data = file_manager.remove_entry(cmd - 1, data)
                except ValueError:
                    print("you must enter an integer")

        elif cmd == 'a':
            new_partner = 'Empty'
            new_partner_dict = {'name': '', 'hours': 0, 'tips': 0}
            pos = 0
            print('Please enter the name of the new partner,\nthen the position in the list.\n'
                  ' (1 is the first position in the list, 2 is the second position and so on.)\n'
                  ' (type "print" to see current list)\n'
                  ' (type "done" when finished)')
            while new_partner.lower() != 'done' or new_partner.lower() != 'd':
                new_partner = input('Input: ')

                if new_partner.lower() == 'done' or new_partner.lower() == 'd' or new_partner == '-1':
                    file_manager.save('partners', data)
                    break
                elif new_partner.lower() == 'p' or new_partner.lower() == 'print':
                    for x in data:
                        print(x)
                    print('')
                else:
                    while True:
                        try:
                            pos = int(input('Index: '))
                            break
                        except ValueError:
                            print("you must enter an integer")

                    new_partner_dict['name'] = new_partner
                    new_partner_dict['index'] = pos - 1
                    file_manager.add_entry(data, new_partner_dict)
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
