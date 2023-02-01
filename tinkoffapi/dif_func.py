from tinkoff.invest import Client, PortfolioResponse
from creds.ApiKeys import tinkoff_token_test_acc,tinkoff_acc_id_test_acc
from pprint import pprint


shares_key = 'total_amount_shares'
bonds_key = 'total_amount_bonds'
etf_key = 'total_amount_etf'
currencies_key = 'total_amount_currencies'


def full_assets(key):
    with Client(tinkoff_token_test_acc) as client:
        a : PortfolioResponse = client.operations.get_portfolio(account_id=tinkoff_acc_id_test_acc)
        # a = client.users.get_accounts().accounts
        # keys = ['total_amount_shares', 'total_amount_bonds', 'total_amount_etf', 'total_amount_currencies']
        # pprint({k: getattr(a, k) for k in keys})
        # pprint(a)
        # key = 'total_amount_shares'
        # pprint(cast_money(getattr(a, key)))
        return cast_money(getattr(a, key))


def cast_money(t):
    u = ' '
    return str(t.units + t.nano/1e9) + u + t.currency

# full_assets()

# shares = full_assets(shares_key)
# bonds = full_assets(bonds_key)
etf = full_assets(etf_key)
# currencies_key = full_assets(currencies_key)
print(etf)
