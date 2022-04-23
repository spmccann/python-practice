# frozen_string_literal: true

# board upates
class Board
  def initialize
    @squares = Array.new(9, ' ')
  end

  def example_display
    puts "
      0|1|2
      -+-+-
      3|4|5
      -+-+-
      6|7|8
    "
  end

  def display
    puts "  Board\n
      #{@squares[0]}|#{@squares[1]}|#{@squares[2]}
      -+-+-
      #{@squares[3]}|#{@squares[4]}|#{@squares[5]}
      -+-+-
      #{@squares[6]}|#{@squares[7]}|#{@squares[8]}
    "
  end

  def placement(place, player)
    @squares[place] = 'X' if player == 'x' || (@squares[place] = 'o')
  end
end
