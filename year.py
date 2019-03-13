import datetime

def create_year():
  d = datetime.date.today()
  yr = (d.strftime('%y'))
  
  return yr
