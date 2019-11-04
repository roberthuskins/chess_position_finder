'''
The pgn_capsule object takes in a single file path to a pgn file 
and then converts the file into a list of strings of the pgn files 
themselves. This is useful on its own, however it will be useful to
pass into the pgn-parser library
'''

class pgn_capsule:

    pgn_array = []
    def __init__(self, game_string):
        parsed_pgn = ""

        game_string = game_string
        file_as_array = game_string.split("\n")

        for i in range(len(file_as_array)):
            # gets rid of trailing whitespace
            file_as_array[i] = file_as_array[i].rstrip("\n\r")  
            #getting rid of header tags
            if "[" in file_as_array[i] or "]" in file_as_array[i]:
                continue
            elif file_as_array[i]:
                parsed_pgn+=file_as_array[i] + " "

                #this is slow
                if "0-1" in file_as_array[i] or "1-0" in file_as_array[i] or "1/2" in file_as_array[i] or "*" in file_as_array[i]:
                    parsed_pgn+="SPLIT_FILE_HERE"
        #the object will have a list of chess games in pgn format
        print(parsed_pgn)
        self.pgn_array = parsed_pgn.split("SPLIT_FILE_HERE")
        del self.pgn_array[-1] #left with extra blank string at the back of the array due to split