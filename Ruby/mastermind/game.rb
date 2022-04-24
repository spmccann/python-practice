# frozen_string_literal: true

require './display'
require './players'
require 'colorize'

# handles game flow/loop

display = Display.new
human = Players.new(display.start)
game_loop = true
display.new_code


while game_loop
  display.guesses(human.guess)
end
