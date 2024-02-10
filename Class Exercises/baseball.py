import datetime
print ("=" * 40)
print (" " * 20, "Baseball Team Manager", " " * 10)

class dates(datetime):
    def __init__(self, year, month, day):
        today = (2021, 3, 21)
        print(f"CURRENT DATE:/t {today}")
        gamedate =