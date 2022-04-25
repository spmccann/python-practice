# frozen_string_literal: true

# player messaging
class Players
  def start
    puts 'Welcome to Mastermind: A Game of Codemakers and Codebreakers'
  end

  def guess
    puts 'Please enter 4 colors (red, blue, yellow, green, white or purple):'
    gets.chomp.downcase.split.map(&:to_sym)
  end

  def rounds(round)
    puts "\nMastermind Round #{round} (of 12)"
  end

  def ending(result)
    case result
    when 'won'
      puts 'You won the game. Would you like you play again? (y/n)?'
      gets.chomp == 'n'
    when 'lost'
      puts 'You lost. The codemaker won. Would you like you play again? (y/n)?'
      gets.chomp == 'n'
    end
  end
end
