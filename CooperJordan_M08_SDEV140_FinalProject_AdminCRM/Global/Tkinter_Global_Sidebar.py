import tkinter as tk
import Pages.Tkinter_Pages_Profile as prof
import Pages.Tkinter_Pages_Contacts as cntc
import Pages.Tkinter_Pages_Calendar as cal



"""Application Description:

This Python application is a tkinter-based graphical user interface (GUI) featuring a sidebar-based navigation system. It provides easy access to three main pages: "Profile," "Contacts," and "Calendar."

Profile Page: Displays a label with the text "Profile Page."

Contacts Page: Allows users to add, view, and sort contact information, including details like first name, last name, company, role, phone number, and email. It organizes entries in a "Treeview" widget and provides "Add Contact" and "Sort" functionalities.

Calendar Page: Enables the management of events associated with specific dates. Users can select dates using a calendar widget, input event descriptions, and utilize "Add Event" and "Sort" options to manage events by date. Event details are displayed in a text widget."""



# Define a base class for all pages
class Page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

# Define a class for the Profile Page
class ProfilePage(Page):
    def __init__(self, master=None):
        super().__init__(master)
        label = tk.Label(self, text="Profile Page")
        label.pack()

# Define a class for the Contacts Page
class ContactsPage(Page):
    def __init__(self, master=None):
        super().__init__(master)
        label = tk.Label(self, text="Contacts Page")
        label.pack()

# Define a class for the Calendar Page
class CalendarPage(Page):
    def __init__(self, master=None):
        super().__init__(master)
        label = tk.Label(self, text="Calendar Page")
        label.pack()

# Define a class for the Sidebar of the application
class SideBarApp:
    def __init__(self, root):
        self.root = root

        # Create and pack sidebar frames
        sidebar_y = tk.Frame(root, bg="lightgray", width=30)
        sidebar_y.pack(fill="y", side="left")

        sidebar_z = tk.Frame(root, bg="lightgray")
        sidebar_z.pack(fill="y", side="left")

        sidebar_x = tk.Frame(root, bg="lightgray", width=30)
        sidebar_x.pack(fill="y", side="left")

        # Create buttons for each page
        profile_button = tk.Button(sidebar_z, text="Profile", command=self.show_profile_page)
        contacts_button = tk.Button(sidebar_z, text="Contacts", command=self.show_contacts_page)
        calendar_button = tk.Button(sidebar_z, text="Calendar", command=self.show_calendar_page)

        profile_button.pack(fill="x", side="top", padx=30, pady=5)
        contacts_button.pack(fill="x", side="top", padx=30, pady=5)
        calendar_button.pack(fill="x", side="top", padx=30, pady=5)

        # Create a content area frame
        self.content = tk.Frame(self.root)
        self.content.pack(fill="both")

        # Initialize pages
        self.current_page = None

    # Show the Profile Page
    def show_profile_page(self):
        self.hide_current_page()
        self.current_page = prof.ProfileApp(self.content)

    # Show the Contacts Page
    def show_contacts_page(self):
        self.hide_current_page()
        self.current_page = cntc.ContactsPageApp(self.content)

    # Show the Calendar Page
    def show_calendar_page(self):
        self.hide_current_page()
        self.current_page = cal.CalendarPageApp(self.content)

    # Hide the current page if it exists
    def hide_current_page(self):
        if self.current_page:
            self.current_page.hide()

if __name__ == "__main__":
    root = tk.Tk()
    app = SideBarApp(root)
    root.mainloop()
