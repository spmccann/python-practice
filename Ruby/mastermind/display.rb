# frozen_string_literal: true

require 'colorize'

# displays game updates
class Display
  attr_accessor(:name)

  def initialize
    @dcode_pegs = {
      'red': '■'.red, 'blue': '■'.blue, 'yellow': '■'.yellow, 'green': '■'.green, 'white': '■'.white, 'purple': '■'.magenta
    }
    @code_colors = %i[red blue yellow green white purple]
    @key_pegs = { 'red': '■'.red, 'white': '■'.white }
    @key_colors = %i[red white]
  end

  def start
    puts 'Mastermind: A Game of Codemakers and Codebreakers'
    # puts 'The computer player selects 4 Code Pegs. With the color and order of pegs of their choice.'
    # puts 'You have 10 rounds to try to guess the 4 Code Peg\'s exact colors and order'
    # puts 'After each round, you will feedback on your guess with 0- 4 Key Pegs'
    # puts 'White Key Peg -- right color, wrong position, red Key Peg -- right color, right position'
    # puts 'Key Peg feedback is not in any specific order. Good luck!'
    puts 'What is your name?'
    @name = gets.chomp
  end

  def new_code
    @random_code = @code_colors.sample(4)
    puts @random_code
  end

  def guesses(guess)
    @output = []
    if guess.length == 4 && guess.all? { |g| @code_colors.include?(g) }
      @player_code = guess
      guess.each { |g| output.push(@code_pegs[g]) }
    else
      puts 'invalid guesses. Please try again. '
    end
    puts @output.join(' ')
  end

  def checks
    if @player_code == @random_code
      puts 'You found the code!'
    else
      @player_code.each_index do |i|
        if @player_code[i] == @random_code[i]
          puts "#{key_peg[0]} right color, right postion"
        elsif @random_code.include?(player_code[i])
          puts "#{key_peg[1]} right color, wrong position"
        else
          puts 'None of your pegs are in the code!'
        end
      end
    end
  end

  def reset
    @colors.sample(4)
  end
end
