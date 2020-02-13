import dotenv
dotenv.load_dotenv()

from state_machine.unfriend import UnfriendStateMachine


usm = UnfriendStateMachine()
usm.execute()

