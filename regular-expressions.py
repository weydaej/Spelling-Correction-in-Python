# documentation: https://docs.python.org/3/library/re.html

# '.' = matches any char except for new line. (DOTALL flag will match any char incl. new line)
# '^' = matches the start of the string, and in MULTILINE mode also matches immediately after each new line
# '$' = matches the end of a string of just before the new line at the end of the string
# '*' = causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as possible 
# '+' = causes the resulting RE to match 1 or more repetitions of the preceding RE, as many repetitions as possible
# '?' = causes the resulting RE to match 0 or 1 repetitions of the preceding RE
# '*?', '+?', '??' = match as much text as possible (greedy)
# '{m}' = specifies that EXACTLY m copies of the previous RE should be matched 
# '{m,n}?' = causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible
# '\' = either escapes special characters or signals a special sequence 
# '[]' = used to indicate a set of characters
#        sets can be listed individually. [abc] will match 'a', 'b' or 'c'
#        ranges can be indicated by separating them with a '-'. [a-z], [0-9]
#        special characters lose their special meaning  
# '|' = A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B
# '(...)' = matches the regex inside the parenthesis, and indicates the start and end of a group
# '(?...)' = the first character after the '?' determines what the meaning and further syntax of the construct is 
# '?aiLmsux' = the group matches the empty string; the letters set the corresponding flags: re.A (ASCII-only matching), re.I (ignore case), re.L (locale dependent), re.M (multi-line), re.S (dot matches all), re.U (Unicode matching), and re.X (verbose), for the entire regular expression
# '(?:...)' = a non-capturing version of regular parenthesis -- matches the regex inside the parenthesis but hte substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern
# '(?P=name)' = backreference to a named group. matches the text that was matched by the earlier group named name
# '(?#...)' = a comment
# '(?=...)' = matches if '...' matches next, but does not consume any of the string (lookahead assertion)
# '(?!...)' = matches if '...' doesn't match next (negative lookahead assertion)
# '(?<=...)' = matches if the current position in the string is preceded by a match for '...' that ends at the current position (positive lookbehind assertion)
# '(?<!...)' = matches if the current position in the string is not preceded by a match for '...' (negative lookbehind assertion)
# '(?(id/name)yes-pattern|no-pattern)' = 
# '\number' = will try to match with yes-pattern if the group with given id or name exists, and with no-pattern if it doesn’t. no-pattern is optional
# '\A' = matches only at the start of the string
# '\b' = matches the empty string, but only at the beginning or end of a word -- word = a sequence of word chars
# '\B' = matches the empty string, but only whe it is not at the beginning or end of a word
# '\d' = matches any decimal digit
# '\D' = matches any char which is not a decimal digit
# '\s' = matches whitespace chars
# '\S' = matches any char which is not a whitespace char
# '\w' = matches word chars
# '\W' = matches any char which is not a word char
# '\Z' = matches only at the end of the string

import re

# 16/12/2016

regex = r"^\d{1,2}\/\d{1,2}\/\d{4}$"
print(re.findall(regex, "16/12/2016"))
print(re.findall(regex, "31/1/1996"))
