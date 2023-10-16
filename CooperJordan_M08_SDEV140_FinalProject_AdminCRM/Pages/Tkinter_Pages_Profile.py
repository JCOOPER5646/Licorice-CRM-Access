import tkinter as tk
from tkinter import ttk
import Components.Tkinter_Components_ImageDisplay
from tkinter import messagebox


'''Application Description:

This Python application presents a graphical user interface (GUI) for managing and customizing a profile. It primarily consists of a top bar for user information and the ability to select a profile photo.

Top Bar Display: The top bar in the application showcases the user's name and provides an area to display a profile picture. Users are greeted with "Hello, John Smith" in this section, and a profile picture can be set or changed.

Profile Photo Selection: Users can select a profile photo from a set of available options using radio buttons. Images, such as "JohnSmith1.jpg" and "JohnSmith2.jpg," are presented for selection. A "Set as profile photo" button allows users to set the selected image as their profile picture.

Profile Data Display: The application displays the user's profile information in a Treeview widget. The initial profile information includes details like name, company, role, phone number, and email.

Flexibility and Customization: Users have the flexibility to choose and set a profile photo that represents them. They can change it whenever they desire, providing a more personalized touch to their profile.

Data Management: The profile data is displayed in a structured and organized manner, making it easy for users to review and customize their profile.

This application is well-suited for providing a user-friendly interface for managing personal or professional profiles. Users can personalize their profiles by selecting and setting profile photos, creating a more engaging and customized user experience.'''



# Define a class for the top bar of the application
class TopBarApp:
    def __init__(self, root):
        self.root = root
        self.content = tk.Frame(self.root)
        self.content.pack(fill="both")

        self.image_label = tk.Label(self.content)
        self.image_label.pack(fill="both", expand=True)
        self.topbar()

        self.current_page = None

    # Display the top bar content
    def topbar(self, image=None):
        self.title = tk.Label(self.image_label, text="Hello, John Smith", bg="lightgray", fg="white")
        self.title.pack()

        if image:
            # Set the image as the profile photo
            image = RadioButtonsApp.set_as_profile_photo(image)
            self.image_label.config(image=image)
            self.image_label.image = image

    # Hide all widgets in the top bar
    def hide(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Hide the current page if it exists
    def hide_current_page(self):
        if self.current_page:
            self.current_page.hide()

# Define a class for the profile application
class ProfileApp:
    def __init__(self, root):
        self.root = root
        self.files = None
        self.pictures = []  # Initialize pictures here

        self.selected_option = tk.StringVar()
        self.top_bar = TopBarApp(self.root)

        self.profileID_tree()
        self.change_option_Button()

        self.content = tk.Frame(self.root)
        self.content.pack(fill="both")

        self.current_page = None
        self.items = []

    # Add an item to the profile
    def add_item(self):
        TopBar_data = TopBarApp()
        if TopBar_data:
            self.items.append(TopBar_data)
            TopBarApp().destroy()
            self.update_display()

    # Update the displayed profile items
    def update_display(self):
        if self.items:
            self.profileID_tree.set(self.items[-1])  # Current items are the Profile Tree Data

    # Create the profile tree
    def profileID_tree(self):
        self.selected_option = tk.StringVar()  # Create a StringVar to store the selected option
        self.identifiers = [
            ["John Smith", "Dunder Mifflin Paper", "Sales Executive", "123-456-7890", "johnsmith@example.com"]
        ]

        self.tree = ttk.Treeview(self.root, columns=("Info"), show="headings")
        self.tree.pack(pady=10)
        self.tree.heading("Info", text="Profile Information")

        for data in self.identifiers:
            info = "\n".join(data)
            self.tree.insert("", "end", values=(info,))

    # Create a button to change profile photo
    def change_option_Button(self):
        self.change_option_button = tk.Button(self.root, text="Profile Photo Library", command=self.radio_button_image_page)
        self.change_option_button.pack()

    # Handle the profile photo selection
    def radio_button_image_page(self):
        self.hide_current_page()

        try:
            self.current_page = RadioButtonsApp(self.content, self.profileID_tree, self.change_option_Button, self.pictures, self.files)
            self.change_option_button.forget()
            self.tree.pack_forget()
        except (TypeError, AttributeError) as e:
            print(f"An exception occurred: {e}")

    # Hide all widgets in the profile app
    def hide(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Hide the current page if it exists
    def hide_current_page(self):
        if self.current_page:
            self.current_page.hide()

# Define a class for radio buttons to select profile photos
class RadioButtonsApp:
    def __init__(self, root, profileID_tree_function, change_option_Button_function, pictures, files):
        self.root = root
        self.profileID_tree_function = profileID_tree_function  # Reference to profileID_tree # Root
        self.change_option_Button_function = change_option_Button_function  # Root
        self.pictures = pictures
        self.files = files
        pictures = []

        self.selected_option = tk.StringVar()

        self.create_radio_buttons()
        self.set_as_button()
        self.frame_widget()

        self.content = tk.Frame(self.root)
        self.content.pack(fill="both")

        self.image_label = tk.Label(self.content)
        self.image_label.pack()

        self.current_page = None

    # Create a frame widget
    def frame_widget(self):
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(side="left")

    # Create radio buttons for image selection
    def create_radio_buttons(self):
        self.selected_option.set("")  # Initialize selected option
        self.JohnSmith1_button = tk.Radiobutton(self.root, text="JohnSmith1.jpg", variable=self.selected_option, value="JohnSmith1")
        self.JohnSmith1_button.pack(side='top', pady=10)

        self.JohnSmith2_button = tk.Radiobutton(self.root, text="JohnSmith2.jpg", variable=self.selected_option, value="JohnSmith2")
        self.JohnSmith2_button.pack(side='top', pady=10)

    # Create a button to set the selected image as a profile photo
    def set_as_button(self):
        self.change_option_button = tk.Button(self.root, text="Set as profile photo", command=self.set_as_profile_photo)
        self.change_option_button.pack(side='top', pady=10)

    # Set the selected image as the profile photo
    def set_as_profile_photo(self):
        selected_option = self.selected_option.get()
        self.JohnSmith1_button.destroy()
        self.JohnSmith2_button.destroy()
        self.change_option_button.destroy()
        if selected_option:
            self.pictures.append(selected_option)

            if self.pictures:
                last_selected_picture = self.pictures[-1]
                file = Components.Tkinter_Components_ImageDisplay.ImageComponentApp(self.root)

                if last_selected_picture == "JohnSmith1":
                    image = file.image_object1()
                elif last_selected_picture == "JohnSmith2":
                    image = file.image_object2()
                else:
                    return

        self.display_ID()
        self.topbar(image)

    # Display the profile information
    def display_ID(self):
        self.profileID_tree_function()
        self.change_option_Button_function()

    # Hide all widgets in the radio buttons app
    def hide(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
