import datetime


class logger:
    def __init__(self, log_path, console=False):
        self.log_path = log_path
        self.console = console

    def log_message(self, message, level):
            timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            log_text = '{}|{}|{}\n'.format(timestamp, level, message)
            if self.console:
                print(log_text)
            with open(self.log_path, 'a+') as file:
                file.write(log_text)
