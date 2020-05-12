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
# '(...)' = 
# '(?...)' =
# '?aiLmsux' =
# '(?:...)' =
# '(?aiLmsux-imsx:...)' =
# '(?P<name>...)' =
# '(?P=name)' =
# '(?#...)' =
# '(?=...)' =
# '(?!...)' =
# '(?<=...)' =
# '(?<!...)' =
# '(?(id/name)yes-pattern|no-pattern)' =
# '\number' =
# '\A' =
# '\b' =
# '\B' =
# '\d' =
# '\D' =
# '\s' =
# '\S' =
# '\w' =
# '\W' =
# '\Z' =
# '\u', '\U'. '\N' =

import re

