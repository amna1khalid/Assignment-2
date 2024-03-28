#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import Enum
from datetime import datetime

class Location(Enum):
    PERMANENT_GALLERIES = 1
    EXHIBITION_HALLS = 2
    OUTDOOR_SPACES = 3

class Event:
    def __init__(self, name, location, start_time, end_time):
        assert isinstance(name, str) and name.strip(), "Name must be a non-empty string"
        assert isinstance(location, Location), "Invalid location"
        assert isinstance(start_time, datetime) and isinstance(end_time, datetime), "Invalid start or end time"
        assert start_time < end_time, "Start time must be before end time"
        
        self.name = name.strip()
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

    def display_event_info(self):
        return f"Name: {self.name}\nLocation: {self.location.name}\nStart Time: {self.start_time.strftime('%Y-%m-%d %H:%M')}\nEnd Time: {self.end_time.strftime('%Y-%m-%d %H:%M')}"

class Exhibition(Event):
    def __init__(self, name, location, start_time, end_time):
        super().__init__(name, location, start_time, end_time)

class Tour(Event):
    def __init__(self, name, location, start_time, end_time, max_capacity):
        super().__init__(name, location, start_time, end_time)
        assert isinstance(max_capacity, int) and max_capacity > 0, "Max capacity must be a positive integer"
        self.max_capacity = max_capacity

class SpecialEvent(Event):
    def __init__(self, name, location, start_time, end_time, ticket_price):
        super().__init__(name, location, start_time, end_time)
        assert isinstance(ticket_price, (int, float)) and ticket_price >= 0, "Ticket price must be a non-negative number"
        self.ticket_price = ticket_price


# In[ ]:




