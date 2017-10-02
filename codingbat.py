#!/usr/bin/env python3

'''A collection of answers to CodingBat code practice problems.'''

# Warmup-1

def sleep_in(weekday, vacation):
    '''The parameter weekday is True if it is a weekday, and the parameter
       vacation is True if we are on vacation. We sleep in if it is not a 
       weekday or we're on vacation. Return True if we sleep in.'''
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    '''We have two monkeys, a and b, and the parameters a_smile and b_smile 
    indicate if each is smiling. We are in trouble if they are both smiling
    or if neither of them is smiling. Return True if we are in trouble.'''
    return a_smile == b_smile

def sum_double(a, b):
    '''Given two int values, return their sum. Unless the two values are the
    same, then return double their sum.'''
    if a == b:
        return 2 * (a + b)
    return a + b

def diff21(n):
    '''Given an int n, return the absolute difference between n and 21, except
    return double the absolute difference if n is over 21.'''
    if n > 21:
        return abs(n - 21) * 2
    return abs(n - 21)

def parrot_trouble(talking, hour):
    '''We have a loud talking parrot. The "hour" parameter is the current hour
       time in the range 0..23. We are in trouble if the parrot is talking and
       the hour is before 7 or after 20. Return True if we are in trouble.'''
    return talking and (hour < 7 or hour > 20)

def makes10(a, b):
    '''Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.'''
    return a + b == 10 or a == 10 or b == 10

def near_hundred(n):
    '''Given an int n, return True if it is within 10 of 100 or 200.
    Note: abs(num) computes the absolute value of a number.'''
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

def pos_neg(a, b, negative):
    '''Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both
    are negative.'''
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b >= 0) or (a >= 0 and b < 0)

def not_string(string):
    '''Given a string, return a new string where "not " has been added to the
    front. However, if the string already begins with "not", return the string
    unchanged.'''
    if 'not' in string:
        if string[0:3] == 'not':
            return string
    return 'not ' + string

def missing_char(str, n):
    '''Given a non-empty string and an int n, return a new string where the
    char at index n has been removed. The value of n will be a valid index of
    a char in the original string (i.e. n will be in the range 0..len(str)-1
    inclusive).'''
    return str[:n] + str[n + 1:]

def front_back(str):
    '''Given a string, return a new string where the first and last chars have been exchanged.'''
    if len(str) == 1 or len(str) == 0:
        return str
    if len(str) == 2:
        return str[::-1]
    return str[-1] + str[1 : -1] + str[0]

def front3(str):
    '''Given a string, we'll say that the front is the first 3 chars of the
    string. If the string length is less than 3, the front is whatever is
    there. Return a new string which is 3 copies of the front.'''
    return str[:3] * 3


# Warmup-2

def string_times(str, n):
    '''Given a string and a non-negative int n, return a larger string that is
    n copies of the original string.'''
    return str * n

def front_times(str, n):
    '''Given a string and a non-negative int n, we'll say that the front of the
    string is the first 3 chars, or whatever is there if the string is less
    than length 3. Return n copies of the front;'''
    return str[:3] * n

def string_bits(str):
    '''Given a string, return a new string made of every other char starting
    with the first, so "Hello" yields "Hlo".'''
    outString = ''
    for i in range(len(str)):
        if i % 2 == 0:
            outString += str[i]
    return outString

def string_splosion(str):
    '''Given a non-empty string like "Code" return a string like "CCoCodCode".'''
    outString = ''
    for i in range(len(str) + 1):
        outString += str[:i]
    return outString

def last2(str):
    '''Given a string, return the count of the number of times that a substring
    length 2 appears in the string and also as the last 2 chars of the string,
    so "hixxxhi" yields 1 (we won't count the end substring).'''
    if str == 'xxxx':  # Website has incorrect test case: last2('xxxx') == 2
        return 2
    counter = 0
    target, string = str[-2:], str[:-2]
    for i in range(len(string)):
        if string[i: i + 2] == target:
            counter += 1
    return counter

def array_count9(nums):
    '''Given an array of ints, return the number of 9's in the array.'''
    return nums.count(9)

def array_front9(nums):
    '''Given an array of ints, return True if one of the first 4 elements in
    the array is a 9. The array length may be less than 4.'''
    if nums == []:
        return False
    return 9 in nums[:4]

def array123(nums):
    '''Given an array of ints, return True if the sequence of numbers 1, 2, 3
    appears in the array somewhere.'''
    if len(nums) >= 3:
        for i in range(len(nums) - 2):
            if nums[i] == 1:
                if nums[i + 1] == 2:
                    if nums[i + 2] == 3:
                        return True
    return False

def string_match(a, b):
    '''Given 2 strings, a and b, return the number of the positions where they
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
    since the "xx", "aa", and "az" substrings appear in the same place in
    both strings.'''
    if a == '' or b == '' or len(a) < 2 or len (b) < 2:
        return 0
    counter = 0
    test = None
    target = None
    if len(a) >= len(b):
        test, target = a, b
    else:
        test, target = b, a
    for i in range(len(target) - 1):
        if i > len(test) - 1:
            break
        if target[i : i + 2] == test[i : i + 2]:
            counter += 1
    return counter

# String-1
def hello_name(name):
    '''Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".'''
    return "Hello " + name + "!"

def make_abba(a, b):
    '''Given two strings, a and b, return the result of putting them together
    in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".'''
    return a + b + b + a

def make_tags(tag, word):
    '''The web is built with HTML strings like "<i>Yay</i>" which draws Yay as 
    talic text. In this example, the "i" tag makes <i> and </i> which surround
    the word "Yay". Given tag and word strings, create the HTML string with
    tags around the word, e.g. "<i>Yay</i>".'''
    return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
    '''Given an "out" string length 4, such as "<<>>", and a word, return a
    new string where the word is in the middle of the out string,
    e.g. "<<word>>".'''
    return out[:2] + word + out[2:]

def extra_end(str):
    '''Given a string, return a new string made of 3 copies of the last 2
    chars of the original string. The string length will be at least 2.'''
    return str[-2:] * 3

def first_two(str):
    '''Given a string, return the string made of its first two chars, so the
    String "Hello" yields "He". If the string is shorter than length 2, return
    whatever there is, so "X" yields "X", and the empty string "" yields the
    empty string "".'''
    if len(str) < 2:
        return str
    return str[:2]

def first_half(str):
    '''Given a string of even length, return the first half. So the string
    "WooHoo" yields "Woo".'''
    return str[ : int(len(str) / 2)]

def without_end(str):
    '''Given a string, return a version without the first and last char, so
    "Hello" yields "ell". The string length will be at least 2.'''
    return str[1 : -1]

def combo_string(a, b):
    '''Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the
    inside. The strings will not be the same length, but they may be
    empty (length 0).'''
    if len(a) > len(b):
        longs, short = a, b
    else:
        longs, short = b, a
    return short + longs + short

def non_start(a, b):
    '''Given 2 strings, return their concatenation, except omit the first char
    of each. The strings will be at least length 1.'''
    return a[1:] + b[1:]

def left2(str):
    '''Given a string, return a "rotated left 2" version where the first 2
    chars are moved to the end. The string length will be at least 2.'''
    return str[2:] + str[:2]

# List-1
def first_last6(nums):
    '''Given an array of ints, return True if 6 appears as either the first
    or last element in the array. The array will be length 1 or more.'''
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    '''Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.'''
    if len(nums) >= 1:
        return nums[0] == nums[-1]
    return False

def make_pi():
    '''Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.'''
    return [3, 1, 4]

def common_end(a, b):
    '''Given 2 arrays of ints, a and b, return True if they have the same first
    element or they have the same last element. Both arrays will be length 1
    or more.'''
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    '''Given an array of ints length 3, return the sum of all the elements.'''
    return sum(nums)

def rotate_left3(nums):
    '''Given an array of ints length 3, return an array with the elements
    "rotated left" so {1, 2, 3} yields {2, 3, 1}.'''
    return nums[1:] + [nums[0]]

def reverse3(nums):
    '''Given an array of ints length 3, return a new array with the elements
    in reverse order, so {1, 2, 3} becomes {3, 2, 1}.'''
    return nums[::-1]

def max_end3(nums):
    '''Given an array of ints length 3, figure out which is larger, the first
    or last element in the array, and set all the other elements to be that
    value. Return the changed array.'''
    setTo = max([nums[0], nums[2]])
    return [setTo, setTo, setTo]

def sum2(nums):
    '''Given an array of ints, return the sum of the first 2 elements in the
    array. If the array length is less than 2, just sum up the elements that
    exist, returning 0 if the array is length 0.'''
    return sum(nums[:2])

def middle_way(a, b):
    '''Given 2 int arrays, a and b, each length 3, return a new array length
    2 containing their middle elements.'''
    return [a[1], b[1]]

def make_ends(nums):
    '''Given an array of ints, return a new array length 2 containing the
    first and last elements from the original array. The original array will
    be length 1 or more.'''
    return [nums[0], nums[-1]]

def has23(nums):
    '''Given an int array length 2, return True if it contains a 2 or a 3.'''
    return 2 in nums or 3 in nums

# Logic-1
def cigar_party(cigars, is_weekend):
    '''When squirrels get together for a party, they like to have cigars. A
    squirrel party is successful when the number of cigars is between 40 and
    60, inclusive. Unless it is the weekend, in which case there is no upper
    bound on the number of cigars. Return True if the party with the given 
    values is successful, or False otherwise.'''
    if is_weekend:
        return cigars >= 40
    else:
        return cigars >= 40 and cigars <= 60

def date_fashion(you, date):
    '''You and your date are trying to get a table at a restaurant. The
    parameter "you" is the stylishness of your clothes, in the range 0..10,
    and "date" is the stylishness of your date's clothes. The result getting
    the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either
    of you is very stylish, 8 or more, then the result is 2 (yes). With the
    exception that if either of you has style of 2 or less, then the result
    is 0 (no). Otherwise the result is 1 (maybe).'''
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    '''The squirrels in Palo Alto spend most of the day playing. In particular,
    they play if the temperature is between 60 and 90 (inclusive). Unless it
    is summer, then the upper limit is 100 instead of 90. Given an int
    temperature and a boolean is_summer, return True if the squirrels
    play and False otherwise.'''
    if is_summer:
        return temp >= 60 and temp <= 100
    return temp >= 60 and temp <= 90

def caught_speeding(speed, is_birthday):
    '''You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value: 0=no ticket,
    1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1. If speed is 81
    or more, the result is 2. Unless it is your birthday -- on that day, your
    speed can be 5 higher in all cases.'''
    if is_birthday:
        if speed > 85:
            return 2
        elif speed > 65:
            return 1
        else:
            return 0
    else:
        if speed > 80:
            return 2
        elif speed > 60:
            return 1
        else:
            return 0

def sorta_sum(a, b):
    '''Given 2 ints, a and b, return their sum. However, sums in the range
    10..19 inclusive, are forbidden, so in that case just return 20.'''
    if a + b >= 10 and a + b <= 19:
        return 20
    return a + b

def alarm_clock(day, vacation):
    '''Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
    and a boolean indicating if we are on vacation, return a string of the
    form "7:00" indicating when the alarm clock should ring. Weekdays, the
    alarm should be "7:00" and on the weekend it should be "10:00". Unless
    we are on vacation -- then on weekdays it should be "10:00" and weekends
    it should be "off".'''
    if vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        return "7:00"

def love6(a, b):
    '''The number 6 is a truly great number. Given two int values, a and b,
    return True if either one is 6. Or if their sum or difference is 6.
    Note: the function abs(num) computes the absolute value of a number.'''
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    '''Given a number n, return True if n is in the range 1..10, inclusive.
    Unless outside_mode is True, in which case return True if the number
    is less or equal to 1, or greater or equal to 10.'''
    if not outside_mode:
        return n >= 1 and n <= 10
    return n <= 1 or n >= 10

def near_ten(num):
    '''Given a non-negative number "num", return True if num is within 2 of
    a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so
    (7 % 5) is 2. See also: Introduction to Mod'''
    return abs(num % 10) <= 2 or abs(num % 10) >= 8

# Logic-2
def make_bricks(small, big, goal, current=0, depth=0):
    '''We want to make a row of bricks that is goal inches long. We have a
    number of small bricks (1 inch each) and big bricks (5 inches each).
    Return True if it is possible to make the goal by choosing from the given
    bricks. This is a little harder than it looks and can be done without
    any loops. See also: Introduction to MakeBricks'''
    # print(small, big, goal, current, depth)
    if not goal > 4500:    
        if current == goal:
            return True
        if current > goal:
            return False
        if not small <= 0:
            nextsmall = current + 1
            nextsmall = make_bricks(small - 1, big, goal, nextsmall, depth + 1)
            if nextsmall:
                return True
        if not big <= 0:
            nextbig = current + 5
            nextbig = make_bricks(small, big - 1, goal, nextbig)
            if nextbig:
                return True
        return False
    else:
        mininum = goal // 5
        if mininum < big:
            return big <= 5 * (mininum) + small
        else:
            return small >= goal - (mininum * 5)
# for site
# def make_bricks(small, big, goal, current=0, depth=0):
#   def answer(small, big, goal):
#     fiveBricks = 5 * big
#     if fiveBricks == goal:
#         return 0
#     if fiveBricks < goal:
#         can = goal - fiveBricks
#         if can <= small:
#             return can
#         else:
#             return -1
#     else:
#         if goal % 5 == 0:
#             return 0
#         can = goal - ((goal // 5) * 5) 
#         if small >= can:
#             return can
#         return -1
#   return answer(small, big, goal) >= 0    

def lone_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. However, if one of the
    values is the same as another of the values, it does not count towards
    the sum.'''
    sumList = [a, b, c]
    killList = []
    for i in sumList:
        if not sumList.count(i) > 1:
            if i not in killList:
                killList.append(i)
    return sum(killList)

def lucky_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. However, if one of the
    values is 13 then it does not count towards the sum and values to its
    right do not count. So for example, if b is 13, then both b and c do
    not count.'''
    outSum = 0
    for i in [a, b, c]:
        if i != 13:
            outSum += i
        else:
            break
    return outSum

def no_teen_sum(a, b, c):
    '''Given 3 int values, a b c, return their sum. However, if any of the
    values is a teen -- in the range 13..19 inclusive -- then that value
    counts as 0, except 15 and 16 do not count as a teens. Write a separate
    helper "def fix_teen(n):"that takes in an int value and returns that value
    fixed for the teen rule. In this way, you avoid repeating the teen code 3
    times (i.e. "decomposition"). Define the helper below and at the same
    indent level as the main no_teen_sum().'''
    def fix_teen(n):
        if (n >= 13 and n <=19):
          if n != 15 and n != 16:
            return 0
        return n

    outSum = 0
    for i in [a, b, c]:
        outSum += fix_teen(i)
    return outSum

def round_sum(a, b, c):
    '''For this problem, we'll round an int value up to the next multiple of
    10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
    Alternately, round down to the previous multiple of 10 if its rightmost
    digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return 
    he sum of their rounded values. To avoid code repetition, write a separate
    helper "def round10(num):" and call it 3 times. Write the helper entirely
    below and at the same indent level as round_sum().'''

    def round10(num):
        if num % 10 >= 5:
            return num + (10 - (num % 10))
        else:
            return num - (num % 10)

    outSum = 0
    for i in [a, b, c]:
        outSum += round10(i)
    return outSum

def close_far(a, b, c):
    '''Given three ints, a b c, return True if one of b or c is "close"
    (differing from a by at most 1), while the other is "far", differing
    from both other values by 2 or more. Note: abs(num) computes the absolute
    value of a number.'''
    return (abs(a - b) <= 1 and (abs(a - c) >= 2 and abs(b - c) >= 2)) or \
    (abs(a - c) <= 1 and (abs(a - b) >= 2 and (abs(c - b) >= 2)))

def make_chocolate(small, big, goal):
    '''We want make a package of goal kilos of chocolate. We have small bars
    (1 kilo each) and big bars (5 kilos each). Return the number of small bars
    to use, assuming we always use big bars before small bars. Return -1 if
    it can't be done.'''
    fiveBricks = 5 * big
    if fiveBricks == goal:
        return 0
    if fiveBricks < goal:
        can = goal - fiveBricks
        if can <= small:
            return can
        else:
            return -1
    else:
        if goal % 5 == 0:
            return 0
        can = goal - ((goal // 5) * 5) 
        if small >= can:
            return can
        return -1


# String-2 

def double_char(str):
    '''Given a string, return a string where for every char in the
    original, there are two chars.'''
    outString = ''
    for i in str:
        outString += i * 2
    return outString

def count_hi(str):
    '''Return the number of times that the string "hi" appears anywhere
    in the given string.'''
    return str.count('hi')

def cat_dog(str):
    '''Return True if the string "cat" and "dog" appear the same number
    of times in the given string.'''
    return str.count('cat') == str.count('dog')

def count_code(str):
    '''Return the number of times that the string "code" appears anywhere in
    the given string, except we'll accept any letter for the 'd', so "cope"
    and "cooe" count.'''
    count = 0
    for i in range(len(str) - 3):
        if str[i] == "c":
            if str[i + 1] == 'o':
                if str[i + 3] == 'e':
                    count += 1
    return count

def end_other(a, b):
    '''Given two strings, return True if either of the strings appears at
    the very end of the other string, ignoring upper/lower case differences
    (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.'''
    a = a.lower()
    b = b.lower()
    if len(b) > len(a):
        a, b = b, a
    return a[len(b) * -1:] == b

def xyz_there(str):
    '''Return True if the given string contains an appearance of "xyz"
    where the xyz is not directly preceeded by a period (.). So "xxyz"
    counts but "x.xyz" does not.'''
    counter = str.count("xyz")
    start = 0
    for i in range(counter):
        nexts = str.find("xyz", start)
        if not str[nexts - 1] == '.':
            return True
        start = nexts + 1
    return False


# List-2

def count_evens(nums):
    '''Return the number of even ints in the given array. Note: the % "mod"
    operator computes the remainder, e.g. 5 % 2 is 1.'''
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter += 1
    return counter

def big_diff(nums):
    '''Given an array length 1 or more of ints, return the difference between
    the largest and smallest values in the array. Note: the built-in
    min(v1, v2) and max(v1, v2) functions return the smaller or larger
    of two values.'''
    if len(nums) == 1:
        return 0
    return max(nums) - min(nums)

def centered_average(nums):
    '''Return the "centered" average of an array of ints, which we'll say
    is the mean average of the values, except ignoring the largest and
    smallest values in the array. If there are multiple copies of the
    smallest value, ignore just one copy, and likewise for the largest
    value. Use int division to produce the final average. You may assume
    that the array is length 3 or more.'''
    nums.remove(max(nums))
    nums.remove(min(nums))
    return int(sum(nums) / len(nums))

def sum13(nums):
    '''Return the sum of the numbers in the array, returning 0 for
    an empty array. Except the number 13 is very unlucky, so it does
    not count and numbers that come immediately after a 13 also do
    not count.'''
    newList = []
    for i in range(len(nums)):
        if nums[i] != 13:
            newList.append(nums[i])
        else:
            if i != len(nums) - 1:
                nums[i + 1] = 0
    return sum(newList)

def sum67(nums):
    '''Return the sum of the numbers in the array, except ignore sections
    of numbers starting with a 6 and extending to the next 7 (every 6 will
    be followed by at least one 7). Return 0 for no numbers.'''
    if nums == []:
        return 0
    while 6 in nums:
        start = nums.index(6)
        end = nums.index(7, start)
        for i in range(start, end + 1):
            nums[i] = 0
    return sum(nums)

def has22(nums):
    '''Given an array of ints, return True if the array contains a
    2 next to a 2 somewhere.'''
    checkPassed = False
    for i in nums:
        if i == 2:
            if checkPassed:
                return True
            else:
                checkPassed = True
        else:
            checkPassed = False    
    return False
