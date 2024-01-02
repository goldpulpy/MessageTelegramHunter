from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat
from telethon.errors import SessionPasswordNeededError

from templates import REPORT, PUSH_START

from telethon.tl.functions.messages import GetHistoryRequest
from time import sleep as wait


class Session:

    def __init__(self, api_id: int = None,
                       api_hash: str = None,
                       session_name: str = None
    ) -> None:

        self.api_id: int = api_id
        self.api_hash: str = api_hash
        self.session_name: str = session_name
        
        self.client = TelegramClient(self.session_name, self.api_id, self.api_hash)

        self.client.parse_mode = "html"

        self.user_id: int = None
        self.username: str = None
        self.first_name: str = None

        self.chats: list = []

        self.home_chat: Dialog = None

        self.message_pool: list = []


    def check_session(self)-> bool:

        self.client.connect()

        if not self.client.is_user_authorized():

            phone_number: str = input("[->] Enter your phone number: ")
            self.client.send_code_request(phone_number)
            
            code: str = input("[->] Enter code: ")
            
            try:

                self.client.sign_in(phone_number, code)
            
            except SessionPasswordNeededError:

                password: str = input("[->] Enter password: ")

                self.client.sign_in(password=password)

            if not self.client.is_user_authorized():

                return False


        user = self.client.get_me()
        
        self.user_id: int = user.id
        self.username: str = user.username
        self.first_name: str = user.first_name

        for dialog in self.client.iter_dialogs():
            self.chats.append(dialog)

        return True

    def push_start(self, forward_to_id: int) -> bool:

        try:

            for chat in self.chats:

                if chat.entity.id == forward_to_id:

                    self.home_chat: Dialog = chat

                    self.client.send_message(self.home_chat.entity, PUSH_START % (
                                             self.home_chat.entity.title, 
                                             self.home_chat.entity.id))
                    
                    break

            if not self.home_chat:

                return False

            return True

        except:

            return False



    def get_pool(self, message_pool_limit: int) -> bool:

        try:

            for chat in self.chats:

                if chat.entity.id == self.home_chat.entity.id:

                    continue
                
                messages = self.client.get_messages(
                    chat.entity,
                    limit=message_pool_limit
                )

                self.message_pool.append(
                    {
                        "chat": chat,
                        "messages": [message for message in messages]
                    }
                )

            return True

        except:

            return False



    def check_new_message (self, message_pool_limit: int,
                           smartFilter: object) -> list:

        new_message_pool: list = []

        new_message_count: int = 0
        trigger_message_count: int = 0

        for chat in self.chats:

            if chat.entity.id == self.home_chat.entity.id:

                continue

            messages: list = self.client.get_messages(chat.entity, limit=message_pool_limit)

            new_message_pool.append({
                "chat": chat,
                "messages": [message for message in messages]
            })

            for chat_from_pool in self.message_pool:

                if chat_from_pool["chat"].entity.id == chat.entity.id:

                    message_from_pool = chat_from_pool["messages"]

                    for message in messages:


                        if message.id not in [m.id for m in message_from_pool]:

                            new_message_count += 1

                            if message.message == '':

                                continue

                            if smartFilter.filt(message.message):

                                trigger_message_count += 1

                                self.send_report(chat, message)

        self.message_pool = new_message_pool

        return new_message_count, trigger_message_count



    def disconnect(self) -> None:
        self.client.disconnect()





    def send_report(self, chat: object, message: str) -> None:

        try:

            username = "@"+chat.entity.username

        except:

            username = "-"


        try:
            
            name = chat.entity.title

        except:

            name = chat.entity.first_name

        self.client.send_message(self.home_chat.entity, REPORT %(
                name,
                chat.entity.id,        
                username,
                chat.entity.id,
                message.id,
                message.message
            
        ))

        
        

        