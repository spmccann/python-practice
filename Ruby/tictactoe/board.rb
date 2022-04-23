# frozen_string_literal: true

require './flow'

# board upates
class Board < Flow
  def initialize
    super
    @squares = Array.new(9, ' ')
  end

  def example_display
    puts "
    ---------
      0|1|2
      -+-+-
      3|4|5
      -+-+-
      6|7|8
    ---------
    "
  end

  def display
    puts "    Live Board
    ---------
      #{@squares[0]}|#{@squares[1]}|#{@squares[2]}
      -+-+-
      #{@squares[3]}|#{@squares[4]}|#{@squares[5]}
      -+-+-
      #{@squares[6]}|#{@squares[7]}|#{@squares[8]}
    ---------
    "
  end

  def placement(place, player)
    player == 'x' ? (@squares[place] = 'X') : @squares[place] = 'O'
  end

  def reset_board
    @squares = Array.new(9, ' ')
  end

  def tie
    reset_board unless @squares.include?(' ')
  end

  def win_cases
    x = %w[X X X]
    o = %w[O O O]
    top = @squares.values_at(0, 1, 2)
    mid = @squares.values_at(3, 4, 5)
    bot = @squares.values_at(6, 7, 8)
    left = @squares.values_at(0, 3, 6)
    center = @squares.values_at(1, 4, 7)
    right = @squares.values_at(2, 5, 8)
    l_diag = @squares.values_at(0, 4, 8)
    r_diag = @squares.values_at(2, 4, 6)
    wins = [top, mid, bot, left, center, right, l_diag, r_diag]
    if wins.include?(x)
      reset_board
      puts "#{flow.names[0]} wins the game!"
    elsif wins.include?(o)
      reset_board
      puts "#{flow.names[1]} wins the game!"
    end
  end

  def open_square(sqr)
    @squares[sqr] == ' '
  end
end
