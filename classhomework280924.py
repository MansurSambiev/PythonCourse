#Расчет чаевых и общей суммы
class Tips:
  def __init__(self, check, tip):
    self.check = check
    self.tip = tip
 
  def calc_tips(self):
    self.tip = self.check*(self.tip/100)
    sum = self.check + self.tip
    print(f'Общая сумма - {sum}Р, чаевые - {self.tip}Р')

bill = Tips(1200, 5)
bill.calc_tips()

-------------------------------------------------------------------------------
#Конвертер температуры
class TempCalc:
  Temperature = ('c', 'f', 'k')
  @classmethod
  def validate(cls, arg):
    return arg in cls.Temperature
  
  def __init__(self, value, temp):
    self.value = value
    if self.validate(temp):
        self.temp = temp
    else:
      print('Неверная единица измерения')


  def calculate(self):
    if self.temp == 'c':
      print(f'{self.value} градусов Цельсия = {round(self.value * 1.8 + 32, 2)}'
            f' градусов Фаренгейта, {round(self.value + 273.15, 2)} градусов Кельвина')
    elif self.temp == 'f':
      print(f'{self.value} градусов Фаренгейта = {round(self.value / 1.8 - 32, 2)}'
            f' градусов Цельсия, {round((self.value + 459.67) / 1.8), 2} градусов Кельвина')
    else:
      print(f'{self.value} градусов Кельвина {round(self.value - 273.15, 2)}'
            f' градусов Цельсия, {round((self.value - 459.67) * 1.8, 2)} градусов Фаренгейта')

new_temp = TempCalc(100, 'c')
new_temp.calculate()
new_temp = TempCalc(100, 'f')
new_temp.calculate()
new_temp = TempCalc(1000, 'k')
new_temp.calculate()
