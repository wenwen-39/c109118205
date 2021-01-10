import csv,sys,os
project_dir = './mainsite/'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mblog.settings'
import django
django.setup()
from mainsite.models import heightdata
data = csv.reader(open("./mainsite/data.csv",encoding="utf-8"),delimiter=",",)
for row in data:
    if row[0] !='year':
        unit = heightdata()
        unit.year = row[0]
        unit.old = row[1]
        unit.total = row[2]
        unit.boy = row[3]
        unit.girl = row[4]
        unit.save()