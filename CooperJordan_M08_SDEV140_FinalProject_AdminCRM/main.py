import tkinter as tk
import Global.Tkinter_Global_Topbar as tb
import Global.Tkinter_Global_Sidebar as sb

'''Application Description:

This Python application provides a framework for a main app with a graphical user interface (GUI). The application structure includes a top bar and a sidebar for easy navigation and interaction.

Top Bar: The top bar serves as a navigation and control area for the application. It typically contains user-specific information and options. Users can access features and information through the top bar.

Sidebar: The sidebar offers an additional navigation method for the application. It contains buttons or links to various modules or sections of the application. Users can click on these buttons to access specific features or pages.

Main Page: The main page is the default landing page when the application is launched. It is used to display essential information about the application or a welcome message. In this example, it simply displays "Main App Page."

Content Area: The application includes a content area where different pages or modules can be displayed. The MainApp class controls this area and allows switching between the top bar and sidebar for different functionalities.

Customization and Expansion: The application framework is designed to be customized and expanded further. You can add more modules, pages, and features to meet the specific needs of your application.

User Interaction: Users can interact with the application through the top bar and sidebar, enabling them to access different parts of the application and perform various tasks.'''

# Define a base class for pages in your app
class Page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

# Define the main page class that inherits from Page
class MainPage(Page):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        label = tk.Label(self, text="Main App Page")
        label.pack()

# Create the main app class
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")

        # Create a content area for module command windows
        self.content = tk.Frame(self.root, bg="white")
        self.content.pack(fill="both", expand=True)

        # The current_page attribute is used to track the currently displayed page
        self.current_page = None

        # Creates and establishes the frames for the respective modules, topbar, and sidebar
        self.top_bar = tb.TopBarApp(self.content)  # TopBarApp and SideBarApp are assumed to be defined in other modules
        self.side_bar = sb.SideBarApp(self.content)

    # Switch the displayed page to the Top Bar
    def displayTB(self):
        self.current_page = self.top_bar

    # Switch the displayed page to the Side Bar
    def displaySB(self):
        self.current_page = self.side_bar

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)  # Create the MainApp instance
    root.mainloop()
