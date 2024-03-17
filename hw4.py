import numpy as np
from PIL import Image as Img

class Image():
    """
    1.	Create a class called Image which takes file_name for its constructor
    and creates/assigns its image array attribute from the file.
    """
    def __init__(self, file_name_val):
        self.file_name = file_name_val
        
    """
    2.	Create a class method called return_image_array(),
    which returns the image array attribute.
    """
    def return_image_array(self):
        with open(self.file_name, 'r') as file:
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            array = []
            for i in range(height):
                row = []
                for j in range(width):
                    r_g_b = file.readline().strip().split(',')
                    row.append([int(r_g_b[0]), int(r_g_b[1]), int(r_g_b[2])])
                array.append(row)
        self.image_array = array
        return self.image_array
    
    """
    3.	Create a class method called create_image_np_array() which
    1) creates a numpy array from the image array,
    2) assigns to a class attribute, and 3) returns it.
    """
    def create_image_np_array(self):
        self.image_np_array = np.array(self.return_image_array())
        return self.image_np_array 
    """
    4.	Create a class method called check_image_np_array_shape() which
    1) assigns the shape of the image np array to a class attribute.
    2) If the image np array does not exist,
    this method should call create_image_np_array()
    to get its shape information.
    """
    def check_image_np_array_shape(self):
        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()
        self.shape = self.image_np_array.shape
        return self.shape
    
    """
    5.	Create a class method called save_image_file() which
    1) creates  'image.sgi' (you can hardcode) file
    under the same directory as the file_name.
    (Ex. if file_name was '../data/data.txt',
    this method creates '../data/image.sgi').
    2) If the image np array does not exist, this method should call
    create_image_np_array() for this class method.
    """
    def save_image_file(self):
        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()
        image_name = self.file_name[:self.file_name.rfind('/') + 1] + 'image.sgi'
        image = Img.fromarray(self.image_np_array.astype(np.uint8), mode='RGB')
        image.save(image_name)


    """
    6.	Create a class method called create_flip_image_np_array() which
    1) creates a numpy array of a flipped image
    by manipulating the image np array, as you did for vertical_flip() in HW3.
    2) assigns it to a class attribute, and  3) returns it.
    4) If the image np array does not exist, this method should call
    create_image_np_array() to complete this class method.
    """
    def create_flip_image_np_array(self):
        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()
        self.flip = np.fliplr(self.image_np_array)
        return self.flip
    """
    7.	Create a class method called save_flip_image_file() which creates
    'flip_image.sgi' (you can hardcode) file under the same directory
    as the file_name. (Ex. if file_name was '../data/data.txt',
    this method creates '../data/flip_image.sgi').
    2) If the flipped image np array does not exist,
    this method should call create_flip_image_np_array() for this class method.
    """
    def save_flip_image_file(self):
        if not hasattr(Image, 'flip'):
            self.create_flip_image_np_array()
        image_name = self.file_name[:self.file_name.rfind('/') + 1] + 'flip_image.sgi'
        image = Img.fromarray(self.flip.astype(np.uint8), mode='RGB')
        image.save(image_name)

    """
    8.	Create a class method called create_upside_down_image_np_array()
    which 1) creates a numpy array of an upside-down image
    by manipulating the image np array, as you did for upside_down() in HW3.
    2) assigns it to a class attribute, and 3) returns it.
    4) If the image np array does not exist,
    this method should call create_image_np_array() for this class method.
    """
    def create_upside_down_image_np_array(self):
        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()
        self.upside_down = np.flipud(self.image_np_array)
        return self.upside_down
    """
    9.	Create a class method called save_upside_down_image_file() which
    creates  'upside_down_image.sgi' (you can hardcode) file under
    the same directory as the file_name. (Ex. if file_name was
    '../data/data.txt', this method creates '../data/upside_down_image.sgi').
    2) If the upside-down image np array does not exist,
    this method should call create_upside_down_image_np_array()
    to complete this class method.
    """
    def save_upside_down_image_file(self):
        if not hasattr(Image, 'upside_down'):
            self.create_upside_down_image_np_array()
        image_name = self.file_name[:self.file_name.rfind('/') + 1] + 'upside_down_image.sgi'
        image = Img.fromarray(self.upside_down.astype(np.uint8), mode='RGB')
        image.save(image_name)
    """
    10.	Create a class method called create_xray_filter_np_array() which
    1) creates a numpy array of a x-ray image by manipulating
    the image np array, as you did for xray_filter() in HW3.
    2) assigns it to a class attribute, and 3) returns it.
    4) If the image np array does not exist, this method should call
    create_image_np_array() for this class method.
    """
    def create_xray_filter_np_array(self):
        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()
        self.x_ray = 255 - self.image_np_array
        return self.x_ray
    """
    11.	Create a class method called save_xray_filter_file() which creates
    'xray_filter_image.sgi' (you can hardcode) file under the same directory
    as the file_name. (Ex. if file_name was '../data/data.txt',
    this method creates '../data/xray_filter_image.sgi').
    2) If the xray filter np array does not exist, this method should call
    create_xray_filter_np_array() to complete this class method.
    """
    def save_xray_filter_file(self):
        if not hasattr(Image, 'x_ray'):
            self.create_xray_filter_np_array()
        image_name = self.file_name[:self.file_name.rfind('/') + 1] + 'xray_filter_image.sgi'
        image = Img.fromarray(self.x_ray.astype(np.uint8), mode='RGB')
        image.save(image_name)
    """
    12.	Create a class method called create_border_np_array() which
    1) takes r, g, b, and pixel values and creates a numpy array
    with surrounding borders by manipulating the image np array,
    as you did for create_border() in HW3.
    The default r, g, and b values are 0, and the default value for pixel is 1.
    2) assigns it to a class attribute and 3) returns it.
    4) If the image np array does not exist, this method should call
    create_image_np_array() for this class method.
    """
    def create_border_np_array(self, r: int=0, g: int=0, b: int=0, pixel: int=1):
        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()

        image = self.image_np_array
        width = image.shape[1]
        height = image.shape[0]
        border_width = (2 * pixel) + width
        border_height = (2 * pixel) + height

        # Create a new array big enough to contain the border
        padded_array = np.empty([border_height, border_width, 3], dtype=np.uint8)
        
        # Fill array with border color
        padded_array[:, :] = np.array([r, g, b])

        # Insert image into colored/bordered array
        padded_array[pixel:(height+pixel), pixel:(width+pixel)] = image
        
        self.bordered_image = padded_array

        return self.bordered_image

        # https://www.pythoninformer.com/python-libraries/numpy/image-operations/ <- this was very helpful!!!
    
    """
    13.	Create a class method called save_border_file() which creates
    'border_image.sgi' (you can hardcode) file under the same directory
    as the file_name. (Ex. if file_name was '../data/data.txt',
    this method creates '../data/border_image.sgi').
    2) If the border np array does not exist, this method should call
    create_border_np_array() to complete this class method.
    """
    def save_border_file(self):
        if not hasattr(Image, 'bordered_image'):
            self.create_border_np_array()
        image_name = self.file_name[:self.file_name.rfind('/') + 1] + 'border_image.sgi'
        image = Img.fromarray(self.bordered_image.astype(np.uint8), mode='RGB')
        image.save(image_name)

    """
    14.	Create a class method called create_r_g_b_np_array() which
    1) creates three numpy arrays, where the first value in a pixel array
    is the same for the r image np array, where the rest are zeros.
    (the second and third values are the same for the g and b image np array,
    respectively, and the rest are zero.)
    2) assigns them to three different class attributes, and
    3) returns them as a tuple of
    (r image np array, g image np array, b image np array).
    4) If the image np array does not exist, this method should call
    create_image_np_array() for this class method.
    """
    def create_r_g_b_np_array(self): 

        if not hasattr(Image, 'image_np_array'):
            self.create_image_np_array()

        red = self.image_np_array.copy()
        red[:, :, [1,2]] = 0
        self.r_image_array = red

        green = self.image_np_array.copy()
        green[:, :, [0,2]] = 0
        self.g_image_array = green

        blue = self.image_np_array.copy()
        blue[:, :, [0,1]] = 0
        self.b_image_array = blue

        return (self.r_image_array, self.g_image_array, self.b_image_array,)
    
    """
    15.	Create a class method called save_r_g_b_file() which
    creates  'r_image.sgi', 'g_image.sgi', and 'b_image.sgi'
    (you can hardcode) files under the same directory as the file_name.
    (Ex. if file_name was '../data/data.txt',  this method creates
    '../data/r_image.sgi'). 2) If r image np array, b image np array,
    or g image np array does not exist,
    this method should call create_r_g_b_np_array()
    to complete this class method.
    """
    def save_r_g_b_file(self):
        colors = ['r', 'g', 'b']
        for i in range(3):
            image_name = self.file_name[:self.file_name.rfind('/') + 1] + f'{colors[i]}_image.sgi'
            image = Img.fromarray(self.create_r_g_b_np_array()[i].astype(np.uint8), mode='RGB')
            image.save(image_name)



