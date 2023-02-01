from tinkoff.invest import Client, PortfolioResponse, RequestError, PortfolioPosition
from creds.ApiKeys import tinkoff_token_test_acc, tinkoff_acc_id_test_acc
from tinkoff.invest import Client, InstrumentStatus, InstrumentIdType, CandleInterval
import pandas as pd
from pprint import pprint



def more_about_assets(figi):
    with Client(tinkoff_token_test_acc) as client:
        a = client.instruments.get_instrument_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=figi)
        b = getattr(getattr(a, 'instrument'), 'ticker')
        return b

# c = client.instruments.share_by(id=figi, id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI)
# c = client.instruments.share_by(id='APLE', id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER, class_code='APLE')



# if __name__ == '__main__':
