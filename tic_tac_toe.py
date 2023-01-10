def play_tic_tac_toe():
  # In the beginning, the tic-tac-toe board was created and it was empty, with no form or substance
  board = [[' ' for _ in range(3)] for _ in range(3)]

  # And the game began, with X going first
  current_player = 'X'
  game_over = False

  # And the game continued, with the players taking turns and marking the board
  while not game_over:
    # And the board was displayed for all to see
    print_board(board)

    # And the current player made their move, choosing a spot on the board
    if current_player == 'X':
      row, col = get_next_move(board, current_player)
    else:
      row, col = get_computer_move(board)

    # And the move was made, the player's symbol placed on the board
    board[row][col] = current_player
    # And the turn passed to the other player
    current_player = 'O' if current_player == 'X' else 'X'

    # And it was determined whether the game was over
    game_over = check_game_over(board)

  # And the final state of the board was displayed
  print_board(board)
  # And it was declared who had won, or if the game was a tie
  if check_win(board, 'X'):
    print("X wins!")
  elif check_win(board, 'O'):
    print("computer wins!")
  else:
    print("It's a tie!")

def print_board(board):
  print("   |   |")
  print(" {} | {} | {}".format(board[0][0], board[0][1], board[0][2]))
  print("   |   |")
  print("-----------")
  print("   |   |")
  print(" {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
  print("   |   |")
  print("-----------")
  print("   |   |")
  print(" {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))
  print("   |   |")

def get_next_move(board, player):
  valid_move = False
  while not valid_move:
    move = input("{}, enter your move (row column): ".format(player))
    row, col = map(int, move.split())
    if row in range(3) and col in range(3) and board[row][col] == ' ':
      valid_move = True
    else:
      print("Invalid move. Try again.")
  return row, col

def check_game_over(board):
  # Check if X has won
  if check_win(board, 'X'):
    return True

  # Check if O has won
  if check_win(board, 'O'):
    return True

  # Check if the board is full (game is a tie)
  if all(all(square != ' ' for square in row) for row in board):
    return True

  # Game is not over
  return False

def check_win(board, player):
  # Check rows
  for row in board:
    if all(square == player for square in row):
      return True

  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  # Check diagonals
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2 - i] == player for i in range(3)):
    return True

  # Player has not won
  return False

def get_computer_move(board):
  # Check if the computer can win in one move
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        board[i][j] = 'O'
        if check_win(board, 'O'):
          return i, j
        board[i][j] = ' '

  # Check if the player can win in one move and block them
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        board[i][j] = 'X'
        if check_win(board, 'X'):
          return i, j
        board[i][j] = ' '

  # Try to take one of the corner squares
  corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
  for i, j in corners:
    if board[i][j] == ' ':
      return i, j

  # Try to take the center square
  if board[1][1] == ' ':
    return 1, 1

  # Take any remaining square
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        return i, j

