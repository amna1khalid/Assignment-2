#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
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

class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        assert isinstance(title, str) and title.strip(), "Title must be a non-empty string"
        assert isinstance(artist, str) and artist.strip(), "Artist must be a non-empty string"
        assert isinstance(date_of_creation, str) and date_of_creation.strip(), "Date of creation must be a non-empty string"
        assert isinstance(historical_significance, str) and historical_significance.strip(), "Historical significance must be a non-empty string"
        assert isinstance(exhibition_location, Location), "Invalid exhibition location"
        
        self.title = title.strip()
        self.artist = artist.strip()
        self.date_of_creation = date_of_creation.strip()
        self.historical_significance = historical_significance.strip()
        self.exhibition_location = exhibition_location

class ArtworkManagement:
    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork):
        assert isinstance(artwork, Artwork), "Invalid artwork"
        self.artworks.append(artwork)

    def remove_artwork(self, title):
        assert isinstance(title, str) and title.strip(), "Title must be a non-empty string"
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                return True
        return False

    def display_artworks(self):
        return [f"Title: {artwork.title}, Artist: {artwork.artist}, Date of Creation: {artwork.date_of_creation}, Historical Significance: {artwork.historical_significance}, Exhibition Location: {artwork.exhibition_location.name}" for artwork in self.artworks]

class Visitor:
    def __init__(self, name, age, email, is_student=False, is_teacher=False):
        assert isinstance(name, str) and name.strip(), "Name must be a non-empty string"
        assert isinstance(age, int) and age > 0, "Age must be a positive integer"
        assert isinstance(email, str) and '@' in email, "Invalid email address"
        
        self.name = name.strip()
        self.age = age
        self.email = email
        self.is_student = is_student
        self.is_teacher = is_teacher

class GroupVisitor(Visitor):
    def __init__(self, name, age, email, group_id):
        super().__init__(name, age, email)
        assert isinstance(group_id, str) and group_id.strip(), "Group ID must be a non-empty string"
        self.group_id = group_id.strip()

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

class EventManagement:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        assert isinstance(event, Event), "Invalid event"
        self.events.append(event)

    def remove_event(self, name):
        assert isinstance(name, str) and name.strip(), "Name must be a non-empty string"
        for event in self.events:
            if event.name == name:
                self.events.remove(event)
                return True
        return False

    def get_event_by_name(self, name):
        assert isinstance(name, str) and name.strip(), "Name must be a non-empty string"
        for event in self.events:
            if event.name == name:
                return event
        return None
    
class ArtworkManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Museum app")

        self.artwork_management = ArtworkManagement()
        self.visitor_info_management = VisitorInfoManagement()
        self.event_management = EventManagement()

        self.create_artwork_management_gui()
        self.create_event_management_gui()
        self.create_ticket_purchase_gui()


    def create_artwork_management_gui(self):
        artwork_frame = tk.LabelFrame(self.root, text="Artwork Management")
        artwork_frame.grid(row=0, column=0, padx=10, pady=10)

        label_title = tk.Label(artwork_frame, text="Title:")
        label_title.grid(row=0, column=0, padx=5, pady=5)

        self.entry_title = tk.Entry(artwork_frame)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5)

        label_artist = tk.Label(artwork_frame, text="Artist:")
        label_artist.grid(row=1, column=0, padx=5, pady=5)

        self.entry_artist = tk.Entry(artwork_frame)
        self.entry_artist.grid(row=1, column=1, padx=5, pady=5)

        label_date_of_creation = tk.Label(artwork_frame, text="Date of Creation:")
        label_date_of_creation.grid(row=2, column=0, padx=5, pady=5)

        self.entry_date_of_creation = tk.Entry(artwork_frame)
        self.entry_date_of_creation.grid(row=2, column=1, padx=5, pady=5)

        label_historical_significance = tk.Label(artwork_frame, text="Historical Significance:")
        label_historical_significance.grid(row=3, column=0, padx=5, pady=5)

        self.entry_historical_significance = tk.Entry(artwork_frame)
        self.entry_historical_significance.grid(row=3, column=1, padx=5, pady=5)

        label_location = tk.Label(artwork_frame, text="Location:")
        label_location.grid(row=4, column=0, padx=5, pady=5)

        self.location_var = tk.StringVar(artwork_frame)
        self.location_var.set("PERMANENT_GALLERIES")  # default value

        location_options = ["PERMANENT_GALLERIES", "EXHIBITION_HALLS", "OUTDOOR_SPACES"]
        self.location_menu = tk.OptionMenu(artwork_frame, self.location_var, *location_options)
        self.location_menu.grid(row=4, column=1, padx=5, pady=5)

        add_button = tk.Button(artwork_frame, text="Add Artwork", command=self.add_artwork)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.artwork_text = tk.Text(artwork_frame, width=50, height=10)
        self.artwork_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_artwork(self):
        title = self.entry_title.get()
        artist = self.entry_artist.get()
        date_of_creation = self.entry_date_of_creation.get()
        historical_significance = self.entry_historical_significance.get()
        location = Location[self.location_var.get()]

        if title.strip() == "":
            messagebox.showerror("Error", "Title cannot be empty.")
            return
        if artist.strip() == "":
            messagebox.showerror("Error", "Artist cannot be empty.")
            return
        if date_of_creation.strip() == "":
            messagebox.showerror("Error", "Date of creation cannot be empty.")
            return
        if historical_significance.strip() == "":
            messagebox.showerror("Error", "Historical significance cannot be empty.")
            return

        try:
            artwork = Artwork(title, artist, date_of_creation, historical_significance, location)
            self.artwork_management.add_artwork(artwork)
            self.artwork_text.insert(tk.END, f"Title: {artwork.title}\nArtist: {artwork.artist}\nDate of Creation: {artwork.date_of_creation}\nHistorical Significance: {artwork.historical_significance}\nExhibition Location: {artwork.exhibition_location.name}\n\n")
            messagebox.showinfo("Success", "Artwork added successfully.")
        except AssertionError as e:
            messagebox.showerror("Error", str(e))

    def create_event_management_gui(self):
        event_frame = tk.LabelFrame(self.root, text="Event Management")
        event_frame.grid(row=0, column=1, padx=10, pady=10)

        self.event_listbox = tk.Listbox(event_frame, width=50, height=10)
        self.event_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        add_button = tk.Button(event_frame, text="Add Event", command=self.add_event)
        add_button.grid(row=1, column=0, padx=5, pady=5)

        remove_button = tk.Button(event_frame, text="Remove Event", command=self.remove_event)
        remove_button.grid(row=1, column=1, padx=5, pady=5)

    def add_event(self):
        event_window = tk.Toplevel()
        event_window.title("Add Event")

        label_name = tk.Label(event_window, text="Event Name:")
        label_name.grid(row=0, column=0, padx=5, pady=5)

        entry_name = tk.Entry(event_window)
        entry_name.grid(row=0, column=1, padx=5, pady=5)

        label_location = tk.Label(event_window, text="Location:")
        label_location.grid(row=1, column=0, padx=5, pady=5)

        location_var = tk.StringVar(event_window)
        location_var.set("PERMANENT_GALLERIES")  # default value

        location_options = ["PERMANENT_GALLERIES", "EXHIBITION_HALLS", "OUTDOOR_SPACES"]
        location_menu = tk.OptionMenu(event_window, location_var, *location_options)
        location_menu.grid(row=1, column=1, padx=5, pady=5)

        label_start_time = tk.Label(event_window, text="Start Time (YYYY-MM-DD HH:MM):")
        label_start_time.grid(row=2, column=0, padx=5, pady=5)

        entry_start_time = tk.Entry(event_window)
        entry_start_time.grid(row=2, column=1, padx=5, pady=5)

        label_end_time = tk.Label(event_window, text="End Time (YYYY-MM-DD HH:MM):")
        label_end_time.grid(row=3, column=0, padx=5, pady=5)

        entry_end_time = tk.Entry(event_window)
        entry_end_time.grid(row=3, column=1, padx=5, pady=5)

        add_button = tk.Button(event_window, text="Add", command=lambda: self.save_event(entry_name.get(), location_var.get(), entry_start_time.get(), entry_end_time.get()))
        add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def save_event(self, name, location, start_time, end_time):
        try:
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
            event = Event(name, Location[location], start_time, end_time)
            self.event_management.add_event(event)
            self.event_listbox.insert(tk.END, f"{event.name} - {event.start_time.strftime('%Y-%m-%d %H:%M')}")
            messagebox.showinfo("Success", "Event added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD HH:MM.")

    def remove_event(self):
        selected_index = self.event_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an event to remove.")
            return
        event_info = self.event_listbox.get(selected_index)
        event_name = event_info.split(" - ")[0]
        if self.event_management.remove_event(event_name):
            self.event_listbox.delete(selected_index)
            messagebox.showinfo("Success", "Event removed successfully.")
        else:
            messagebox.showerror("Error", "Event not found.")

    def create_ticket_purchase_gui(self):
        ticket_frame = tk.LabelFrame(self.root, text="Ticket Purchase")
        ticket_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        label_ticket_type = tk.Label(ticket_frame, text="Ticket Type:")
        label_ticket_type.grid(row=0, column=0, padx=5, pady=5)

        self.ticket_type_var = tk.StringVar(ticket_frame)
        self.ticket_type_var.set("Individual")  # default value

        ticket_type_options = ["Individual", "Group"]
        self.ticket_type_menu = tk.OptionMenu(ticket_frame, self.ticket_type_var, *ticket_type_options)
        self.ticket_type_menu.grid(row=0, column=1, padx=5, pady=5)

        label_event_name = tk.Label(ticket_frame, text="Event Name:")
        label_event_name.grid(row=1, column=0, padx=5, pady=5)

        self.entry_event_name = tk.Entry(ticket_frame)
        self.entry_event_name.grid(row=1, column=1, padx=5, pady=5)

        purchase_button = tk.Button(ticket_frame, text="Next", command=self.ticket_purchase_next_step)
        purchase_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def ticket_purchase_next_step(self):
        ticket_type = self.ticket_type_var.get()
        event_name = self.entry_event_name.get()

        if event_name.strip() == "":
            messagebox.showerror("Error", "Event name cannot be empty.")
            return

        if ticket_type == "Individual":
            self.individual_ticket_purchase(event_name)
        else:
            self.group_ticket_purchase(event_name)

    def individual_ticket_purchase(self, event_name):
        event = self.event_management.get_event_by_name(event_name)

        if event is None:
            messagebox.showerror("Error", "Event not found.")
            return

        ticket_window = tk.Toplevel()
        ticket_window.title("Individual Ticket Purchase")

        label_visitor_name = tk.Label(ticket_window, text="Visitor Name:")
        label_visitor_name.grid(row=0, column=0, padx=5, pady=5)

        entry_visitor_name = tk.Entry(ticket_window)
        entry_visitor_name.grid(row=0, column=1, padx=5, pady=5)

        label_visitor_age = tk.Label(ticket_window, text="Visitor Age:")
        label_visitor_age.grid(row=1, column=0, padx=5, pady=5)

        entry_visitor_age = tk.Entry(ticket_window)
        entry_visitor_age.grid(row=1, column=1, padx=5, pady=5)

        label_visitor_email = tk.Label(ticket_window, text="Visitor Email:")
        label_visitor_email.grid(row=2, column=0, padx=5, pady=5)

        entry_visitor_email = tk.Entry(ticket_window)
        entry_visitor_email.grid(row=2, column=1, padx=5, pady=5)

        purchase_button = tk.Button(ticket_window, text="Purchase Ticket", command=lambda: self.purchase_individual_ticket(event, entry_visitor_name.get(), entry_visitor_age.get(), entry_visitor_email.get()))
        purchase_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def purchase_individual_ticket(self, event, visitor_name, visitor_age, visitor_email):
        if visitor_name.strip() == "":
            messagebox.showerror("Error", "Visitor name cannot be empty.")
            return
        if not visitor_age.isdigit() or int(visitor_age) <= 0:
            messagebox.showerror("Error", "Visitor age must be a positive integer.")
            return
        if visitor_email.strip() == "" or '@' not in visitor_email:
            messagebox.showerror("Error", "Invalid email address.")
            return

        visitor = Visitor(visitor_name, int(visitor_age), visitor_email)
        ticket = self.visitor_info_management.purchase_ticket(visitor, event)
        messagebox.showinfo("Ticket Information", f"Ticket Price: {ticket.price} AED")
        confirm_button = tk.Button(self.root, text="Confirm Individual Purchase", command=lambda: self.display_ticket_and_receipt(ticket))
        confirm_button.grid(row=2, column=0, padx=10, pady=10)

    def group_ticket_purchase(self, event_name):
        event = self.event_management.get_event_by_name(event_name)

        if event is None:
            messagebox.showerror("Error", "Event not found.")
            return

        group_ticket_window = tk.Toplevel()
        group_ticket_window.title("Group Ticket Purchase")

        label_group_id = tk.Label(group_ticket_window, text="Group ID:")
        label_group_id.grid(row=0, column=0, padx=5, pady=5)

        entry_group_id = tk.Entry(group_ticket_window)
        entry_group_id.grid(row=0, column=1, padx=5, pady=5)

        label_num_members = tk.Label(group_ticket_window, text="Number of Members:")
        label_num_members.grid(row=1, column=0, padx=5, pady=5)

        entry_num_members = tk.Entry(group_ticket_window)
        entry_num_members.grid(row=1, column=1, padx=5, pady=5)

        add_members_button = tk.Button(group_ticket_window, text="Add Members", command=lambda: self.add_group_members(group_ticket_window, event, entry_group_id.get(), entry_num_members.get()))
        add_members_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def add_group_members(self, window, event, group_id, num_members):
        if group_id.strip() == "":
            messagebox.showerror("Error", "Group ID cannot be empty.")
            return
        if not num_members.isdigit() or int(num_members) <= 0:
            messagebox.showerror("Error", "Number of members must be a positive integer.")
            return

        num_members = int(num_members)
        group_members_window = tk.Toplevel(window)
        group_members_window.title("Add Group Members")

        label_members = tk.Label(group_members_window, text="Enter Visitor Information for Each Member:")
        label_members.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.group_members_entries = []
        for i in range(num_members):
            label_name = tk.Label(group_members_window, text=f"Visitor {i+1} Name:")
            label_name.grid(row=i+1, column=0, padx=5, pady=5)

            entry_name = tk.Entry(group_members_window)
            entry_name.grid(row=i+1, column=1, padx=5, pady=5)

            label_age = tk.Label(group_members_window, text=f"Visitor {i+1} Age:")
            label_age.grid(row=i+num_members+1, column=0, padx=5, pady=5)

            entry_age = tk.Entry(group_members_window)
            entry_age.grid(row=i+num_members+1, column=1, padx=5, pady=5)

            label_email = tk.Label(group_members_window, text=f"Visitor {i+1} Email:")
            label_email.grid(row=i+2*num_members+1, column=0, padx=5, pady=5)

            entry_email = tk.Entry(group_members_window)
            entry_email.grid(row=i+2*num_members+1, column=1, padx=5, pady=5)

            self.group_members_entries.append((entry_name, entry_age, entry_email))

        purchase_button = tk.Button(group_members_window, text="Purchase Tickets", command=lambda: self.purchase_group_tickets(event, group_id))
        purchase_button.grid(row=3*num_members+1, column=0, columnspan=2, padx=5, pady=5)

    def purchase_group_tickets(self, event, group_id):
        visitors = []
        for entry_name, entry_age, entry_email in self.group_members_entries:
            name = entry_name.get()
            age = entry_age.get()
            email = entry_email.get()
            if name.strip() == "" or not age.isdigit() or int(age) <= 0 or email.strip() == "" or '@' not in email:
                messagebox.showerror("Error", "Invalid visitor information.")
                return
            visitor = GroupVisitor(name, int(age), email, group_id)
            visitors.append(visitor)
        total_price = self.visitor_info_management.purchase_group_tickets(visitors, event)
        messagebox.showinfo("Total Price", f"Total Price for the Group: {total_price} AED")
        confirm_button = tk.Button(self.root, text="Confirm Group Purchase", command=lambda: self.display_group_tickets_and_receipt(visitors, event))
        confirm_button.grid(row=2, column=1, padx=10, pady=10)

    def display_ticket_and_receipt(self, ticket):
        messagebox.showinfo("Ticket Information", ticket.display())
        messagebox.showinfo("Payment Receipt", ticket.display_receipt())

    def display_group_tickets_and_receipt(self, visitors, event):
        for visitor in visitors:
            ticket = Ticket(visitor, event)
            messagebox.showinfo("Ticket Information", ticket.display())
            messagebox.showinfo("Payment Receipt", ticket.display_receipt())



root = tk.Tk()
app = ArtworkManagementApp(root)
root.mainloop()


# In[ ]:




