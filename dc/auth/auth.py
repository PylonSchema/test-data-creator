from ..form import Form

import random
import string

class Auth:
    def __init__(self) -> None:
        self.pylon = Pylon()

class Pylon:
    def __init__(self, random_seed=None) -> None:
        if random_seed is not None:
            random.seed(random_seed)

        self.form = Form()

    def create(self):
        account = {
            "email": self.form.generate_email(),
            "username": self.form.generate_from(string.ascii_lowercase+string.digits, 8, 13),
            "password": self.form.generate_from(string.ascii_lowercase+string.digits, 11, 17)
        }
        return account