import re

'''
The pgn_capsule object takes in a single file path to a pgn file 
and then converts the file into a list of strings of the pgn files 
themselves. This is useful on its own, however it will be useful to
pass into the pgn-parser library
'''

class pgn_capsule:

    pgn_array = []
    def __init__(self, file_path):
        parsed_pgn = ""

        python_pgn_file = open(file_path)
        file_as_array = python_pgn_file.readlines()
        python_pgn_file.close()

        for i in range(len(file_as_array)):
            # gets rid of trailing whitespace
            file_as_array[i] = file_as_array[i].rstrip("\n\r") 
            #getting rid of header tags
            if "[" in file_as_array[i] or "]" in file_as_array[i]:
                continue
            elif file_as_array[i]:
                parsed_pgn+=file_as_array[i] + " "
                if "0-1" in file_as_array[i] or "1-0" in file_as_array[i] or "1/2" in file_as_array[i] or "*" in file_as_array[i]:
                    parsed_pgn+="SPLIT_FILE_HERE"
        #the object will have a list of chess games in pgn format
        
        self.pgn_array = parsed_pgn.split("SPLIT_FILE_HERE")
        del self.pgn_array[-1] #left with extra blank string at the back of the array due to split

    #returns the last element of the pgn_array and deletes it from the object
    def pop(self):
        return self.pgn_array.pop()

# test = pgn_capsule("master_games.pgn")
# print(test.pop())
# print(test.pop())
