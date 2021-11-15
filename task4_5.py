def deposit(amount, period, replenishment):
    deposit_list = [{
        'begin_sum': 1000,
        'end_sum': 10000,
        6: 5,
        12: 6,
        24: 5,
    },
        {
            'begin_sum': 10000,
            'end_sum': 100000,
            6: 6,
            12: 7,
            24: 6.5,
        },
        {
            'begin_sum': 100000,
            'end_sum': 1000000,
            6: 7,
            12: 8,
            24: 7.5,
        },
    ]

    def month(month_sum, percent, number_of_months):
        all_sum = month_sum * (number_of_months - 2)
        return all_sum + (all_sum / 100 * ((percent / number_of_months) * (number_of_months - 2)))

    for elem in deposit_list:
        if elem.get('begin_sum') < amount < elem.get('end_sum'):
            return print(month(replenishment, elem.get(period), period) + amount + (amount / 100) * elem.get(period))


deposit(9000, 6, 2000)
