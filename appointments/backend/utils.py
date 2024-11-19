from datetime import datetime, timedelta

def generate_time_slots(start_time, end_time, interval=60):
    """
    Generate time slots between `start_time` and `end_time` with the given `interval` in minutes.
    """
    slots = []
    current_time = datetime.combine(datetime.today(), start_time)
    end_time = datetime.combine(datetime.today(), end_time)
    while current_time < end_time:
        slots.append(current_time.time())
        current_time += timedelta(minutes=interval)
    return slots
