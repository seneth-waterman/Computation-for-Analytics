
input_file = './imdb_titles_medium.tsv'
delimiter = '\t'
keys = ['title', 'region', 'language', 'types']
null_value = '\\N'
title_id = 'id'
information = 'information'

def create_movie_list(input_file, delimiter, keys, null_value, title_id, information):
    """
    Create a function called create create_movie_list(),
    which takes five input parameters called input_file (str),
    delimeter (str), keys (list), null_value (str), title_id (str),
    and information (str).
    Here is more about the input_file. It is a tsv file which contains
    information about movies.
    Each line of the file contains information about a movie.
    This function should return a list of dictionaries
    where each dictionary corresponds to a movie and information
    about the movie.
    Each dictionary should have the following keys:
    1. First key-value pair(Key: Value)
    - Key: Assign it the "title_id" variable.
    - Value: Assign it the corresponding titleID value from the input file.
    2. Second key-value pair(Key: Value)
    - Key: Assign it the "information" variable.
    - Value: This is a list of dictionaries that contains information
    on the movies having the same "title_id"
    as in the first key value pair above.
    Each dictionary should contain all the keys from the "keys" variable
    and its corresponding value.
    Ex.
    If keys = ['title','region'], the dictionary should only contain
    'title' and 'region'.
    If any of the keys have a value which is the null value,
    then the key should not be included.
    Ex.
    keys = ['title','region','language','types']
    null_value = '\\N'
    Row of file = [ ...., 'Карменсіта',  'UA', '\\N', 'imdbDisplay']
    The dictionary should only contain 'title', 'region' and 'types'.
    3. Third key-value pair(Key: Value)
    - Key: 'original_title'
    - Value: If the second field of the row from the file is '1',
             then assign its "title" as a value.
    Ex.
    Row of file = [ 'tt0000001', '1', 'Карменсіта',...]
    The key-value pair is {'original_title': 'Карменсіта'}
    """
    # Generate an index for headers
    with open(input_file, mode='r') as f:
        headers = f.readline().strip().split(delimiter)

    #Generate List of Data
    data = []
    with open(input_file, mode='r') as f:
        for line in f.readlines():
            data.append((line.strip().split(delimiter)))
    #Problem_1: List of Dictionary's of Each Movie

    # List of Dictionary's of Each Movie
    movie_list = []

    #Initiate List to Track ids
    id_list =[]

    # Loop through movies with different id's 
    for i in range(1, len(data)):
    
        
        #If id has not been added to movie list: 
        if data[i][0] not in id_list:

            #Add id to list so it will not get itterated over again
            id_list.append(data[i][0])

            #Dictionary for each movie 
            movie_dict = {}

            # First Key - Value Pair: {id:id#}
            movie_dict[title_id] = data[i][headers.index('titleId')]

            #Second Key-Value Pair: {information: list of dictionaries of information about each movie with same id}
            info_list = []

            # Iterate through each movie with the same id and add dictionary of info about that movie to info_list
            for j in range(len(data)):

                # If movie (row) in data set has the same id:
                if data[i][0] == data[j][0]:

                    #create a dictionary for that movie (row)
                    dic_individual_movie = {}   
                    
                    # loop through piece of information (item) for each movie (row) adding it to the dictionary of the movie (row)
                    # loop through each piece of desired info given in variable keys
                    for k in range(len(keys)):
                        # skip items that contain null value
                        if data[j][headers.index(keys[k])] != null_value:
                            dic_individual_movie[keys[k]] = data[j][headers.index(keys[k])] 
                    
                    # Add dictionary of movie (row) into info_list
                    info_list.append(dic_individual_movie)

                    #Third Key Value Pair - original title
                    if data[j][headers.index('isOriginalTitle')] == '1':
                        movie_dict['original_title'] = data[j][headers.index('title')]
                    
            # Add {information: list of dictionaries of information about each movie with same id} 
            movie_dict[information] = info_list


            # Add dictionary of movies with same id to movie list
            movie_list.append(movie_dict)

    return(movie_list)

def return_title_id_original_title_dict(movie_list, title_id):
    """
    Q2.
    Complete return_title_id_original_title_dict() which takes
    the output movie list  from Question 1 and title_id as input parameters.
    This function should return a dictionary
    where the key is the value of title_id
    and the corresponding value is the value of its original_title.
    This dictionary should only include title_id keys
    if "original_title" key exists.
    """

    # Create dictionary w/ key:value pairs {id: name of original title}
    title_id_original_title_dict = {}

    #Iterate through each id listed in movie list
    for i in range(len(movie_list)):

        try: 
            # Check if original title exist:
            original_title = movie_list[i]['original_title']
            # Add key value pair {value of title_id (id#): original title}
            title_id_original_title_dict[movie_list[i][title_id]] = original_title
        except:
            continue
 
    return(title_id_original_title_dict)


def return_information_element_set(**kargs):
    """
    Q3.
    Create a function called return_information_element_set()
    which takes arbitrary  keyword arguments.
    For a list assigned to the keyword argument 'movie_list'
    and a string assigned to the keyword argument 'key',
    this function should return a set that includes unique values
    found in any values associated with the 'key' in 'information'.
    You are allowed to hard code the strings, 'movie_list','information'
    and 'key' in your function.
    """
    unique_values = set()
    movie_list = kargs['movie_list']
    key = kargs['key']
    information = 'information'

    for i in range(len(movie_list)):
        for j in range(len(movie_list[i][information])): 
            try:
                unique_values.add(movie_list[i][information][j][key])
            except:
                continue
    
    return unique_values


def sort_information(**kargs):
    """
    Q4.
    Create a function called sort_information() which takes
    arbitrary keyword arguments.
    For the list of movies returned by Question 1,
    this function should return a list of movies with the ‘information’ array
    sorted by the field assigned to the keyword argument 'key'
    in ascending order. If key does not exist in the information array,
    then assume that the value of the field is an empty string('').
    You are allowed to hard code the strings,
    'movie_list', ‘information’, and 'key' in your function.
    """
    movie_list = kargs['movie_list']
    key = kargs['key']
    information = 'information'

    for i in range(len(movie_list)):
        list_containing_key = []
        list_without_key = []
        for j in range(len(movie_list[i][information])): 
            try:
                movie_list[i][information][j][key]
                list_containing_key.append(movie_list[i][information][j])
            except:
                list_without_key.append(movie_list[i][information][j])
        
        sorted_list = sorted(list_containing_key, key=lambda x: x[key])
        
        if len(list_without_key) > 0:
            movie_list[i][information] = (list_without_key + sorted_list)
        else: 
            movie_list[i][information] = (sorted_list)
        
        #movie_list[i][information] = sorted_information_list
    
    #return sorted_information_list
    return movie_list




#movie_list = create_movie_list(input_file, delimiter, keys, null_value, title_id, information)
#title_id_original_title_dict = return_title_id_original_title_dict(movie_list, title_id)

#print(len(movie_list))
#print(len(title_id_original_title_dict))
#print(title_id_original_title_dict)
#print(return_information_element_set(movie_list=movie_list, key='types'))
#movie_list = movie_list[0:1]
#print(movie_list[0:1])
#print(sort_information(movie_list=movie_list, key='region'))




