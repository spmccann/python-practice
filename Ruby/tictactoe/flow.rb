# frozen_string_literal: true

# messages to players to create flow of game
class GameFlowMessages
  attr_accessor(:names)

  def start_game
    puts "2-Player Tic Tac Toe\nNew Game? (yes/no)"
    gets.downcase.chomp == 'yes'
  end

  def player_names
    puts 'Please enter the names for player one and player two (e.g Scott Mireya): '
    @names = gets.chomp.split
    puts "Hello, #{@names[0]} and #{@names[1]}!"
    puts "\nYou can make your move by entering the corresponding square number"
  end

  def make_move(turn)
    if turn == 'x'
      puts "#{names[0]}, mark a square for 'X' (0-8): "
    else
      puts "#{names[1]}, mark a square for 'O' (0-8):  "
    end
    gets.chomp.to_i
  end
end
