from os import sep
from tkinter import END
#import time
#time.sleep(1)

single_quotes = 'Detroit '
double_quotes = "Red Wings "
triple_quotes = """are an original six hockey team. \nThey\'ve won the most stanley cups of any American NHL franchise. """
hockeytown = "Detroit is nicknamed 'Hockeytown'. "
gordie_howe = 1809
stevie_y = 1755

print("%s%s%s" % (single_quotes, double_quotes, triple_quotes))
print("%sTheir all time points leader is Gordie Howe." % (hockeytown))
print("He scored %d points in his career." % (gordie_howe))
print("Steve Yzerman was a close second with %d points all time." % (stevie_y))
print("Grand Rapids Griffins are the AHL affiliate\nToledo Walleye, the ECHL affiliate", end='')
print(" Pi is approximately %f" % (22/7))
print(hockeytown * 5)

# single and double quotes
# triple quotes for multiple lines
# backslash escape for special characters like apostrophes
# multiple embedded values using %s, %d, and %f
# multiplying strings
# removing the newline of a print statement with end=""
# adding newlines to print statements