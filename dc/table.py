from .auth import auth

import pandas as pd

class Table:
    def __init__(self) -> None:
        self.auth = auth.Auth()

    def create_pylon_create(self, count: int):
        df = pd.DataFrame(columns=['email', 'username', 'password'])
        for i in range(count):
            df = pd.concat([df, pd.DataFrame(self.auth.pylon.create(), index=[i])])
        
        return df
    
class CSV:
    def __init__(self) -> None:
        self.table = Table()

    def pylon_create(self, count: int, path: str="./pylon_create.csv"):
        df = self.table.create_pylon_create(count)
        df.to_csv(path)