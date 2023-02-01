from tinkoff.invest import Client, PortfolioResponse
from creds.ApiKeys import tinkoff_token_test_acc, tinkoff_acc_id_test_acc
# from about_acc import shares, bonds, etf, currencies, futures

shares_key = 'total_amount_shares'
bonds_key = 'total_amount_bonds'
etf_key = 'total_amount_etf'
currencies_key = 'total_amount_currencies'
futures_key = 'total_amount_futures'

def full_assets(key):
    with Client(tinkoff_token_test_acc) as client:
        a : PortfolioResponse = client.operations.get_portfolio(account_id=tinkoff_acc_id_test_acc)
        # a = client.users.get_accounts().accounts
        # keys = ['total_amount_shares', 'total_amount_bonds', 'total_amount_etf', 'total_amount_currencies']
        # pprint({k: getattr(a, k) for k in keys})

        # key = 'total_amount_shares'
        # print(cast_money(getattr(a, key)))
        # print(type(getattr(a, key)))
        return cast_money(getattr(a, key))

def cast_money(t):
    u = ' '
    return str(t.units + t.nano/1e9) + u + t.currency


""" 
for i in range(len(x)):
    result[i] = int(x[i]) + int(y[i])
print(result)
"""


shares = full_assets(shares_key)
bonds = full_assets(bonds_key)
etf = full_assets(etf_key)
currencies = full_assets(currencies_key)
futures = full_assets(futures_key)

def full_assets_to_display(shares, bonds, etf, currencies, futures):
    if shares != '0.0 rub':
        a = 'Shares: ' + shares
    else:
        a = ''
    if bonds != '0.0 rub':
        b = f'\nBonds: {bonds}'
    else:
        b = ''
    if etf != '0.0 rub':
        c = f'\nETF: {etf}'
    else:
        c = ''
    if currencies != '0.0 rub':
        d = f'\nCurrencies: {currencies}'
    else:
        d = ''
    if futures != '0.0 rub':
        e = f'\nFutures: {futures}'
    else:
        e = ''

    s = a+b+c+d+e



    # return [x for x in without_none(k)]
    return s


results_full_assets = full_assets_to_display(shares, bonds, etf, currencies, futures)

# print(results_full_assets)


