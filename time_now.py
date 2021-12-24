from datetime import datetime

def get_hour():
    now = datetime.now().strftime('%H')
    return int(now)

print(get_hour())


