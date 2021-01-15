import datetime
from schedule.models import Calendar
#from schedule.models import Event
from schedule.periods import Period, Week, Day, Month
from .models import Task


cl = Calendar.objects.all()

for c in cl:
    print(c.slug)

c = cl[5]

c = Calendar.objects.get(slug=c.slug)

ev = Task.objects.filter(calendar=c)

#p = Week(ev, datetime.datetime.now())

#tz = datetime.timezone(name='America/Chicago')
#now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6)))

now = datetime.datetime.now(datetime.timezone.utc)
#now = datetime.datetime.now(tz='UTC')


p = []
p.append(Day(ev, now))
p.append(Week(ev, now))
p.append(Month(ev, now))

oc = p[0].get_occurrences()
oc = p[1].get_occurrences()
oc = p[2].get_occurrences()


def fmtocc(oc):
    daynames = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for o in oc:
        st = o.start
        en = o.end
        print(o.title)
        print(daynames[st.weekday()] + ' through ' + daynames[en.weekday()])
