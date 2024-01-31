import datetime

now = datetime.datetime.now()

# 1
five_days_ago = now - datetime.timedelta(days=5)
print(f"five days ago = {five_days_ago.date()}")

# 2
yesterday = now - datetime.timedelta(days=1)
tomorrow = now + datetime.timedelta(days=1)
print(f"Yesterday = {yesterday.date()}\ntoday = {now.date()}\ntomorrow = {tomorrow.date()}") #date чтобы чисто год месяц день показать

#3
dropped_ms=now.replace(second=0,microsecond=0)
print(f"without second{dropped_ms}")

#4
date_1=now
date_2=five_days_ago
print(f"total seconds {(date_1-date_2).total_seconds() }")


