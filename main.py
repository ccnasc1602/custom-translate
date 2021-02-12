from utils.translations.translate import gettex as _

class Main:
    def __init__(self):
        pass
    
    def run(self, message):
        print(_(message, "br", "br"))


if __name__=="__main__":
    Main().run("Executar este módulo na linha de comando produz a seguinte saída")