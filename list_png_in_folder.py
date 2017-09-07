import os

def list_available_png(path):
    """ Return a list if file names of type *.png in at path """
    
    png_list = []
    
    with os.scandir(path) as dir_list:
        for entry in dir_list:
            
            if entry.name[-3:] == "png":
                print("self.",entry.name[:-4], " = None", sep="")
                png_list.append(entry.name)
        
    return png_list
        


print(list_available_png("D:\learnpython\Projects\SimLife"))