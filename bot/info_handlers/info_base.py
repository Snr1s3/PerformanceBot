import json

class InfoBase:
    def __init__(self, socket_con):
        self.socket_con = socket_con

    def get_info(self, section: str, formatter: callable) -> list:
        content = self.socket_con.receive()
        arr = []
        try:
            data = json.loads(content)
            if section:
                info = data.get(section, {})
                arr = formatter(info)
            else:
                return data
        except Exception as e:
            print("Error parsing JSON:", e)
            print("Raw content:", content)
        return arr