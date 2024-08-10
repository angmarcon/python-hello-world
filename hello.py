
# Welcome, new coder.
# Enter your code on line 7 to print 'Hello, World!'
# to the console (the panel on the right)


print("Hello World!");

# Next, PLAY!

#   1. Change the message that is printed.
print("Hello LaunchCode DA2024!")

#   2. Figure out what the parentheses do. Will the code work without them?
# Won't run without parens - SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#print "Hello"  

#   3. Remove one or both quotation marks. 
#   Do we need to include both opening and closing quote marks? 
#print("test quotes) #SyntaxError: unterminated string literal (detected at line 9)
#print(test quotes") #SyntaxError: unterminated string literal (detected at line 10)

# Is there a difference between using a single or a double quote (' vs. ")?
# No difference, Python interprets these identically
print ('test quotes')
print("test quotes")


#   4. Print a number. (Bonus: Print two numbers added together).
#   5. Print multiple messages one after the other.
print(7)
print(7+7)

#   6. Print two messages on the same line.

# Using commas
print("Hello,", "comma!", "This is on one line.")

# Using concatenation
print("Hello, " + "concatenation!" + " This is on one line.")

# Using f-strings (formatted strings)
name = "f-string"
print(f"Hello, {name}! This is on one line.")

# Using the end parameter
print("Hello,", end="")
print("end parameter!", end="")
print(" This is all on one line.")

# Using the end parameter with additional spacing
print("Hello,", end=" ")
print("end param with spaces!", end=" ")
print(" This is all on one line.")

#   7. Print a message that contains quote marks, such as Quoth the Raven "Nevermore".
# In this case, we must handle a few different ways to avoid Python misinterpreting the quotation marks 
# that we want to display as the end of the string literal.  See the white below and the syntax error
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# print("A message that contains "Quotation Marks"")

# Using single quotes to enclose the string/double quotes to display
print('A message that contains "Quotation Marks"')

# Using backslash to escape the double quotes
print("A message that contains \"Quotation Marks\"")

# Using triple quotes
print("""A message that contains "Quotation Marks" """)


















#   8. Other. You choose!
#
