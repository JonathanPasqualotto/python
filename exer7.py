import datetime

nasc = int(input('Digite o ano de seu nascimento:'))


data = datetime.date.today()
ano = data.strftime("%Y")

mediaAno = float(ano) - nasc

print("Sua idade atual é %d"%(mediaAno))



