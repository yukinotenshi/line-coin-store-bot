import os
import json
import dotenv
import requests
from time import sleep
from model import db, Order
from state_machine.add_friend import AddFriendStateMachine
from state_machine.buy_sticker import BuyStickerStateMachine
from state_machine.unfriend import UnfriendStateMachine

dotenv.load_dotenv()


def update_status(order_id, status):
    success = False
    while not success:
        try:
            requests.post(os.getenv("MAIN_WEBHOOK"), json={"id": order_id, "status": status}, headers={
                "Authorization": os.getenv("WEBHOOK_PSWD")
            })
            success = True
        except:
            pass


def get_order():
    if db.is_closed():
        db.connect()

    order = Order.get_or_none(Order.is_processing == False)
    if not order:
        return

    order.is_processing = True
    order.save()
    if not db.is_closed():
        db.close()

    return order


def handle_order(order: Order):
    items = json.loads(order.items)

    update_status(order.order_id, "Menambahkan teman")
    afsm = AddFriendStateMachine(order.target_id)
    afsm.execute()

    if 'name' not in afsm.data:
        update_status(order.order_id, "ID LINE tidak ditemukan.")
        return

    for i in items:
        update_status(order.order_id, "Mengirimkan pesanan")
        bssm = BuyStickerStateMachine(i['link'], afsm.data['name'], driver=afsm.data['driver'])
        bssm.execute()

    update_status(order.order_id, "Pesanan berhasil dikirimkan")
    usm = UnfriendStateMachine(order.target_id, driver=afsm.data['driver'])
    usm.execute()
    usm.close()


if __name__ == "__main__":
    while True:
        order = get_order()
        if not order:
            sleep(10)
            continue

        try:
            handle_order(order)
        except Exception as e:
            print(e)
