import mmap
import os.path
class DataManager:
    """This class helps keeping all the ids saved in a txt file"""
    def __init__(self, fileName):
        
        self.fileName = fileName
        if os.path.isfile(self.fileName) == False:
            file = open(self.fileName, 'w')
            file.write("*_INI FILE_*\n")
            file.close()
    def is_stored_b(self, id_string):
        Found = False
        if os.path.isfile(self.fileName) == False:
            return Found
        with open(self.fileName, 'rb', 0) as file, \
             mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(bytes(id_string, 'UTF-8')) != -1:
                Found = True
        return Found
    def is_stored(self, id_string):
        Found = False
        if os.path.isfile(self.fileName) == False:
            return Found
        if id_string in open(self.fileName).read():
            Found = True
        return Found;
    def add_data(self, id_string):
        if os.path.isfile(self.fileName) == False:
            file = open(self.fileName, 'w')
        else:
            file = open(self.fileName, 'a')
        if not self.is_stored_b(id_string):
            file.write(id_string + "\n")
            file.close()
        return
    def remove_data(self, id_string):
        if os.path.isfile(self.fileName) == True:
            file = open(self.fileName,"r")
            fileData = f.readlines()
            file.close()
            file = open(self.fileName,"w")
            for line in fileData:
                if line!=id_string+"\n":
                    f.write(line)
            file.close()
        return
    def Set_fileName(self, name):
        self.fileName = name
        return
