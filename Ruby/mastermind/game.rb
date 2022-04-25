# frozen_string_literal: true

require './display'
require './players'

# handles game flow/loop

display = Display.new
human = Players.new
computer = Players.new

if human.start == 'b'
  display.new_code('no code')
  breaker_loop = true
else
  maker_loop = true
end

while breaker_loop
  human.rounds(display.next_round)
  display.pegs(human.ask_code)
  display.feedback
  abort if human.ending(display.result)
end

while maker_loop
  display.new_code(computer.ask_code) # need to get the code from the player
  computer.rounds(display.next_round)
  display.pegs(computer.thinking) # puts something like "computer is making its guess"
  display.feedback
  abort if computer.ending(display.result)
end
