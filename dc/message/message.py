from ..form import Form

import string

class Mesagge:
    def __init__(self) -> None:
        pass

    def message(self, channel_id: int):
        return {
            "channelid": channel_id,
            "content": Form.generate_from(string.ascii_lowercase+string.digits+" ", 13, 120)
        }