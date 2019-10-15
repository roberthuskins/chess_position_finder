import chess
import chess.engine
import chess.pgn
import io
from pgn_capsule import pgn_capsule


'''
Takes in a pgn_capsule object, spits out a list of FEN positions where tactics arise.
'''


'''
capsule: the pgn_capsule object, that holds multiple pgn files
min: minimum centipawn loss for the tactic fen to be outputted
max: maximum centipawn loss for the tactic fen to be outputted

'''
def tactics_finder(capsule, min, max, depth):
    #https://python-chess.readthedocs.io/en/latest/engine.html?highlight=engine
    engine = chess.engine.SimpleEngine.popen_uci("engine/stockfish-10-64")
    output = []

    print(capsule.pgn_array)

    number_of_failed_parses = 0
    for i in capsule.pgn_array:
        #here is where we go through each move and check engine evaluation
        pgn_to_io = io.StringIO(i)
        
        #imports the pgn into a python-chess board object

        try:
            game = chess.pgn.read_game(pgn_to_io)
            board = game.board()
        except:
            print("Error: Game not able to be imported. Moving onto next game.")
            continue
        
        #keeps track of the games we've analyzed
        count = 0

        #going through each move, then checking to see if the engine has any opinions on it
        for move in game.mainline_moves():
            board.push(move)

            #information stockfish gives us
            info = engine.analyse(board, chess.engine.Limit(depth=depth))

            #info["score"] is a PovScore object
            if info["score"].is_mate():
                output.append(board.fen())
                break
            elif abs(info["score"].relative.score()) >=min and abs(info["score"].white().score()) <=max:
                output.append(board.fen())
                break
    
    print("> NUMBER OF GAMES ANALYZED: {}\n NUMBERED OF FAILED PARSES: {}\n".format(len(capsule.pgn_array),number_of_failed_parses))
    engine.quit()
    return output

'''
Test Application

print("> File path of pgn file, ex \"master_games.pgn\": ")
capsule = pgn_capsule(input())

print("> Minimum centipawn loss of the positions that are outputted: ")
min = int(input())

print("> Maximum centipawn loss of the positions that are outputted: ")
max = int(input())

print("> Engine depth, ex 15: ")
depth = int(input())

output = tactics_finder(capsule, min, max, depth)

for i in output:
    print(i)

'''
    

