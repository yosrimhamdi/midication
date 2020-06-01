from .get_all_dates import get_all_dates
from matplotlib import pyplot as plt

def get_months(dates):
  months = []
  
  for date in dates:
    months.append(date.split('/')[1])

  return months

def draw(monthNbr):
  x = [i for i in range(1, 13)]
  
  plt.plot(x, monthNbr)

  plt.title('nombre des consultations pour chaque mois')

  plt.xlabel('mois')
  plt.ylabel('nombre des consultations')

  plt.show()

def per_month():
  dates = get_all_dates()
  months = get_months(dates)

  monthNbr = [i for i in range(12)]

  for i in range(12):
    monthNbr[i] = 0
    for month in months:
      if (int(month) == i + 1):
        monthNbr[i] += 1

  draw(monthNbr)
      