import base64

ask_user = input('1. convert image to bytes.\n2.convert bytes to image')

if ask_user == '1':
    image_to_bytes()
    
elif ask_user == '2':
    bytes_to_image()

else:
    print('Wrong Input!!!')
    


def image_to_bytes():
    
    # get image path from user
    file_path = input('''Enter image path like this:
D:\\Sadeq0101\\image.jpg
''')
    
    # change '\\' or '\' to '/' to inhibition backslash errors
    if '\\' in file_path or '/' in file_path:
        
        # edited file path
        edited_image_path = file_path.replace('\\', '/')
        
        # split file path by / and make a list of them, then we choose last one in the list
        # delete 4 last letter of the name. because they are format of file. '.jPG' or '.PNG'
        text_file_name = ((edited_image_path.split('/'))[-1])[:-4]
        
        # split file path by / and make a list of them, then we choose all indexes from 0 to 1 before last one.
        # last one is the file name
        text_file_path = '/'.join((edited_image_path.split('/'))[:-1]) + '/'
        
        # open and choose image
        imageFile = open(fr'''{edited_image_path}''', "rb")

        # decode image and converts it to strings
        image_string = base64.b64encode(imageFile.read()) 
        
        # open a text file that places in path that image exists and save it same as image name
        text_file = open(f'''{text_file_path}/{text_file_name}.txt''', 'w')
        
        # write bytes of image in text file
        text_file.write(fr'''{image_string}''')
        
        print('Image converted to bytes!')
      


def image_to_bytes():
    
    # get image path from user
    file_path = input('''Enter image path like this:
D:\\Sadeq0101\\image.jpg
''')
    
    # change '\\' or '\' to '/' to inhibition backslash errors
    if '\\' in file_path or '/' in file_path:
        
        # edited file path
        edited_image_path = file_path.replace('\\', '/')
        
        # split file path by / and make a list of them, then we choose last one in the list
        # delete 4 last letter of the name. because they are format of file. '.jPG' or '.PNG'
        text_file_name = ((edited_image_path.split('/'))[-1])[:-4]
        
        # split file path by / and make a list of them, then we choose all indexes from 0 to 1 before last one.
        # last one is the file name
        text_file_path = '/'.join((edited_image_path.split('/'))[:-1]) + '/'
        
        # open and choose image
        imageFile = open(fr'''{edited_image_path}''', "rb")

        # decode image and converts it to strings
        image_string = base64.b64encode(imageFile.read()) 
        
        # open a text file that places in path that image exists and save it same as image name
        text_file = open(f'''{text_file_path}/{text_file_name}.txt''', 'w')
        
        # write bytes of image in text file
        text_file.write(fr'''{image_string}''')
        
        print('Image converted to bytes!')
      