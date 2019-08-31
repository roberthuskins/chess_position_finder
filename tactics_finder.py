import chess
import chess.engine
import chess.pgn
import io
from pgn_capsule import pgn_capsule


'''
Takes in a pgn_capsule object, spits out a list of FEN positions where tactics arise.
'''

#https://python-chess.readthedocs.io/en/latest/engine.html?highlight=engine
engine = chess.engine.SimpleEngine.popen_uci("engine/stockfish-10-64")

'''
capsule: the pgn_capsule object, that holds multiple pgn files
min: minimum centipawn loss for the tactic fen to be outputted
max: maximum centipawn loss for the tactic fen to be outputted

'''
def tactics_finder(capsule, min, max, depth):
    output = []
    for i in capsule.pgn_array:
        #here is where we go through each move and check engine evaluation
        pgn_to_io = io.StringIO(i)
        
        #imports the pgn into a python-chess board object

        try:
            game = chess.pgn.read_game(pgn_to_io)
        except:
            print("Unknown error, game not able to be imported")
            continue
        board = game.board()
        count = 0

        #going through each move, then checking to see if the engine has any opinions on it
        for move in game.mainline_moves():
            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(depth=depth))

            #info["score"] is a PovScore object
            if info["score"].is_mate():
                output.append(board.fen())
                break
            elif abs(info["score"].relative.score()) >=min and abs(info["score"].white().score()) <=max:
                output.append(board.fen())
                break
    
    print("> NUMBER OF GAMES ANALYZED: {}\n".format(len(capsule.pgn_array)))
    return output

'''
Temporary interface for the app
'''

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

engine.quit()

    

