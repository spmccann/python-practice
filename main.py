# def string_times(str_1, n):
#     new_str = ""
#     for _ in range(n):
#         new_str += str_1
#     print(new_str)
#
#
# string_times("hi", 2)


# def front_times(str1, n):
#     newstr = ""
#     for _ in range(n):
#         newstr += str1[:3]
#     print(newstr)
#
#
# front_times("Abc", 3)

# def string_bits(str1):
#     newstr = ""
#     for i in range(len(str1)):
#         if i % 2 == 0:
#             newstr += str1[i]
#     print(newstr)
#
# string_bits("Heeololeo")

# Takes a number and returns it from highest to lowest
# def descending_order(num):
#     sort = sorted(str(num), reverse=True)
#     to_num = "".join(sort)
#     return int(to_num)
#
#
# descending_order(1843)

# returns the index for letters in a string
# def alphabet_position(text):
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#     position_ints = [alphabet.index(letter) + 1 for letter in text.lower() if letter in alphabet]
#     string_ints = [str(p_int) for p_int in position_ints]
#     position_string = " ".join(string_ints)
#     return position_string
#
#
# alphabet_position("The sunset sets at twelve o' clock.")

# find 1 even/odd in list of all even or odds
# def find_outlier(integers):
#     outlier = [integer for integer in integers if integer % 2 == 0]
#     outlier2 = [integer for integer in integers if integer % 2 != 0]
#     if len(outlier) < 2:
#         return outlier[0]
#     else:
#         return outlier2[0]
#
#
# find_outlier([160, 3, 1719, 19, 11, 13, -21])


# check for same number of 'x's and 'o's
# def xo(s):
#     test_s = s.lower()
#     x_count = [x for x in test_s if x == "x"]
#     o_count = [o for o in test_s if o == "o"]
#     if len(x_count) == len(o_count):
#         return True
#     else:
#         return False
#
#
# xo("xooxx")

# check for narcissistic numbers
# def narcissistic_number(num):
#     number = [int(n) for n in str(num)]
#     squared_add = sum([n**len(number) for n in number])
#
#     if squared_add == num:
#         return True
#     else:
#         return False
#
#
# narcissistic_number(153)

# remove vowels
# def troll(comment):
#     chars = "aeiouAEIOU"
#     for c in chars:
#         comment = comment.replace(c, "")
#     print(comment)
#
#
# troll("This website is for losers LOL!")
# import math

# returns true if number is square
# def squares(n):
#     if n > 0:
#         value = n**0.5
#     return value.is_integer()
#
#
# squares(81)

# # returns unique ordered values from a list
# def unique_in_order(n):
#     unique = []
#     add_to = [unique.append(a) for a in n if a not in unique[-1:]]
#     return unique
#
#
# unique_in_order('AAAABBBCCDAABBB')

# find prime numbers
# def is_prime(num):
#     count = 0
#     if num >= 2:
#         if num == 2 or num % 2 != 0:
#             for n in range(3, num+1, 2):
#                 if num % n == 0:
#                     count += 1
#             if count > 1:
#                 return False
#             else:
#                 return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(is_prime(2))

# calculate the number of bounces seen given height, bouncy-ness and window height
# def bounce_balls(h, bounce, window):
#     count = 1
#     ball = h
#     while h > 0 and 0 < bounce < 1 and window < h and ball > window:
#         count += 2
#         ball *= bounce
#         print(ball)
#
#     return count - 2
#
#
# print(bounce_balls(3, .66, 1.5))


# return the middle character or middle 2 characters
# import math
#
#
# def get_middle(n):
#     if len(n) % 2 == 0:
#         position1 = math.floor(len(n)/2)
#         position2 = math.ceil(len(n)/2)
#         middle = n[position1-1] + n[position2]
#         return middle
#     else:
#         return n[math.ceil(len(n)/2)-1]
#
#
# print(get_middle("testing"))

#  returns a phone number from numbers in an array
# def phone_number(a):
#     number = "".join(str(n) for n in a)
#     pn = f"({number[0:3]}) {number[3:6]}-{number[6:10]} "
#     return pn
#
#
# phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# prints name that hit like button and "and 2 others" for 4 or more
#
# def like_button(names):
#     if len(names) < 1:
#         blank = "no one likes this"
#         return blank
#     elif len(names) < 2:
#         output = f"{names[0]} likes this"
#         return output
#     elif len(names) < 3:
#         output = f"{names[0]} and {names[1]} like this"
#         return output
#     elif len(names) < 4:
#         output = f"{names[0]}, {names[1]} and {names[2]} like this"
#         return output
#     else:
#         more_output = f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
#         return more_output
#
#
# print(like_button(["Peter"]))

# equal sides of an array DOES NOT WORK
#
# def arr_sum(arr):
#     total = 0
#     half = 0
#     for n in arr:
#         total += n
#     print(total)
#     for n in arr:
#         if n < total/2:
#             half += n
#             print(half)
# #             return half
# #         else:
# #             return -1
#
#
# print(arr_sum([1, 2, 3, 4, 3, 2, 1]))


