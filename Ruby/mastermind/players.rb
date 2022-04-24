# frozen_string_literal: true

# player creation and abilities
class Players
  attr_accessor(:name)

  def initialize(name)
    @name = name
  end

  def guess
    puts 'Please enter 4 colors (red, blue, yellow, green, white, purple)'
    gets.chomp.split.map(&:to_sym)
  end
end
