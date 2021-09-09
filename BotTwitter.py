import datetime
class BotTwitter:
      def __init__ (self):
            self.cuentas = ["ivan","erick","diego","carlos"]
            self.temas = ["#bitcoin","#elonmusk","#pitbulls"]
            self.fechaInicial = datetime.datetime.now()

a = BotTwitter ()
b = BotTwitter ()
print(a.cuentas)
print(b.temas)
print(datetime.datetime.now())





