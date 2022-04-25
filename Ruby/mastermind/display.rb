# frozen_string_literal: true

require 'colorize'

# displays game updates
class Display
  def initialize
    @code_pegs = {
      'red': '■'.red, 'blue': '■'.blue, 'yellow': '■'.yellow,
      'green': '■'.green, 'white': '■'.white, 'purple': '■'.magenta
    }
    @code_colors = %i[red blue yellow green white purple]
    @round = 0
  end

  def new_code
    @round_code = []
    @generated_code = @code_colors.sample(4)
    @generated_code.each { |g| @round_code.push(@code_pegs[g]) }
    puts @round_code.join(' ')
  end

  def guesses(guess)
    output = []
    guess.each { |g| output.push(@code_pegs[g]) } if guess.length == 4 && guess.all? { |g| @code_colors.include?(g) }
    puts output.join(' ')
    @player_code = guess
  end

  def feedback
    if @player_code == @generated_code
      @round = 0
      @win = true
      puts "You found the code! (#{@round_code.join(' ')})"
    elsif @player_code.nil?
      puts 'invalid guess. Please try again. '
      @round -= 1
    else
      check_matches
    end
  end

  def check_matches
    count = 0
    @player_code.each_index do |i|
      if @player_code[i] == @generated_code[i]
        puts 'Correct color, correct postion'
      elsif @generated_code.include?(@player_code[i])
        puts 'Correct color, incorrect position'
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
    if @round > 11
      lost
    elsif @win
      win
    else
      'game continues'
    end
  end

  def win
    @win = false
    new_code
    'won'
  end

  def lost
    puts "the code was #{@round_code.join(' ')}"
    @round = 0
    new_code
    'lost'
  end
end
