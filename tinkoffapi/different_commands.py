# import datetime
#
# from tinkoff.invest import Client, InstrumentStatus, InstrumentIdType, CandleInterval
#
# import tokens
#
#
# with Client(tokens.test_token()) as client:
#     # a = client.operations.get_operations(
#     #     account_id=tokens.id_test(),
#     #     from_= datetime.datetime(2022,5,5),
#     #     #     to=datetime.datetime.now()
#     # )
#     # print(a)
#
#     # b = client.instruments.bonds(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL)
#     # b = client.instruments.bonds()
#     # b = len(b.instruments)
#     # print(b)
#
#     # b = client.instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)
#     # # b = client.instruments.bonds()
#     # # b = len(b.instruments)
#     # print(b)
#
# #Газпром нефть
#     figi = 'BBG004S684M6'
#  #    ticker = 'SIBN'
#  #    class_code = 'TQBR'
#  # #Apple Hospitality REIT
#  #    figi = 'BBG006473QX9'
#  #    ticker = 'APLE'
#  #    class_code = 'SPBXM'
# # Газпром
# #     figi = 'BBG004730RP0'
# #     ticker = 'GAZP'
# #     class_code = 'TQBR'
#
#     # f = 'APLE'
#     # figi = 'BBG000K6Y764'
#     # cc = 'MMAT'
#     # ticker = 'MMAT'
#     # e = 'CAKE'
#     # r = 'BBG000CS8TM8'
#     # c = client.instruments.share_by(id=figi, id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI)
#     # c = client.instruments.share_by(id='APLE', id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER, class_code='APLE')
#     # print(c)
#     #
#
#     # figi = 'BBG000CS8TM8'
#     # c = client.market_data.get_order_book(figi=figi, depth=50)
#     # print(c)
#
#     # figi = 'BBG000K6Y764'
#     c = client.market_data.get_candles(
#         figi=figi,
#         from_=datetime.datetime(2022,5,1),
#         to=datetime.datetime.now(),
#         interval=CandleInterval.CANDLE_INTERVAL_DAY
#     )
#     print(c)