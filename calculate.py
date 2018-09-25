def tph(total_hours, tip_amount):
    """
    This calculates tips per hour
    :param total_hours: The sum of the numbers entered by the user.
    :param tip_amount:  Total sum of money counted by the user.
    :return: amount or tips divided by the total hours worked.
    """
    return tip_amount / total_hours


# def calc_idph(tph, dictionary):
def itph(tips_per_hour, data):
    """
    Calculates each partners total tips.
    :param tips_per_hour: The value calculated by calc_tph.
    :param data: A list of dictionaries that store the user data
    :return: Dictionary with partner name : total tips for the week
    """

    for x in data:
        # x['tips'] = "%.2f" % x['hours'] * tph
        x['tips'] = float("%.2f" % (x['hours'] * tips_per_hour))
    # return data


def under(data):
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


def distribute_under(data, money, money_under, debug):
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

