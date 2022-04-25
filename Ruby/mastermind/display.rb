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

  def new_code(user_code = 'no code')
    @vanity_code = []
    @generated_code = []
    if user_code == 'no code'
      4.times { @generated_code.push(@code_colors[rand(6)]) }
      @generated_code.each { |g| @vanity_code.push(@code_pegs[g]) }
      puts @vanity_code.join(' ')
    else
      user_code.each { |g| @vanity_code.push(@code_pegs[g]) }
      puts "You have selected the code #{@vanity_code.join(' ')}"
      @generated_code = user_code
    end
  end

  # code maker only
  def make_a_code
    @vanity_make_code = []
    @make_code = []
    4.times { @make_code.push(@code_colors[rand(6)]) }
    @make_code.each { |g| @vanity_make_code.push(@code_pegs[g]) }
    @make_code
  end

  def pegs(guess)
    if guess == 12
      @player_code = make_a_code
      puts @vanity_make_code.join(' ')
    else
      output = []
      guess.each { |g| output.push(@code_pegs[g]) }
      puts output.join(' ')
      @player_code = guess
    end
  end

  def feedback
    if @player_code == @generated_code
      @round = 0
      @win = true
      puts "You found the code! (#{@vanity_code.join(' ')})"
    elsif @player_code.length != 4 || @player_code.all? { |g| @code_colors.include?(g).! }
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
    puts "the code was #{@vanity_code.join(' ')}"
    @round = 0
    new_code
    'lost'
  end
end
