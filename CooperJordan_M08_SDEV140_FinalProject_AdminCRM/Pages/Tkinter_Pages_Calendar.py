import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

'''Application Description:

This Python application provides a user-friendly calendar page within a tkinter-based graphical user interface (GUI). The calendar page allows users to add and manage events with dates and descriptions.

Calendar Widget: The application includes a calendar widget that enables users to select dates for adding events. Users can click on a specific date on the calendar to choose it.

Event Management: Users can add events with a selected date and a corresponding event text. The "Add Event" button is used to input and save events, and events are stored as tuples (date, event_text) in a list.

Event Sorting: The application provides a "Sort" button to sort the events by date. Events are sorted in chronological order.

Event Display: A text widget is used to display the added events, showing the date and the event's text description. The display area is scrollable, providing an overview of all scheduled events.

Flexibility: Users can easily manage their events and ensure that they are sorted correctly.'''

# Define a class for the Calendar Page of the application
class CalendarPageApp:
    def __init__(self, root):
        self.root = root
        self.events = []

        # Create and pack GUI elements
        self.tkinterCalendar(root)
        self.title_display_addEventText(root)
        self.event_entry_box(root)
        self.event_adding_button(root)
        self.event_sorting_button(root)
        self.event_display = tk.Text(root, height=10, width=40)
        self.event_display.pack(pady=10)

    # Create a calendar widget for selecting dates
    def tkinterCalendar(self, root):
        self.cal = Calendar(root, selectmode='day')
        self.cal.pack(padx=10, pady=10)

    # Display a label instructing to add events by clicking on dates
    def title_display_addEventText(self, root):
        self.add_event_text = tk.Label(root, text="Click on the date to add an event")
        self.add_event_text.pack()

    # Create an entry box for entering event text
    def event_entry_box(self, root):
        self.event_entry = tk.Entry(root)
        self.event_entry.pack(pady=10)

    # Create a button to add events
    def event_adding_button(self, root):
        self.add_event_button = tk.Button(root, text="Add Event", command=self.add_event)
        self.add_event_button.pack(pady=10)

    # Create a button to sort events by date
    def event_sorting_button(self, root):
        self.events_sorter_button = tk.Button(root, text="Sort", command=self.sort_events)
        self.events_sorter_button.pack(pady=5)

    # Function to add events with date and text
    def add_event(self):
        selected_date = self.cal.get_date()
        selected_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y/%m/%d")
        event_text = self.event_entry.get()
        self.events.append((selected_date, event_text))
        self.event_entry.delete(0, tk.END)
        self.display_events()

    # Custom sorting function for events by date
    def custom_sort(self, event):
        date_str, _ = event
        date_obj = datetime.strptime(date_str, "%Y/%m/%d")
        return date_obj

    # Function to sort and display events
    def sort_events(self):
        self.events.sort(key=self.custom_sort)
        self.display_events()

    # Function to display events in the text widget
    def display_events(self):
        self.event_display.delete(1.0, tk.END)
        for date, event_text in self.events:
            formatted_date = datetime.strptime(date, "%Y/%m/%d").strftime("%m/%d/%y")
            self.event_display.insert(tk.END, f"{formatted_date}: {event_text}\n")

    # Hide or destroy all widgets and content associated with the CalendarPageApp
    def hide(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarPageApp(root)
    root.mainloop()
