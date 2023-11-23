from PIL import Image, ImageDraw

# add your images path to image_path_list as separate items 
image_path_list = ["assets/dog-1.jpg", "assets/dog-2.jpg", "assets/dog-3.jpg"]

image_list = [Image.open(img) for img in image_path_list]


image_list[0].save('animation.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=1000, # in milliseconds
            loop=0)


def ellipse(x, y, offset):
    image = Image.new("RGB", (400, 400), "blue")
    draw = ImageDraw.Draw(image)
    draw.ellipse((x, y, x+offset, y+offset), fill="red")
    return image


def make_gif():
    frames = []
    x = 0
    y = 0
    offset = 50
    for number in range(20):
        frames.append(ellipse(x, y, offset))
        x += 35
        y += 35
        
    frame_one = frames[0]
    frame_one.save("circle.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)
    

if __name__ == "__main__":
    make_gif()



"""
# import the modules
import glob
from PIL import Image

# Function to process images and make a gif from them
def make_gif(image_folder):
    '''
    This function takes image folder as parameter and returns a gif made from 
    these images

    param: str -> path
    return: gif
    '''

    # creates an array of images from the image folder 
    frames = [Image.open(image) for image in glob.glob(f"{image_folder}/*")]
    # creates gif face
    frame_one = frames[0]
    # 1 time 1000 milliseconds; creates a gif named download.gif
    frame_one.save("download.gif", format="GIF", append_images=frames,
                save_all=True, duration=1000, loop=1)

if __name__== "__main__":
    # if this .py file runs it automatically calls the function with given folder path
    f_path = input("Enter file path: ")
    try:
        make_gif(f_path)
    except:
        print("An error occured!")
"""