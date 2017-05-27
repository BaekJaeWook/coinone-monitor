import requests
import sys
import time
from datetime import datetime



def watch_price(max_price=0, min_price=0):
    resp = requests.get("https://api.coinone.co.kr/trades/?currency=eth")
    result = resp.json()

    order = result["completeOrders"][-1]
    price = int(order["price"])
    date_now = datetime.fromtimestamp(int(order["timestamp"]))
    print("max_limit: %d\nmin_limit: %d\n" % (max_price, min_price))
    print("time: %s\nprice: %d\n" % (date_now, price))

    if max_price == 0 and min_price == 0:
        return

    if price >= max_price: 
        for _ in range(3):
            time.sleep(0.2)
            print("warn!!! max price: %d\a\n" % price)
    elif price <= min_price:
        for _ in range(5):
            time.sleep(0.2)
            print("warn!!! min price: %d\a\n" % price)


if __name__ == "__main__":
    max_price = int(sys.argv[1])
    min_price = int(sys.argv[2])

    while True:
        time.sleep(5)
        watch_price(max_price, min_price)
