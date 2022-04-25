# frozen_string_literal: true

require './display'
require './players'

# handles game flow/loop

display = Display.new
player = Players.new
game_loop = true
player.start
display.new_code

while game_loop
  player.rounds(display.next_round)
  display.guesses(player.guess)
  display.feedback
  abort if player.ending(display.result)
end
