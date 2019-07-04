# Calculates estimated income by x amount of pay-periods
def calculateIncomeByPayPeriod(net_pay_per_pay_period, bills_per_pay_period, savings_per_pay_period, pay_periods=1):
    disposable = (net_pay_per_pay_period - bills_per_pay_period - savings_per_pay_period)
    return {
        "Disposable": disposable * pay_periods,
        "Savings": savings_per_pay_period * pay_periods,
        "inRent": bills_per_pay_period * pay_periods,
    }