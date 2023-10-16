import tkinter as tk
from tkinter import ttk

'''Application Description:

This Python application provides a Contacts Page within a tkinter-based graphical user interface (GUI). The Contacts Page allows users to manage and display contact information efficiently.

Contact Entry Form: The application provides a user-friendly interface to input and save contact details. Users can enter various fields such as first name, last name, company, role, phone number, and email.

Treeview Widget: Contacts are displayed in a tabular format using a ttk.Treeview widget. Each contact is represented as a row with columns for different attributes. The Treeview widget enables users to view and manage contact information effectively.

Add Contact Button: Users can add new contacts by clicking the "Add Contact +" button. This action opens a contact entry page where users can input the details for a new contact.

Data Management: Contact data is stored in the Treeview widget, and new contacts are appended as rows. The "Save" button allows users to add a contact, and the application automatically updates the display.

Scrollbar: A horizontal scrollbar is provided to allow users to navigate through the contact list easily.

Flexibility: Users can conveniently add, view, and manage contact details in a structured and organized manner.'''


# Define a class for the Contacts Page of the application
class ContactsPageApp:
    def __init__(self, root):
        self.root = root
        self.fields = ["Enter a First Name:", "Enter a Last Name:", "Enter a Company:", "Enter a Role:", "Enter a Phone Number:", "Enter an Email:"]
        self.field_entries = ["First Name", "Last Name", "Company", "Role", "Phone Number", "Email"]
        self.contact_entry_widgets = []

        # Create a Treeview widget to display contacts with specified columns
        self.contacts_tree = ttk.Treeview(root, columns=self.field_entries, show="headings")
        self.contacts_tree.pack(pady=10)

        # Set column headings for the Treeview
        for field in self.field_entries:
            self.contacts_tree.heading(field, text=field)

        # Create a button to add a new contact
        self.add_contact_button = tk.Button(root, text="Add Contact +", command=self.contacts_entry_page)
        self.add_contact_button.pack(pady=10)

        # Create a horizontal scrollbar for the Treeview
        self.x_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
        self.x_scrollbar.pack(fill=tk.X)
        self.contacts_tree.configure(xscrollcommand=self.x_scrollbar.set)
        self.x_scrollbar.config(command=self.contacts_tree.xview)

    # Create a page for entering contact details
    def contacts_entry_page(self):
        for field in self.fields:
            label = tk.Label(self.root, text=field)
            label.pack()
            entry = tk.Entry(self.root)
            entry.pack(pady=5)
            self.contact_entry_widgets.append(entry)

        save_button = tk.Button(self.root, text="Save", command=self.save_contact)
        save_button.pack(pady=10)

    # Save contact details entered by the user
    def save_contact(self):
        contact_data = [entry.get() for entry in self.contact_entry_widgets]
        self.contacts_tree.insert("", tk.END, values=contact_data)
        self.clear_entry_fields()

    # Clear the entry fields after saving a contact
    def clear_entry_fields(self):
        for entry in self.contact_entry_widgets:
            entry.delete(0, tk.END)

    # Hide or destroy all widgets and content associated with the ContactsPageApp
    def hide(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactsPageApp(root)
    root.mainloop()
