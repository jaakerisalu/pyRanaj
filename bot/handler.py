class CommandHandler:
    def __init__(self, cli, msg, channel):
        self.client = cli
        splits = msg.split(' ', 1)
        self.command = splits[0]
        self.message = splits[1]
        self.channel = channel

    def send_message(self, text):
        self.client.api_call("chat.postMessage", channel=self.channel,
                             text=text, as_user=True)

    @property
    def test(self):
        return self.send_message("This is a tesst handler")

    @property
    def pasta(self):
        return self.send_message("This is another handler")

    @property
    def not_found(self):
        return self.send_message("Dafuq u want man")

    def handle(self):
        """
            Map commands ranaj should respond to to their handlers here
        """
        accepted_commands = ["test", "pasta"]
        if self.command in accepted_commands:
            return getattr(self, self.command)
        return self.not_found
