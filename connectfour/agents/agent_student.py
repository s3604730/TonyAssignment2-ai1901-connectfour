from connectfour.agents.computer_player import RandomAgent
import random


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
       
       
       
        self.MaxDepth = 3

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append(move)
            vals.append(self.dfMiniMax(next_state, 1))

        bestMove = moves[vals.index(max(vals))]
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            # Enemy state or minimizing player state
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])

            else:
                next_state = board.next_state(self.id, move[1])

            moves.append(move)
            vals.append(self.dfMiniMax(next_state, depth + 1))
        # Enemy state
        if depth % 2 == 1:
            bestVal = min(vals)
        # our state
        else:
            bestVal = max(vals)

        return bestVal

    def evaluateBoardState(self, board):
        heuristicValue = 0
        heuristicHorizontalValue = 0
        heuristicPositiveDiagonalValue = 0
        listID = [1, 2]

        """
        Your evaluation function should look at the current state and return a score for it. 
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """

        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width 
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array 
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """

        # print(self.id)
        # get the id
        currentID = self.id
        # remove the other id
        listID.remove(currentID)
        # create enemyID
        enemyID = listID[0]
        # print("fdsafasdfsd" + str(enemyID))

        # Check all cells and add heuristic value based on how many in a row
        # or column
        for x in range(0, board.width):
            for y in range(0, board.height):

                # print(str(x) + " Yes " + str(y))
                # print(str(x) + "and" + str(y))
                # 2 combo vertical by row for us
                if x < 5:
                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x + 1, y)
                        == currentID
                    ):
                        heuristicValue += 10

                    if x < 4:
                        if (
                            board.get_cell_value(x, y)
                            == board.get_cell_value(x + 1, y)
                            == board.get_cell_value(x + 2, y)
                            == currentID
                        ):
                            heuristicValue += 50
                        if x < 3:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y)
                                == board.get_cell_value(x + 2, y)
                                == board.get_cell_value(x + 3, y)
                                == currentID
                            ):
                                heuristicValue += 5000

                # 2 combo horizontal by column for us

                if x < 6:
                    # print(str(x) + "and" + str(y))
                    # print(board.get_cell_value(0,5))
                    # 2 combo horizontal by column
                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x, y + 1)
                        == currentID
                    ):
                        heuristicValue += 10

                    # 3 combo horizontal by column
                    if y < 5:
                        if (
                            board.get_cell_value(x, y)
                            == board.get_cell_value(x, y + 1)
                            == board.get_cell_value(x, y + 2)
                            == currentID
                        ):
                            heuristicValue += 50

                        if y < 4:

                            # 4 combo horizontal by column
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x, y + 1)
                                == board.get_cell_value(x, y + 2)
                                == board.get_cell_value(x, y + 3)
                                == currentID
                            ):
                                heuristicValue += 5000

                # 2 combo linear negative diagonal
                if x < 5:
                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x + 1, y + 1)
                        == currentID
                    ):
                        heuristicValue += 10

                    # 3 combo linear negative diagonal
                    if x < 4:
                        if y < 5:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y + 1)
                                == board.get_cell_value(x + 2, y + 2)
                                == currentID
                            ):
                                heuristicValue += 50
                            # 4 combo linear negative diagonal
                            if x < 3:
                                if y < 4:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x + 1, y + 1)
                                        == board.get_cell_value(x + 2, y + 2)
                                        == board.get_cell_value(x + 3, y + 3)
                                        == currentID
                                    ):
                                        heuristicValue += 5000

                # 2 combo linear positive diagonal
                if x < 6:

                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x - 1, y + 1)
                        == currentID
                    ):
                        heuristicValue += 10

                    # 3 combo linear positive diagonal
                    if x < 6:
                        if y < 5:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 2, y + 2)
                                == currentID
                            ):
                                heuristicValue += 50

                            # 4 combo linear positive diagonal
                            if y < 4:
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x - 1, y + 1)
                                    == board.get_cell_value(x - 2, y + 2)
                                    == board.get_cell_value(x - 3, y + 3)
                                    == currentID
                                ):
                                    heuristicValue += 5000

                #
                # Enemy ID HEURISTIC*******************************************
                # 2 combo vertical by row for us
                if x < 5:
                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x + 1, y)
                        == enemyID
                    ):
                        heuristicValue -= 10

                    # 3 combo vertical by row for us
                    if x < 4:
                        if (
                            board.get_cell_value(x, y)
                            == board.get_cell_value(x + 1, y)
                            == board.get_cell_value(x + 2, y)
                            == enemyID
                        ):
                            heuristicValue -= 50

                        # 4 combo vertical by row for us
                        if x < 3:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y)
                                == board.get_cell_value(x + 2, y)
                                == board.get_cell_value(x + 3, y)
                                == enemyID
                            ):
                                heuristicValue -= 5000

                # print(board.height)
                # print(y)
                # 2 combo horizontal by column for us

                if x < 6:

                    # 2 combo horizontal by column
                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x, y + 1)
                        == enemyID
                    ):
                        heuristicValue -= 10

                    # 3 combo horizontal by column
                    if y < 5:
                        if (
                            board.get_cell_value(x, y)
                            == board.get_cell_value(x, y + 1)
                            == board.get_cell_value(x, y + 2)
                            == enemyID
                        ):
                            heuristicValue -= 50

                        if y < 4:

                            # 4 combo horizontal by column
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x, y + 1)
                                == board.get_cell_value(x, y + 2)
                                == board.get_cell_value(x, y + 3)
                                == enemyID
                            ):
                                heuristicValue -= 5000

                # 2 combo linear negative diagonal
                if x < 5:
                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x + 1, y + 1)
                        == enemyID
                    ):
                        heuristicValue -= 10

                    # 3 combo linear negative diagonal
                    if x < 4:
                        if y < 5:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y + 1)
                                == board.get_cell_value(x + 2, y + 2)
                                == enemyID
                            ):
                                heuristicValue -= 50
                            # 4 combo linear negative diagonal
                            if x < 3:
                                if y < 4:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x + 1, y + 1)
                                        == board.get_cell_value(x + 2, y + 2)
                                        == board.get_cell_value(x + 3, y + 3)
                                        == enemyID
                                    ):
                                        heuristicValue -= 5000

                # 2 combo linear positive diagonal
                if x < 6:

                    if (
                        board.get_cell_value(x, y)
                        == board.get_cell_value(x - 1, y + 1)
                        == enemyID
                    ):
                        heuristicValue -= 10

                    # 3 combo linear positive diagonal
                    if x < 6:
                        if y < 5:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 2, y + 2)
                                == enemyID
                            ):
                                heuristicValue -= 50

                        # 4 combo linear positive diagonal
                        if y < 4:
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 2, y + 2)
                                == board.get_cell_value(x - 3, y + 3)
                                == enemyID
                            ):
                                heuristicValue -= 5000

                # DEFENSIVE HEURISTIC PLAYER 2*****************
                # if current player is the second player
                try:
                    if currentID == 2:
                        if x < 7:
                            if y < 7:
                                # 2 combo horizontal by column for the enemy and there
                                # is an open space on the right
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x, y + 1)
                                    == enemyID
                                    and board.get_cell_value(x, y + 2) == 0
                                    # or there is an open space on the left side of the 2 combo horizontal
                                    # by column
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x, y + 1)
                                    == enemyID
                                    and board.get_cell_value(x, y - 1) == 0
                                ):
                                    heuristicValue -= 50

                                # 3 combo horizontal by column and theres space on the right side
                                # for enemy
                                if y < 7:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x, y + 1)
                                        == board.get_cell_value(x, y + 2)
                                        == enemyID
                                        and board.get_cell_value(x, y + 3) == 0
                                        # or 3 combo horizontal by column and space on the left
                                    ) or (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x, y + 1)
                                        == board.get_cell_value(x, y + 2)
                                        == enemyID
                                        and board.get_cell_value(x, y - 1) == 0
                                    ):
                                        heuristicValue -= 1500

                except:
                    pass

                # if current player is the second player
                try:
                    if currentID == 2:
                        if x < 7:

                            # 2 combo vertical by row for the enemy and there
                            # is an open space on the right
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y)
                                == enemyID
                                and board.get_cell_value(x + 2, y) == 0
                                # or there is an open space on the left side of the 2 combo vertical                                   # by column
                            ) or (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y)
                                == enemyID
                                and board.get_cell_value(x - 1, y) == 0
                            ):
                                heuristicValue -= 50
                            # 3 combo vertical by row and theres space on forward
                            # for enemy
                            if x < 7:
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y)
                                    == board.get_cell_value(x + 2, y)
                                    == enemyID
                                    and board.get_cell_value(x + 3, y) == 0
                                    # or 3 combo horizontal by column and space on backward
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y)
                                    == board.get_cell_value(x + 2, y)
                                    == enemyID
                                    and board.get_cell_value(x - 1, y) == 0
                                ):
                                    heuristicValue -= 1500

                except:
                    pass

                # if current player is the second player
                try:
                    if currentID == 2:
                        if x < 7:

                            # 2 combo positive diagonal and space on the right
                            # is an open space on the right
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == enemyID
                                and board.get_cell_value(x - 2, y + 2) == 0
                                # or there is an open space on the left side of the 2 combo diagonal                                  # by column
                            ) or (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == enemyID
                                and board.get_cell_value(x + 1, y - 1) == 0
                            ):
                                heuristicValue -= 50
                            # 3 combo postive diagonal and theres space on the right side
                            #
                            if x < 7:
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x - 1, y + 1)
                                    == board.get_cell_value(x - 2, y + 2)
                                    == enemyID
                                    and board.get_cell_value(x - 3, y + 3) == 0
                                    # or 3 combo horizontal by column and space on the left
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x - 1, y+1)
                                    == board.get_cell_value(x - 2, y+2)
                                    == enemyID
                                    and board.get_cell_value(x + 1, y - 1) == 0
                                ):
                                    heuristicValue -= 1500

                except:
                    pass
                #negative diagonal
                # if current player is the second player
                try:
                    if currentID == 2:
                        if x < 7:

                            # 2 combo negative diagonal and space on the right
                            # is an open space on the right
                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y + 1)
                                == enemyID
                                and board.get_cell_value(x + 2, y + 2) == 0
                                # or there is an open space on the left side of the 2 combo negative diagonal                                  # by column
                            ) or (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y + 1)
                                == enemyID
                                and board.get_cell_value(x - 1, y - 1) == 0
                            ):
                                heuristicValue -= 50
                            # 3 combo negative diagonal and theres space on the right side
                            #
                            if x < 7:
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y + 1)
                                    == board.get_cell_value(x + 2, y + 2)
                                    == enemyID
                                    and board.get_cell_value(x + 3, y + 3) == 0
                                    # or 3 combo horizontal by column and space on the left
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y + 1)
                                    == board.get_cell_value(x + 2, y + 2)
                                    == enemyID
                                    and board.get_cell_value(x - 1, y - 1) == 0
                                ):
                                    heuristicValue -= 1200

                except:
                    pass
                # if current player is the second player
                # format 1011 or 1101 negative diagonal
                try:
                    if currentID == 2:
                        if x < 7:

                            # 2 combo negative diagonal and space on the right, open space AND another piece on the right
                            # 1 1 0 1 format

                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y + 1)
                                == board.get_cell_value(x + 3, y + 3)
                                == enemyID
                                and board.get_cell_value(x + 2, y + 2) == 0
                                # or by negative diagonal, 1 0 1 1 format
                            ) or (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 2, y + 2)
                                == board.get_cell_value(x + 3, y + 3)
                                == enemyID
                                and board.get_cell_value(x + 1, y + 1) == 0
                            ):
                                heuristicValue -= 1200
                except:
                    pass
                # if current player is the second player
                # format 1011 or 1101 postive diagonal
                try:
                    if currentID == 2:
                        if x < 7:

                            # 2 combo positive diagonal
                            # 1 1 0 1 format

                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 3, y + 3)
                                == enemyID
                                and board.get_cell_value(x - 2, y + 2) == 0
                            ) or (
                                # or by postive diagonal, 1 0 1 1 format
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 2, y + 2)
                                == board.get_cell_value(x - 3, y + 3)
                                == enemyID
                                and board.get_cell_value(x - 1, y + 1) == 0
                            ):
                                heuristicValue -= 1200
                except:
                    pass

                # if current player is the second player
                # format 1011 or 1101 horizontal by column
                try:
                    if currentID == 2:
                        if x < 7:

                            # 2 combo Vertical row
                            # 1 1 0 1 format

                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 3, y + 3)
                                == enemyID
                                and board.get_cell_value(x - 2, y + 2) == 0
                            ) or (
                                # or by postive diagonal, 1 0 1 1 format
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 2, y + 2)
                                == board.get_cell_value(x - 3, y + 3)
                                == enemyID
                                and board.get_cell_value(x - 1, y + 1) == 0
                            ):
                                heuristicValue -= 1200
                except:
                    pass
                # OFFENSIVE HEURISTIC PLAYER 1
                #combo horizontal empty space either side
                # if current player is the first player
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:
                            if y < 7:
                                # 2 combo horizontal by column for the enemy and there
                                # is an open space on the right
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x, y + 1)
                                    == currentID
                                    and board.get_cell_value(x, y + 2) == 0
                                    # or there is an open space on the left side of the 2 combo horizontal
                                    # by column
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x, y + 1)
                                    == currentID
                                    and board.get_cell_value(x, y - 1) == 0
                                ):
                                    heuristicValue += 50

                                # 3 combo horizontal by column and theres space on the right side
                                # for enemy
                                if y < 4:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x, y + 1)
                                        == board.get_cell_value(x, y + 2)
                                        == currentID
                                        and board.get_cell_value(x, y + 3) == 0
                                        # or 3 combo horizontal by column and space on the left
                                    ) or (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x, y + 1)
                                        == board.get_cell_value(x, y + 2)
                                        == currentID
                                        and board.get_cell_value(x, y - 1) == 0
                                    ):
                                        heuristicValue += 1200

                except:
                    pass
                #combo vertical
                # if current player is the first player
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:
                            if y < 7:
                                # 2 combo vertical by row for the enemy and there
                                # is an open space on the right
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y)
                                    == currentID
                                    and board.get_cell_value(x + 2, y) == 0
                                    # or there is an open space on the left side of the 2 combo vertical
                                    # by row
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y)
                                    == currentID
                                    and board.get_cell_value(x - 1, y) == 0
                                ):
                                    heuristicValue += 50

                                # 3 combo horizontal by column and theres space on the right side
                                # for enemy
                                if y < 7:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x + 1, y)
                                        == board.get_cell_value(x + 2, y)
                                        == currentID
                                        and board.get_cell_value(x + 3, y) == 0
                                        # or 3 combo horizontal by column and space on the left
                                    ) or (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x + 1, y)
                                        == board.get_cell_value(x + 2, y)
                                        == currentID
                                        and board.get_cell_value(x - 1, y) == 0
                                    ):
                                        heuristicValue += 1200

                except:
                    pass
                #combo positive diagonal 
                # if current player is the first player
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:
                            if y < 7:
                                # 2 combo postive diagonal
                                # is an open space on the right
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x - 1, y+1)
                                    == currentID
                                    and board.get_cell_value(x - 2, y+2) == 0
                                    # or there is an open space on the left side of the 2 combo postive diagonal
                                    # by row
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x - 1, y+1)
                                    == currentID
                                    and board.get_cell_value(x + 1, y-1) == 0
                                ):
                                    heuristicValue += 50

                                # 3 combo postive diagonal
                                # f
                                if y < 7:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x - 1, y+1)
                                        == board.get_cell_value(x -2, y+2)
                                        == currentID
                                        and board.get_cell_value(x - 3, y+3) == 0
                                        # or 3 combo horizontal by column and space on the left
                                    ) or (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x - 1, y+1)
                                        == board.get_cell_value(x - 2, y+2)
                                        == currentID
                                        and board.get_cell_value(x + 1, y-1) == 0
                                    ):
                                        heuristicValue += 1200

                except:
                    pass

                #combo negative diagonal 
                # if current player is the first player
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:
                            if y < 7:
                                # 2 combo postive diagonal
                                # is an open space on the right
                                if (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y+1)
                                    == currentID
                                    and board.get_cell_value(x + 2, y+2) == 0
                                    # or there is an open space on the left side of the 2 combo postive diagonal
                                    # by row
                                ) or (
                                    board.get_cell_value(x, y)
                                    == board.get_cell_value(x + 1, y+1)
                                    == currentID
                                    and board.get_cell_value(x - 1, y-1) == 0
                                ):
                                    heuristicValue += 50

                                # 3 combo postive diagonal
                                # f
                                if y < 7:
                                    if (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x + 1, y+1)
                                        == board.get_cell_value(x +2, y+2)
                                        == currentID
                                        and board.get_cell_value(x + 3, y+3) == 0
                                        # or 3 combo postive diagonal
                                    ) or (
                                        board.get_cell_value(x, y)
                                        == board.get_cell_value(x + 1, y+1)
                                        == board.get_cell_value(x + 2, y+2)
                                        == currentID
                                        and board.get_cell_value(x - 1, y-1) == 0
                                    ):
                                        heuristicValue += 1200

                except:
                    pass
                # if current player is the first player
                # format 1011 or 1101 horizontal by column
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:

                            # 2 combo Vertical row
                            # 1 1 0 1 format

                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 3, y + 3)
                                == currentID
                                and board.get_cell_value(x - 2, y + 2) == 0
                            ) or (
                                # or by postive diagonal, 1 0 1 1 format
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 2, y + 2)
                                == board.get_cell_value(x - 3, y + 3)
                                == currentID
                                and board.get_cell_value(x - 1, y + 1) == 0
                            ):
                                heuristicValue += 1200
                except:
                    pass
            
                # if current player is the first player
                # format 1011 or 1101 negative diagonal
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:

                            # 2 combo negative diagonal and space on the right, open space AND another piece on the right
                            # 1 1 0 1 format

                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 1, y + 1)
                                == board.get_cell_value(x + 3, y + 3)
                                == currentID
                                and board.get_cell_value(x + 2, y + 2) == 0
                                # or by negative diagonal, 1 0 1 1 format
                            ) or (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x + 2, y + 2)
                                == board.get_cell_value(x + 3, y + 3)
                                == currentID
                                and board.get_cell_value(x + 1, y + 1) == 0
                            ):
                                heuristicValue += 1200
                except:
                    pass
                # if current player is the first player
                # format 1011 or 1101 postive diagonal
                try:
                    if currentID == 1 or currentID == 2:
                        if x < 7:

                            # 2 combo positive diagonal
                            # 1 1 0 1 format

                            if (
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 1, y + 1)
                                == board.get_cell_value(x - 3, y + 3)
                                == currentID
                                and board.get_cell_value(x - 2, y + 2) == 0
                            ) or (
                                # or by postive diagonal, 1 0 1 1 format
                                board.get_cell_value(x, y)
                                == board.get_cell_value(x - 2, y + 2)
                                == board.get_cell_value(x - 3, y + 3)
                                == currentID
                                and board.get_cell_value(x - 1, y + 1) == 0
                            ):
                                heuristicValue += 1200
                except:
                    pass

                
        return heuristicValue
