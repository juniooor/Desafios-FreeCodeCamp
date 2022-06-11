def add_time(start,add,day=None):
  time, periodo = start.split() 
  horas, minutos = map(int,time.split(':'))  
  addH, addM = map(int,add.split(':'))
  meidia = ('PM','AM') 
  Ndias = '' 
  depois = ''
  
  carry, minutos = divmod(minutos + addM,60) 
  horas += carry 
  ciclos, horas = divmod(horas + addH,12) 
  
  periodo = abs(meidia.index(periodo)-(ciclos % 2)) 
  passou = (periodo + ciclos) // 2  
  
  if horas == 0: 
    horas = 12

  if minutos < 10: 
    minutos = f'0{minutos}'

  if day:
      semana = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
      new_day = f', {semana[(semana.index(day.capitalize()) + passou) % 7]}' 
  
  if passou == 1:
      depois = ' (next day)'
  elif passou != 0:
      depois = f' ({passou} days later)'
      
  return f'{horas}:{minutos} {meidia[periodo]}{Ndias}{depois}'



actual = add_time("8:16 PM", "466:02", "tuesday")
print(actual)