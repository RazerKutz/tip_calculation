import collections
import file_manager


def main():
    """
    Starts the program
    :return: -
    """
    print_header()
    partner_data = file_manager.load('partners')
    if partner_data.__len__() == 0:
        input_partners_manual(partner_data)
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
            hours_list = input_hours(data)
            # if the user enters Q then the program closes nicely
            if hours_list is None:
                print('No data entered.')
                continue

            partner_dict = dict(zip(data, hours_list))

            total_money = float(input('Total tips: '))

            tips_per_hour = calc_tph(sum(partner_dict.values()), total_money)
            tips_per_hour = float("%.3f" % tips_per_hour)
            print(tips_per_hour)
            partner_dict_idph = calc_idph(tips_per_hour, partner_dict)

            tip_total_under = calc_under(partner_dict_idph)
            od = sort_dec(partner_dict_idph)
            od = collections.OrderedDict(od)
            print(od, type(od))
            final_dict = distribute_under(od, total_money, tip_total_under)
            print('------------------')

            for key, val in final_dict.items():
                print('{0:10} : {1:3}'.format(key, val))
                print('------------------')

        elif cmd == 'r':
            for idx, x in enumerate(data):
                print(idx + 1, x)
            # partner = 'Empty'
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
                    file_manager.add_entry(new_partner, data)
        elif cmd == 'l':
            for x in data:
                print(x)
        elif cmd == "q":
            print('quitting program.')
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
        data.append(input('Partner Name: '))
    file_manager.save('partners', data)
    return list


def input_hours(data):
    """
    Gets the hours the each partners worked.
    :param data: Partner List.
    :return: Returns a list of hours.
    """
    print('Please input the hours worked for each partner.'
          ' (Enter a -1 to cancel.)')
    hours = []
    good_data = True
    for x in range(0, len(data)):
        # cmd = input(data[x] + ': ')
        while True:
            try:
                cmd = float(input(data[x] + ': '))
                break
            except ValueError:
                print("you must enter an integer")
        if float(cmd) < 0:
            return None
        else:
            hours.append(float(cmd))
        """
        cmd = input(data[x] + ': ')
        if cmd.lower() == 'q':
            return None
        else:
            hours.append(float(cmd))
        """
    return hours


def calc_tph(total_hours, tip_amount):
    """
    This calculates tips per hour
    :param total_hours: The sum of the numbers entered by the user.
    :param tip_amount:  Total sum of money counted by the user.
    :return: amount or tips divided by the total hours worked.
    """
    return tip_amount / total_hours


def calc_idph(tph, dictionary):
    """
    Calculates each partners total tips.
    :param tph: The value calculated by calc_tph.
    :param dictionary: Dictionary with name : hours
    :return: Dictionary with partner name : total tips for the week
    """
    return {k: float("%.2f" % (dictionary[k] * tph)) for k in dictionary}


def calc_under(p_dict):
    """
    this sums the "total tips for week" for each partner with out the decimal value.
    :param p_dict: Dictionary with partner name : total tips for the week
    :return: Sum of the total tips with out decimals.
    """
    p2_dict = {k: int(p_dict[k]) for k in p_dict}
    return sum(p2_dict.values())


def sort_dec(p_dict):
    """
    sorts the decimals in descending order.
    :param p_dict: Dictionary with partner name : total tips for the week
    :return: Dictionary with partner name : total tips for the week but sorted with higher decimals at the top.
    """
    return sorted(p_dict.items(), key=lambda kv: kv[1] % 1, reverse=True)


def distribute_under(p_dict, money, money_under):
    """
    takes the total tips of the store and subtracts the calc_under amount from it to get the total money left over.
    :param p_dict: Dictionary with partner name : total tips for the week
    :param money: total money the store earned that week
    :param money_under: value returned from calc_under
    :return: the tips each partner will get for the week. Dictionary with partner name : total tips for the week
    """
    money = int(money)
    extra = money - money_under

    print('DEBUG: Before the rounding')

    print(p_dict)
    p_dict = {k: int(p_dict[k]) for k in p_dict}
    count = 0
    print(p_dict, type(p_dict))
    for x, y in p_dict.items():
        if count < extra:
            p_dict[x] = p_dict.get(x) + 1
            count += 1

    return p_dict


def print_header():
    print('------------------------')
    print('     Tip Calculation')
    print('------------------------')


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
        print('{0:2d} {1:3d}'.format(partners[x], hours[x]))


"""
END DEBUGGING TOOLS
"""

if __name__ == '__main__':
    main()
