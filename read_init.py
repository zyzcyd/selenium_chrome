import configparser


class ReadIni:
    def __init__(self):
        self.data = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(r'/Users/zhangjiangtao/PycharmProjects/selenium_chrome/config/LocalElement.ini')
        return cf

    # def __init__(self):
    #     self.cf = configparser.ConfigParser()
    #     self.cf.read(r'/Users/zhangjiangtao/PycharmProjects/selenium_chrome/config/LocalElement.ini')

    def get_value(self, list_name, key):
        print(list_name, key)
        return self.data.get(list_name, key)


if __name__ == '__main__':
    aa = ReadIni()
    print(aa.get_value('element', 'username'))

read_ini = ReadIni()