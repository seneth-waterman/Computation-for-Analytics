import pickle
# DO NOT ADD ANY OTHER PACKAGES AND LIBRARIES


def create_image_array(file_name):
    """
    Create a function called create_image_array() which takes
    file_name as an input variable and returns a list
    with the given width and height.
    """
    with open(file_name, 'r') as file:
        # Determine width and height of file (first two lines)
        width = int(file.readline().strip())
        height = int(file.readline().strip())

        # Initiate list to store data 
        array = []

        # Create the data row by row (i = row #)
        i = 0 
        while i < height:
            j = 0
            # Create a list to store each rows information
            row = []
            # Cycle through each column of the row (j = columns #)
            while j < width: 
                #read the rgb value from the file and store it in a list
                r_g_b = file.readline().strip().split(',')
                #convert each rgb value to integer, add value as a list to the row
                row.append([int(r_g_b[0]), int(r_g_b[1]), int(r_g_b[2])])
                #go to next column
                j += 1
            # Add completed row to array
            array.append(row)

            # go to next row
            i += 1
    return array


def load_pickle_file(file_name):
    """
    Create a function called load_pickle_file() which takes a pickle file
    called file_name as an input variable, and returned its python object.
    """
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data

def xray_filter(numbers):
    """
    Create xray_filter() that takes a list and returns a new list.
    This new list includes updated r,g,b values that
    r_value = 255 - r_value
    g_value = 255 - g_value
    and b_value = 255 – b_value.
    """
    
    # create a copy of the list so you can change values in place
    x_ray = copy_all_lists(numbers)

    # cycle through list, row by row, iterating over each column and changing the rgb value (255 - old value)
    i = 0
    while i < len(x_ray):
        j = 0
        while j < len(x_ray[i]):
            x_ray[i][j][0] = 255 - numbers[i][j][0]
            x_ray[i][j][1] = 255 - numbers[i][j][1]
            x_ray[i][j][2] = 255 - numbers[i][j][2]
            j += 1
        i += 1
    
    return x_ray


def adjust_r_g_b(numbers, r_ratio, g_ratio, b_ratio):
    """
    Create a function called adjust_r_g_b() that takes the image array and
    three float values that are multiplied to r,g, and b values accordingly.
    The adjusted value should be rounded to an integer.
    """

    # create a copy of the list so you can change values in place
    adjusted = copy_all_lists(numbers)

    # cycle through list, row by row, iterating over each column and changing the rgb value (color_ratio * old value)
    i = 0
    while i < len(adjusted):
        j = 0
        while j < len(adjusted[i]):
            adjusted[i][j][0] = round(r_ratio * numbers[i][j][0])
            adjusted[i][j][1] = round(g_ratio * numbers[i][j][1])
            adjusted[i][j][2] = round(b_ratio * numbers[i][j][2])
            j += 1
        i += 1
    
    return adjusted


def upside_down(numbers):
    """
    Create a function called upside_down() that takes a list and
    reverses the list.
    """

    # create a copy of the list so you can change values in place
    upside_down = copy_all_lists(numbers)
    height = len(upside_down)

    # cycle through list, row by row, iterating over each column and changing the rgb value by swapping row # index (new row # = height - old row # value)
    i = 0
    while i < len(upside_down):
        j = 0
        while j < len(upside_down[i]):
            upside_down[i][j][0] = numbers[height - i - 1][j][0]
            upside_down[i][j][1] = numbers[height - i - 1][j][1]
            upside_down[i][j][2] = numbers[height - i - 1][j][2]
            j += 1
        i += 1
    
    return upside_down


def vertical_flip(numbers):
    """
    Create a function called vertical_flip() that
    takes a list and returns a list
    where values in each row are vertically flipped.
    """

    # create a copy of the list so you can change values in place
    vertical_flip = copy_all_lists(numbers)

    # cycle through list, row by row, iterating over each column and changing the rgb value by swapping column # index (new column # = height - old column # value)
    i = 0
    while i < len(vertical_flip):
        j = 0
        while j < len(vertical_flip[i]):
            width = len(numbers[i])
            vertical_flip[i][j][0] = numbers[i][width - j - 1][0]
            vertical_flip[i][j][1] = numbers[i][width - j - 1][1]
            vertical_flip[i][j][2] = numbers[i][width - j - 1][2]
            j += 1
        i += 1
    
    return vertical_flip

def create_border(**kargs):
    """
    Add a border around the images with given
    red, green, blue and pixel values.
    Input parameters are given as arbitary keyword arguments
    including numbers, red, green, blue and pixel.
    "numbers" is a list of pixel values of the input image created
    by create_image_array().
    "red", "green", "blue" are indicating values for rgb values.
    The "pixel" number of [red, green, blue] value should be added
    at the beginning and end of each row.
    In addition, the returned list should have
    the "pixel" number of rows only consists
    with the given red, green, blue at the beginning and end of "numbers".
    """

    #define border color and size
    border_color = [kargs['red'], kargs['green'], kargs['blue']]
    border_size = kargs['pixel']
    
    #define interior array
    interior_array = kargs['numbers']

    #make an empty list to add items to
    bordered_array = []

    # Top border = pixel + width + pixel 
    width_of_interior = len(interior_array[0])
    width_of_top_border = 2 * border_size + width_of_interior
    
    # Create top border
    bordered_top = []
    for t in range(width_of_top_border):
        bordered_top.append(border_color)
    # Add top border n times (n = pixel)
    for n in range(border_size):
        bordered_array.append(bordered_top)
  
    # Each row = pixel + original + pizel
    for i in range(len(interior_array)):
        bordered_row = []
        # Pad beginning of row with given number of pixels
        for j in range(border_size):
            bordered_row.append(border_color)
        
        # Add row from oringal array (this is the image)
        for item in interior_array[i]:
            bordered_row.append(item)

        # Pad end of row with given number of pixels
        for k in range(border_size):
            bordered_row.append(border_color)

        # Add individual row to new bordered array
        bordered_array.append(bordered_row)
    

    # Bottom border = Top border = pixel + width + pixel 
    # Add bottom border n times (n = pixel)
    for b in range(border_size):
        bordered_array.append(bordered_top)

    return bordered_array


def copy_all_lists(input_list):
    """
    Creates a copy of entire list - including nested lists.
    """
    copied_list = []
    i = 0 
    while i < len(input_list):
        j = 0 
        copied_row = []
        while j < len(input_list[i]):
            copied_row.append(input_list[i][j].copy())
            j += 1
        copied_list.append(copied_row)
        i += 1
    return copied_list

import numpy as np
file_name = 'trial.txt'
array = create_image_array(file_name)
#print(array)

#print(xray_filter(array))
#print(adjust_r_g_b(array, 1, 0.9, 0.8))
#print(upside_down(array))
#print(vertical_flip(array))
#create_border(numbers=array, red=0, green=0, blue=0, pixel=2)

print(array)

#np_array = np.loadtxt(file_name,
                      #delimiter = ',',
                      #skiprows = 2,
                      
                      #)
np_array = np.array([[[1,2], [3,4]],[[5,6],[7,8]]])
print(np_array)
