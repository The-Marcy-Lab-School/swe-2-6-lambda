from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15))
hall.add_event(Event('Movie Night: Coco', date(2026, 11, 28), capacity=30, base_price=8))
hall.add_event(Event('Board Game Night', date(2027, 1, 8), capacity=25, base_price=0))


# Uncomment, predict, run, then comment it out again.
# print(sorted(hall.events))
# Prediction:
# Actual:

print(max(hall.events, key=lambda event: event.capacity))
# Prediction:
# Actual:

print(min(hall.events, key=lambda event: event.ticket_price()))
# Prediction:
# Actual:

by_date = sorted(hall.events, key=lambda event: event.date)
print([event.name for event in by_date])
# Prediction:
# Actual:


# Replace each None with one call to min(), max(), or sorted() that uses key=lambda ...

def latest_first(events):
    return None   # 1. The events, from the latest date to the earliest

def fewest_seats(events):
    return None   # 2. The event with the fewest seats

def alphabetical(events):
    return None   # 3. The events in alphabetical order by name


print(latest_first(hall.events))
# [Event('Board Game Night', 2027-01-08), Event('Intro to Pottery', 2026-12-09), Event('Friday Night Jazz', 2026-12-05), Event('Movie Night: Coco', 2026-11-28)]
print(fewest_seats(hall.events))
# Event('Intro to Pottery', 2026-12-09)
print(alphabetical(hall.events))
# [Event('Board Game Night', 2027-01-08), Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09), Event('Movie Night: Coco', 2026-11-28)]
