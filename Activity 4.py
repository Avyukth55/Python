from datetime import datetime
import calendar
now=datetime.now()
print(now)
date=now.date()
time=now.time().strftime("%H:%M:%S")
month=calendar.month_name[now.month]
year=now.year
hours=now.hour
minute=now.minute
second=now.second
print(f"{'DATE':<15}{'TIME':<15}{'YEAR':<15}")
print(f"{str(date):<15}{time:<15}{year:<15}")
print(f"{'HOURS':<15}{'MINUTES':<15}{'SECONDS':<15}")
print(f"{hours:<15}{minute:<15}{second:<15}")
print(f"{'MONTH':<15}")
print(f"{month:<15}")