import dotenv
dotenv.load_dotenv()

from state_machine.buy_sticker import BuyStickerStateMachine


bssm = BuyStickerStateMachine()
bssm.execute()
