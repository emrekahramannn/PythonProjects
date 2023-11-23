# import 
from rembg import remove


def TakePaths():
    """
        This function takes inputs from user to be used in RemoveBackground function
        as parameters. This function ensures that the given inputs has proper
        extensions (.jpg or .png).

        First input is the name of the image file with proper extension given by
        user or program itself.

        Second input is the name of the processed image file with proper extension,
        or if it is not given with .png extension.

            return -> tuple     (input_image_path, output_img_path)  
    """
    while True:
        # take input path for image which bg will be removed
        input_img_path = input("Enter image path: ")            # full/relative path with .jpg/.png extension

        input_img_path = input_img_path.strip()                 # remove spaces from both ends

        extension = input_img_path[-4:]                         # check if input has valid extension
        
        # Choose proper extension
        if (extension == ".png") or (extension == ".jpg"):
            print("Valid input.")
            break

        elif (not ( extension == ".jpg")) or (not( extension == ".png")):
            print("Please choose one of these extensions:\t1.JPG\t2.PNG")
            choice = input("\nYour choice:")

            if choice == "1" or choice.lower() == "jpg" or choice.lower() == ".jpg":
                input_img_path = input_img_path[:-4] + ".jpg"
                print("Valid input.")
                break

            elif choice == "2" or choice.lower() == "png" or choice.lower() == ".png":
                input_img_path = input_img_path[:-4] + ".png"
                print("Valid input.")
                break


    while True:
        output_img_path = input("Enter output image name: ")

        output_img_path = output_img_path.strip()

        extension = output_img_path[-4:]
        if extension == ".png":
            print(f"Your output file name: {output_img_path}")
            break
        elif not ( extension == ".png"):
            output_img_path = output_img_path[:-4] + ".png"
            print(f"Your output file name: {output_img_path}")
            break
    
    return input_img_path, output_img_path





# Function to remove background
def RemoveBackground(input_img_path, output_img_path):
    
    try:
        # try to open files
        with open(input_img_path, "rb") as img_input:               # rb -> read binary
            with open(output_img_path, "wb") as img_output:         # wb -> write binary
                input_img = img_input.read()
                output_img = remove(input_img)                      # remove the background from input image file
                img_output.write(output_img)                        # and write it on output image file
    except FileNotFoundError:
        # if encounter any error -cannot found the file
        print("An error has occured. Please try again.")
        quit()


    print("Background removed successfully.\nYou can enjoy your image :)")


if __name__ == "__main__":
    input_path, output_path = TakePaths()
    RemoveBackground(input_path, output_path)
else:
    print("""
            To remove background from your pictures use these 2 functions in order.
            First: TakePaths
                This function returns a tuple. First item in this tuple is the first
                argument of the second function and the second item in this tuple is 
                second argument of the second function.
                Call the function like this: input_file, output_file = TakePaths()
          
            Second: RemoveBackground(param1, param2)
                This function removes background from the param1 and return param2
                as output image. Call this function with the outputs of the first function.
                Call the function like this: RemoveBackground(input_file, output_file)
        """)