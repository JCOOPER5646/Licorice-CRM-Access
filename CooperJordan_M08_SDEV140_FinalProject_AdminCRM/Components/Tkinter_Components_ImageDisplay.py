import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

'''Application Description:

This Python application is a custom image component that creates a circular image display within a Tkinter canvas. It's particularly useful for displaying profile pictures or circular images. Here's a breakdown of its functionality:

Circular Canvas: The application creates a circular canvas to display images. It uses the Canvas widget from Tkinter to define the canvas's dimensions and shape.

Image Loading: The app loads two images, 'JohnSmith1.jpg' and 'JohnSmith2.jpg', which are assumed to be profile pictures. These images are opened using the Python Imaging Library (PIL), known as Pillow.

Image Resizing: The images are resized to fit the circular canvas. They are scaled to have the same dimensions as the canvas for a clean display.

Circular Mask: The circular shape is applied to the images using a circular mask. This mask ensures that the images are displayed within the circular canvas. Any parts of the image outside the circular region are transparent.

Display Images: The images are displayed on the canvas as PhotoImage objects, which are compatible with Tkinter. Two labels are created to display the images on the canvas, and these labels are associated with the PhotoImage objects.

Customization: The app is designed to work with two specific images, 'JohnSmith1.jpg' and 'JohnSmith2.jpg'. You can modify the code to work with your preferred images by replacing the file paths in the image_open method. You can also customize the canvas size by adjusting self.canvas_width and self.canvas_height.

User Interface: While this application does not have a user interface of its own, it can be integrated into a larger application or used as part of a user profile display.'''



class ImageComponentApp(tk.Canvas):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root

        # Initialize image_tk_1 and image_tk_2 as instance variables
        self.image_tk_1 = None
        self.image_tk_2 = None

        # Initialize canvas and images
        self.image_circular_canvas()
        self.image_open()
        self.image_resize()
        self.image_object1()
        self.image_object2()
       

        self.content = tk.Frame (self.root, bg = "white")
        self.content.pack(fill = "both", side = "right" , expand = True)

        self.current_page = None

    def image_circular_canvas(self):
        # Create a circular canvas to display the image

        # Canvas measurements
        self.canvas_width = 40
        self.canvas_height = 40
        self.canvas_center_x = self.canvas_width // 2
        self.canvas_center_y = self.canvas_height // 2
        self.radius = min(self.canvas_center_x, self.canvas_center_y) 

        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(fill = "x" , side = "top")


        # Create a circular background by drawing an oval
        self.canvas_circle = self.canvas.create_oval(
            self.canvas_center_x - self.radius, self.canvas_center_y - self.radius,
            self.canvas_center_x + self.radius, self.canvas_center_y + self.radius,
            outline="lightgray", width=2
        )

        # Circle Object method
        self.configure(bg="white", highlightthickness=0)



    def image_open(self):
        # Open the image file
        self.image_1 = Image.open(r"C:\Users\Owner\OneDrive\Desktop\python.files\CooperJordan_M08_SDEV140_FinalProject_AdminCRM\Media\JohnSmith1.jpg")
        self.image_2 = Image.open(r"C:\Users\Owner\OneDrive\Desktop\python.files\CooperJordan_M08_SDEV140_FinalProject_AdminCRM\Media\JohnSmith1.jpg")

    def image_resize(self):
        # Resize the Image to fit the circular canvas
        self.image_1 = self.image_1.resize((2 * self.radius, 2 * self.radius), Image.BILINEAR)
        self.image_2 = self.image_2.resize((2 * self.radius, 2 * self.radius), Image.BILINEAR)

    def apply_circle_mask(self, image):
        # Create a circular mask
        mask = Image.new("L", (2 * self.radius, 2 * self.radius), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 2 * self.radius, 2 * self.radius), fill=255)

        # Apply the circular mask to the image
        image.putalpha(mask)
        return image


    def image_object1(self):
        # Apply circular mask to the first image
        self.image_1 = self.apply_circle_mask(self.image_1)
        # Convert the first image to PhotoImage objects
        self.image_tk_1 = ImageTk.PhotoImage(self.image_1)
        # Create labels to display the first image on the canvas
        self.image_label_1 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk_1)

    def image_object2(self):
        # Apply circular mask to the second image
        self.image_2 = self.apply_circle_mask(self.image_2)
        # Convert the second image to PhotoImage objects
        self.image_tk_2 = ImageTk.PhotoImage(self.image_2)
        #Create the labels to display the second image
        self.image_label_2 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk_2)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageComponentApp(root)
    root.mainloop()
