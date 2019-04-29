from datetime import datetime
date_format = "%d/%m/%Y"
a = datetime.strptime('12/11/1994', date_format)
b = datetime.strptime('11/1/1996', date_format)
delta = b - a
print (delta)
