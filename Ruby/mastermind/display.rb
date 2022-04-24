# frozen_string_literal: true

require 'colorize'

# displays game updates
class Display
  def initialize
    @code_pegs = {
      'red': '■'.red, 'blue': '■'.blue, 'yellow': '■'.yellow, 'green': '■'.green, 'white': '■'.white, 'purple': '■'.magenta
    }
    @code_colors = %i[red blue yellow green white purple]
    @round = 0
  end

  def new_code
    output = []
    @generated_code = @code_colors.sample(4)
    @generated_code.each { |g| output.push(@code_pegs[g]) }
    puts output.join(' ')
  end

  def guesses(guess)
    output = []
    if guess.length == 4 && guess.all? { |g| @code_colors.include?(g) }
      guess.each { |g| output.push(@code_pegs[g]) }
    else
      puts 'invalid guesses. Please try again. '
      @round -= 1
    end
    puts output.join(' ')
    @player_code = guess
  end

  def feedback
    if @player_code == @generated_code
      @win = true
      puts 'You found the code!'
    else
      check_matches
    end
  end

  def check_matches
    count = 0
    @player_code.each_index do |i|
      if @player_code[i] == @generated_code[i]
        puts 'right color, right postion'
      elsif @generated_code.include?(@player_code[i])
        puts 'right color, wrong position'
      else
        count += 1
        puts 'None of your pegs are in the code!' if count == 4
      end
    end
  end

  def next_round
    @round += 1
  end

  def result
    if @round > 9
      @round = 0
      new_code
      'lost'
    elsif @win
      @round = 0
      @win = false
      new_code
      'won'
    else
      'game continues'
    end
  end
end
