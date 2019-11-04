# chess_position_finder

Imports a chess pgn file and analyses it with the [Stockfish](https://stockfishchess.org/) chess engine. Outputs a list of chess positions for the user to try to solve for themselves. 

For example, if you upload the famous [Opera House Game](https://en.wikipedia.org/wiki/Opera_Game) (the app supports bulk pgn files as well) with the following parameters...
![Imgur](https://i.imgur.com/3e6dNGl.png)




The app shout output...
![Imgur](https://i.imgur.com/Zd10K9V.png)

To view the position for yourself, you can post the FEN string ... <br><b>r3kb1r/p2nqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/R3K2R w KQkq - 1 12</b><br>into an analysis board such as [lichess](https://lichess.org/analysis/standard/_____r3kb1r/p2nqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/R3K2R_w_KQkq_-_1_12#22).

## Requirements:
Flask: https://github.com/pallets/flask <br>
Python-Chess: https://github.com/niklasf/python-chess

