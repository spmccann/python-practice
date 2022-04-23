puts "2 Player Tic Tac Toe\nNew Game? (yes/no)"
answer = gets.downcase
if answer == 'yes'
  game_start = true
else
  puts 'goodbye'
end


puts "  Board\n
  0|1|2
  -+-+-
  3|4|5
  -+-+-
  6|7|8
"

while game_start
  puts 'Select a square (0-8): '
  square_choice = gets
  game_start = false
end

