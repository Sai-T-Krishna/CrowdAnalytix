## import all the required modules

# install the pillow package
from PIL import Image
import json
import wget, os

''' For more on wget package - https://pypi.org/project/wget/ '''
import base64
import validators

# enter the input url - Eg: https://www.google.com/logos/doodles/2021/uefa-euro-2020-6753651837109267-l.png
url = input("'Please enter image URL (string):'")
def func():
    try:
        # validate the url
        validators.url(url)

        # downloading the image from the given url
        file_name = wget.download(url)

        # getting the file path
        file_path = os.path.abspath(file_name)

        # getting the file size
        size = os.path.getsize(file_name)

        print('\n')
        print("size of image is : ", size, 'bytes')
        print('\n')
        print('Image Successfully Downloaded: ', file_name)
        print("path is: ", file_path)

    # exception when the url is not valid
    except Exception:
        print('Enter a valid url')

    else:
        ''' resizing the image '''
        # open the image and get the width and height
        image = Image.open(file_name)
        org_width, org_height = image.size

        # get resized image and save it using thumbnail method
        image.thumbnail(size=(250,250))
        image.save('resized_image.png', optimize=True, quality=65)

        # get resized image width and height
        get_res = Image.open('resized_image.png')
        resized_wid, resized_hght = get_res.size
        resized_image_size = os.path.getsize('resized_image.png')
        resized_path = os.path.abspath('resized_image.png')
        print('Image is resized successfully')

        # base64 representation
        ''' Base64 - Base64 is a group of similar binary-to-text encoding schemes 
            that represent binary data in an ASCII string format by translating it into a radix-64 representation. 
            The term Base64 originates from a specific MIME content transfer encoding'''
        with open('resized_image.png', "rb") as img_file:
            my_string = base64.b64encode(img_file.read())
        print(my_string)
        
        # jsonify the output
        value = {
            "thumbnail_base64": str(my_string),
            "thumbnail_path": resized_path ,
            "original_size": "size of original image is " + str(size) + " bytes",
            "thumbnail_size": "size of Thumbnail image is " + str(resized_image_size) + " bytes",
            "original_resolution": "resolution of original image: " +  str(org_width) + " X " + str(org_height),
            "thumbnail_resolution": "resolution of resized image: " +  str(resized_wid) + " X " + str(resized_hght),

        }
        print('\n')
        print(json.dumps(value))

# execute the function  
func()
        

    

    




