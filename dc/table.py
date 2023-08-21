from .auth import auth
from .message import message

import pandas as pd

class Table:
    def __init__(self) -> None:
        self.auth = auth.Auth()
        self.message = message.Mesagge()

    def create_pylon_create(self, count: int):
        df = pd.DataFrame(columns=['email', 'username', 'password'])
        for i in range(count):
            df = pd.concat([df, pd.DataFrame(self.auth.pylon.create(), index=[i])])
        
        return df
    
    def create_message(self, count: int, channel_id: int):
        df = pd.DataFrame(columns=['channelid', 'content'])
        for i in range(count):
            df = pd.concat([df, pd.DataFrame(self.message.message(channel_id))])

        return df
    
class CSV:
    def __init__(self) -> None:
        self.table = Table()

    def pylon_create(self, count: int, path: str="./pylon_create.csv"):
        df = self.table.create_pylon_create(count)
        df.to_csv(path)

    def create_message(self, count: int, channel_id: int, path: str="./message.csv"):
        df = self.table.create_message(count, channel_id)
        df.to_csv(path)