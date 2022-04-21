def caesar_cipher(string, shift)
  alpha = ('a'..'z').to_a
  up_alpha = ('A'..'Z').to_a
  output = []
  beforer_cipher = string.split('')
  beforer_cipher.each do |letter|
    if alpha.include?(letter)
      new_let_idx = alpha.index(letter) + shift
      if (new_let_idx) < 26
        output += [alpha[new_let_idx]]
      else output += [alpha[new_let_idx % 26]] 
      end
    elsif up_alpha.include?(letter)
      new_let_idx = up_alpha.index(letter) + shift
      if (new_let_idx) < 26
        output += [up_alpha[new_let_idx]]
      else output += [up_alpha[new_let_idx % 26]] 
      end
    else output += [letter]
    end
  end
  after_cipher = output.join("")
  puts after_cipher
end
    
caesar_cipher("What a string!", 5)
