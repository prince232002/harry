import datetime 
t=datetime.datetime.now()
d=datetime.date.today()
print(t.hour,"hrs",t.minute,"mins",t.second,"sec")
print(t.strftime("%A %b"))