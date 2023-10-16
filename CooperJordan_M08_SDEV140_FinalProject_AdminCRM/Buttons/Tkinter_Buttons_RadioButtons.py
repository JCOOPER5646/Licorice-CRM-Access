import tkinter as tk
from tkinter import messagebox
import Components.Tkinter_Components_ImageDisplay 




'''Application Description:

This Python application allows users to select and display one of two profile images by using radio buttons. It's a part of a larger application where users can set their profile picture. Here's a description of its functionality:

Radio Buttons: The application provides two radio buttons: "JohnSmith1.jpg" and "JohnSmith2.jpg." Users can select one of these options.

Set as Profile Photo: A "Set as profile photo" button allows users to set the selected image as their profile picture.

Dynamic Display: When an image is selected, the application dynamically displays the chosen image on the window. The previously displayed image is removed, and the new image is shown. This creates a user-friendly interface for setting a profile picture.

Integration: The application can be integrated into a larger application or user profile section. It allows users to choose from predefined profile images and easily update their profile picture.

Error Handling: The application includes basic error handling. If there is an issue opening the image, it shows an error message using the messagebox from Tkinter.

Customization: While this application is set up to work with the images "JohnSmith1.jpg" and "JohnSmith2.jpg," you can customize it to work with other profile images by replacing the file paths in the choose_open_file method. You can add additional radio buttons and images to suit your needs.

'''



class Page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

class ImagePage(Page):
    def __init__(self, master=None):
        super().__init__(master)
        label = tk.Label(self, text="Image Page")
        label.pack()


class RadioButtonsApp (tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self , root)
        self.root = root
        self.selected_option = tk.StringVar()
        
        # Create and pack GUI elements
        
        self.create_radio_buttons()
        self.set_as_button()
        self.frame_widget()
        self.choose_open_file()
        

        self.content = tk.Frame(self.root  )
        self.content.pack(fill="both")

        # Initialize an empty label to display the selected image
        self.image_label = tk.Label(self.content)
        self.image_label.pack()

        # Initialize instances of ImageComponentApp with None as the initial image
        self.topbar_content = None
        self.file = None
   

    def create_radio_buttons(self):
        # Create radio buttons for image selection
        self.JohnSmith1_button = tk.Radiobutton(self.root, text="JohnSmith1.jpg", variable=self.selected_option, value="JohnSmith1")
        self.JohnSmith1_button.pack(side = 'top', pady=10)

        self.JohnSmith2_button = tk.Radiobutton(self.root, text="JohnSmith2.jpg", variable=self.selected_option, value="JohnSmith2")
        self.JohnSmith2_button.pack(side = 'top' , pady=10)

    def set_as_button(self):
        # Create a button to set the selected image as a profile photo
        self.change_option_button = tk.Button(self.root, text="Set as profile photo", command=self.choose_open_file)
        self.change_option_button.pack(side = 'top' , pady=10)


    def frame_widget(self):
        self.image_frame = tk.Frame(self)
        self.image_frame.pack (side = "left")


        
    def choose_open_file(self):

#Display contents inside topbar
        selected_option = self.selected_option.get()

        if selected_option:
            try:
                 # Destroy any previously displayed image frame
                for widget in self.image_frame.winfo_children():
                    widget.destroy()

                # Create a new frame to display the image
                self.image_display_frame = tk.Frame(self.image_frame)
                self.image_display_frame.pack(side = "left")


                if selected_option == "JohnSmith1":
                    # Call methods for image 1
                    self.file = Components.Tkinter_Components_ImageDisplay.ImageComponentApp(self.root)
                    self.picture_1 = self.file.image_object1()
                    self.image_display_frame = self.picture_1

                elif selected_option == "JohnSmith2":
                    # Call methods for image 2
                    self.file = Components.Tkinter_Components_ImageDisplay.ImageComponentApp(self.root)
                    self.picture_2 = self.file.image_object2()
                    self.image_display_frame = self.picture_2

                self.JohnSmith1_button.forget()
                self.JohnSmith2_button.forget()
                self.change_option_button.forget()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {str(e)}")


    def hide(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = RadioButtonsApp(root)
    root.mainloop()





