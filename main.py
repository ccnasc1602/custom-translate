from utils.translations.translate import gettex as _

class Main:
    def __init__(self):
        pass
    
    def run(self, message):
        print(_(message))


if __name__=="__main__":
    Main().run("Language not specified or output language equal to input language")