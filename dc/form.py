import random
import string

class Form:
    def __init__(self, seed=None) -> None:
        if seed is not None:
            random.seed(seed)

    def generate_from(self, string: str, min: int, max: int):
        assert min < max
        return "".join([random.choice(string) for _ in range(random.randint(min, max))])
        
    def generate_email(self) -> str:
        local_parts = self.generate_from(string.ascii_lowercase+string.digits, 5, 9)
        domain_name = f"{self.generate_from(string.ascii_lowercase, 3, 5)}.{self.generate_from(string.ascii_lowercase, 2, 4)}"
        return f"{local_parts}@{domain_name}"