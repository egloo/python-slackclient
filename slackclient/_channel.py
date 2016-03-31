class Channel(object):
    def __init__(self, server, name, channel_id, members=None):
        self.server = server
        self.name = name
        self.id = channel_id
        self.members = [] if members is None else members

    def __eq__(self, compare_str):
        # if self.name == compare_str or self.name == "#" + compare_str or self.id == compare_str:
        #     return True
        # else:
        #     return False
        return compare_str in (self.id, self.name) or (compare_str is not None and "#" + compare_str == self.name)

    def __str__(self):
        # data = ""
        # for key in list(self.__dict__.keys()):
        #     data += "{0} : {1}\n".format(key, str(self.__dict__[key])[:40])
        # return data
        fmt = "{} : {:.40}"
        return "\n".join(fmt.format(key, str(value)) for key, value in self.__dict__.items())

    def __repr__(self):
        return self.__str__()

    def send_message(self, message):
        message_json = {"type": "message", "channel": self.id, "text": message}
        self.server.send_to_websocket(message_json)
