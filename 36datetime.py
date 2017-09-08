from datetime import datetime, timedelta, timezone

now = datetime.now()
utc_now = datetime.utcnow()
print(now)
print(utc_now)
print(type(now))
print(type(utc_now))

t = datetime(2017, 4, 19, 12)
print(t)

print(t.timestamp())

# 本地时间
print(datetime.fromtimestamp(t.timestamp()))

# UTC标准时区
print(datetime.utcfromtimestamp(t.timestamp()))

print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))

print(now + timedelta(hours=10, minutes=-5))

tz_utc_8 = timezone(timedelta(hours=8))
print(now.replace(tzinfo=tz_utc_8))

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)


