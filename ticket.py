#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Ticket:
    def __init__(self, visitor, event):
        assert isinstance(visitor, Visitor), "Invalid visitor"
        assert isinstance(event, Event), "Invalid event"
        
        self.visitor = visitor
        self.event = event
        self.price = self.calculate_ticket_price()

    def calculate_ticket_price(self):
        base_price = 63  # AED
        if self.visitor.is_student or self.visitor.is_teacher or self.visitor.age < 18 or self.visitor.age >= 60:
            return 0  # Free ticket for students, teachers, children, and seniors
        elif isinstance(self.visitor, GroupVisitor):
            return (base_price / 2) * 1.05  # 50% discount for group visitors
        elif isinstance(self.event, SpecialEvent):
            return (self.event.ticket_price) * 1.05
        else:
            return base_price * 1.05  # Full price for adults with 5% VAT

    def display(self):
        return f"Ticket Information:\nVisitor: {self.visitor.name}\nEvent: {self.event.name}\nLocation: {self.event.location.name}\nStart Time: {self.event.start_time.strftime('%Y-%m-%d %H:%M')}\nEnd Time: {self.event.end_time.strftime('%Y-%m-%d %H:%M')}\nTicket Price: {self.price} AED"

    def display_receipt(self):
        return f"Payment Receipt:\nVisitor: {self.visitor.name}\nEvent: {self.event.name}\nLocation: {self.event.location.name}\nPrice: {self.price} AED"

    
class VisitorInfoManagement:
    def __init__(self):
        self.visitors = []

    def add_visitor(self, visitor):
        assert isinstance(visitor, Visitor), "Invalid visitor"
        self.visitors.append(visitor)

    def remove_visitor(self, email):
        assert isinstance(email, str) and email.strip(), "Email must be a non-empty string"
        for visitor in self.visitors:
            if visitor.email == email:
                self.visitors.remove(visitor)
                return True
        return False

    def purchase_ticket(self, visitor, event):
        assert isinstance(visitor, Visitor), "Invalid visitor"
        assert isinstance(event, Event), "Invalid event"
        
        ticket = Ticket(visitor, event)
        return ticket

    def purchase_group_tickets(self, visitors, event):
        total_price = 0
        for visitor in visitors:
            ticket = Ticket(visitor, event)
            total_price += ticket.price
        return total_price

