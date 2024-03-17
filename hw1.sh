#!/usr/bin/bash

line_break='=============='
path=`pwd`
file_name='git_address.txt'
file_contents=`cat $file_name`

#loop through each line in file_name
for line in $file_contents
do
    #seperate each line based on comma in new variables; url and folder
    IFS=',' read -ra parts <<< "$line"
    git_repo_url=${parts[0]}
    folder_path=${parts[1]}

    #If the folder path EXISTS, update it using git pull
    if [ -d $folder_path ]
        then 
        cd $folder_path
        git pull 
        #List all contents of the folder path
        ls -la 
    
    #If the folder path DNE, clone the repository to the given folder path
    else
        git clone $git_repo_url $folder_path 
        #List all contents of the folder path
        cd $folder_path 
        ls -la 
    fi
    
    #Return to original directory
    cd $path

    #Print line break
    echo $line_break

done 

