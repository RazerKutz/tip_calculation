import collections
import file_manager


def main():
    print_header()
    file_manager.load()
    run_loop()


def run_loop():
    # todo Check for partners.txt.
    while True:
        cmd = input('[E]nter info or [Q]uit: ').lower()
        if cmd == 'e':
            partners = input_partners_from_file()
            # print_partners(partners)
            hours_list = input_hours(partners)
            # if the user enters Q then the program closes nicely
            if hours_list is None:
                print('quitting program.')
                break
            # print_partners_plus_hours(partners, hours_list)
            partner_dict = dict(zip(partners, hours_list))
            # print(partner_dict)
            # print(sum(dictionary.values()))
            total_money = float(input('Total tips: '))
            # calc_tph(sum(dictionary.values()), )
            dollar_per_hour = calc_tph(sum(partner_dict.values()), total_money)
            dollar_per_hour = float("%.2f" % dollar_per_hour)
            print(dollar_per_hour)
            partner_dict_idph = calc_idph(dollar_per_hour, partner_dict)
            # print(partner_dict_idph)
            # print(calc_under(partner_dict_idph))
            tip_total_under = calc_under(partner_dict_idph)
            od = sort_dec(partner_dict_idph)
            od = collections.OrderedDict(od)
            print(od, type(od))
            final_dict = distribute_under(od, total_money, tip_total_under)
            for key, val in final_dict.items():
                print(key, ": ", val)
        elif cmd == "q":
            print('quitting program.')
            break
        print()



# This is if there is no file for the partners
def input_partners_manual():
    count = input('Number of partners: ')
    list = []
    print(type(int(count)), ' ' + count)
    for x in range(0, int(count)):
        list.append(input('Partner Name: '))

    return list


# reads the list of partners from the partners.txt
def input_partners_from_file():
    with open('partners.txt') as f:
        lines = f.readlines()
    lines = [x.rstrip('\n') for x in lines]
    return lines


def print_partners(x):
    print(x)


def print_partners_plus_hours(partners, hours):
    for x in range(0, len(partners)):
        print(partners[x] + ' : ' + hours[x])


def input_hours(p_list):
    print('Please input the hours worked for each partner.')
    hours = []

    for x in range(0, len(p_list)):
        cmd = input(p_list[x] + ': ')
        if cmd.lower() == 'q':
            return None
        else:
            hours.append(float(cmd))

    return hours


def calc_tph(total_hours, tip_amount):
    return tip_amount / total_hours
    # return tip_amount / total_hours


def calc_idph(dph, dictionary):
    return {k: float("%.2f" % (dictionary[k] * dph)) for k in dictionary}


def calc_under(p_dict):
    p2_dict = {k: int(p_dict[k]) for k in p_dict}
    return sum(p2_dict.values())


def sort_dec(p_dict):
    # return collections.OrderedDict(sorted({k: p_dict[k] for k in p_dict}, key=lambda f: f % 1))
    return sorted(p_dict.items(), key=lambda kv: kv[1] % 1, reverse=True)

    # return sorted({k: od[k] for k in od}, key=lambda f: f % 1)


def distribute_under(p_dict, money, money_under):
    # print(money, type(money))
    # print(money_under, type(money_under))
    money = int(money)
    extra = money - money_under

    print('DEBUG: Before the rounding')

    print(p_dict)
    p_dict = {k: int(p_dict[k]) for k in p_dict}
    count = 0
    print(p_dict, type(p_dict))
    for x, y in p_dict.items():
        if count <= extra:
            p_dict[x] = p_dict.get(x) + 1
            # p_dict[x] = p_dict.get(x) + 1
            count += 1

    return p_dict


def print_header():
    print('------------------------')
    print('     Tip Calculation')
    print('------------------------')


if __name__ == '__main__':
    main()
