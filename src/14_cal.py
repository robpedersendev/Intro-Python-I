"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def parent(args):
    script_name, *args = sys.argv
    if not args:
        rend_cal()  # This function will act as the parent function and will be the
    elif len(args) == 1:  # function that is directly called. Everything else will be a
        month = int(args[0])  # child function and receive data or do something based off of
        rend_cal(month)  # this function.
    elif len(args) == 2:
        month, year = map(int, args)  # This takes data from the CLI, passes it to args and based off
        rend_cal(month, year)  # of len(args) will do a specific function call or action.
    else:
        print("You did it wrong")


def rend_cal(month=None, year=None):
    if not month and not year:
        year, month = [datetime.now().year, datetime.now().month]
        calendar.prmonth(year, month)  # This function sets a default value for the parameters
    elif month and not year:  # passed to it from a function that will be created. Once
        year = datetime.now().year  # the values are passed to the function it will use an
        calendar.prmonth(year, month)  # if/else/elif to determine the correct values and utilize
    else:  # the calendar.prmonth method to render the calendar with the
        calendar.prmonth(year, month)  # specified values


def utilization():
    instruc = "\nNAME\n\t14_cal.py -- a simple calendar tool\n\n"
    instruc += "USAGE\n\tpython 14_cal.py [month [year]]\n\n"
    instruc += "DESCRIPTION\n\t"
    desc = """If no arguments are passed, the current month's calendar will 
        be printed. If one argument is passed, the corresponding month 
        will be printed for the current year. If two arguments are 
        passed, then the month for given month and year will be printed.\n"""
    instruc += desc
    print(instruc)
    exit(1)  # If there is an error message, then print out in depth why it exited


if __name__ == '__main__':  # Used to specify what to do when the file is ran
    parent(sys.argv)  # Pass the command line provided information into the parent Func
