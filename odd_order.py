#%%
import pickle
from fubon_neo.sdk import FubonSDK, Mode, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

with open('info.pkl', 'rb') as f:
    user_info_dict = pickle.load(f)

sdk = FubonSDK()
accounts = sdk.login(user_info_dict['id'], user_info_dict['pwd'], user_info_dict['cert_path'], user_info_dict['cert_pwd'])

active_acc = None
for acc in accounts.data:
    if acc.account == user_info_dict['target_account']:
        active_acc = acc

print(active_acc)
# %%

order = Order(
    buy_sell = BSAction.Buy,
    symbol = "2881",
    price =  "85.4",
    quantity =  3,
    market_type = MarketType.IntradayOdd,
    price_type = PriceType.Limit,
    time_in_force = TimeInForce.ROD,
    order_type = OrderType.Stock,
    user_def = "odd" # optional field
)

order_res = sdk.stock.place_order(active_acc, order)
