# frozen_string_literal: true

require './player'
require './board'
require './flow'

board = Board.new
flow = GameFlowMessages.new

flow.start_game ? game_start = true : abort
flow.player_names
board.example_display

while game_start
  choice = flow.make_move('x')
  board.placement(choice, 'x')
  board.display
  choice = flow.make_move('o')
  board.placement(choice, 'o')
  board.display
  game_start = false
end
