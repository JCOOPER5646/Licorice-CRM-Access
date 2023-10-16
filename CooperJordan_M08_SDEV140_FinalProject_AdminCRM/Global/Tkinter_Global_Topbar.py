import tkinter as tk
import Buttons.Tkinter_Buttons_RadioButtons as Tkinter_Buttons_RadioButtons


'''Application Description:

This Python application features a tkinter-based graphical user interface (GUI) for a top bar with a profile picture functionality. It provides a simple layout with a light gray top bar at the top of the window.

Top Bar: The top bar contains a label with the text "Hello, John Smith." This area serves as a header for the application.

Profile Picture Flexibility: The application allows the user to manage their profile picture. When the "profile_picture_flex" method is invoked, it opens a component provided by "Tkinter_Buttons_RadioButtons," which likely allows users to select or change their profile picture. The selected profile picture is then displayed within the top bar area.'''

class Page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

class TopBarApp (tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

    
        # Create a Top frame (light blue top bar)
        self.topBar_x = tk.Frame(root, bg="lightgray", height=100, width=100)
        self.topBar_x.pack(fill="x", side="top")

        self.topBar_y = tk.Frame(root, bg="lightgray", height=40)
        self.topBar_y.pack(fill="x", side="top")

        # Create a frame for the label
        self.label_frame = tk.Frame(self.topBar_x, height=10)
        self.label_frame.pack(side="top" )

        # Header Label
        self.title = tk.Label(self.label_frame, text="Hello, John Smith", bg="lightgray", fg="white")
        self.title.pack()

        
     
      
    def profile_picture_flex(self):

        self.profile_image_widget = Tkinter_Buttons_RadioButtons.RadioButtonsApp(self.root)  # Pass self.topBar_x as the parent
        self.profile_pictures = self.profile_image_widget.choose_open_file()
        # Position the profile image label in the top left corner
        
        
                
        




if __name__ == "__main__":
    root = tk.Tk()
    app = TopBarApp(root)
    root.mainloop()
