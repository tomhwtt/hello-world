import datetime

# creaet a two digit year
def create_year():
  d = datetime.date.today()
  yr = (d.strftime('%y'))
  
  return yr
