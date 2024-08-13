
# Demo print statements and a few basic principles
# When finished with demo, push it to Git

# Keyboard shortcut to Comment/Uncomment is the same as in Azure Data Studio: Ctrl + /

# A note about Debugging before we get started:
# As you progress through this class, you will find yourself having to fix problems in your code. 
# Whether the code simply won’t run or is giving you the wrong answer, fixing problems with code is a vital part of being a programmer. 
# The process of working through issues in code is called debugging. We will cover debugging in depth in a later chapter, but here is what we need to know now.

# Errors are common and even the most experienced programmers are regularly debugging their code.
# Asking for help from peers and mentors can be a key part of the process.
# Google is very much an acceptable resource when it comes to debugging.
# Asking for Help
# Before asking for help, make sure that you have the answers to some of the questions that may be asked of you and that your questions to 
# the person who is helping you are detailed. “My code doesn’t work” or “Why doesn’t my code work?” are difficult questions for someone to answer. 
# “I tried using print like the chapter outlined, but the screen says ‘Invalid Input’. What does that mean and how might I go about addressing it?” 
# is a good question to ask.

# Here are some tips on what information you might need when asking for help:

# Ask Google for help first. If you see an error message as opposed to “Hello World!”, copy it into Google and search. 
# You may find the answer right away! If you don’t find the answer or are not sure you understand it, make note of that.
# Make sure to document everything. The steps you took before you encountered the problem, screenshots of what the error message is, 
# what your application should be able to do. This is all helpful information for the person assisting you.
# When asking your question, make sure that the person knows what documentation you have. If you took a screenshot or saved Google results related 
# to the error message, inform the person who is helping you before you all start working together on the issue.


# # First, print the phrase Hello World
# print("Hello World!")


# #   1. Change the message that is printed.
# print("Hello LaunchCode DA2024!")

# #   2. Figure out what the parentheses do. Will the code work without them?
# # Won't run without parens - SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# #print "Hello"  

# #   3. Remove one or both quotation marks. 
# #   Do we need to include both opening and closing quote marks? 
# print("test quotes) #SyntaxError: unterminated string literal (detected at line 9)
# print(test quotes") #SyntaxError: unterminated string literal (detected at line 10)

# # Is there a difference between using a single or a double quote (' vs. ")?
# # # No difference, Python interprets these identically
# print ('test quotes')
# print("test quotes")


#   4. Print a number. (Bonus: Print two numbers added together).
#   5. Print multiple messages one after the other.
# print(7)
# print(7+7)

# #   6. Print two messages on the same line.

# # Using commas
# print("Hello,", "comma!", "This is on one line.")

# # Using concatenation
# print("Hello, " + "concatenation!" + " This is on one line.")

# # Using f-strings (formatted strings)
# name = "f-string"
# print(f"Hello, {name}! This is on one line.")

# # Using the end parameter
# print("Hello,", end="")
# print("end parameter!", end="")
# print(" This is all on one line.")

# # Using the end parameter with additional spacing
# print("Hello,", end=" ")
# print("end param with spaces!", end=" ")
# print(" This is all on one line.")

#   7. Print a message that contains quote marks, such as Quoth the Raven "Nevermore".
# In this case, we must handle a few different ways to avoid Python misinterpreting the quotation marks 
# that we want to display as the end of the string literal.  See the white below and the syntax error
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# print("A message that contains "Quotation Marks"")

# # Using single quotes to enclose the string/double quotes to display
# print('A message that contains "Quotation Marks"')

# # Using backslash to escape the double quotes
# print("A message that contains \"Quotation Marks\"")

# # Using triple quotes
# print("""A message that contains "Quotation Marks" """)



# # Comment Demo
# # print("This does not print.")
# print("Hello, World!  Comment Demo") # Comments do not have to start at the beginning of a line.

# # Here is how
# # to have
# # multi-line
# # comments
# print("Comments make your code more readable by others.");



# This is a line of comments I'm using as an example 
# during lecture to demo multi line commenting and its functionality


# # Additional print examples
# print('Hello, JavaScript.');
# print(2001);
# print("What","do","commas","do?");
# print("Does", "adding",      "space", "matter?");
# print('Launch' + 'Code');
# print("LaunchCode was founded in", 2013);

# New Line Example:
print("Some Programming Languages:");
print("Python\nJavaScript\nJava\nC#\nSwift");


# # AC - Note to Self:
# # Once finished with the above demo, proceed to Terminal to demo git commands to push file to GitHub repo
# # git status || This will show you all the files you changed in red.
# # git add . || This will stage/prepare all the changed files in this directory to be updated in your GitHub repo
# # git status || This is optional but will show you all your staged files in green, which are now ready to update in GH
# # git commit -m "<type a message here>" || This will ‘commit’, or finalize your changes in git. 
#     #  Between the quotes, replace the text and carrot symbols < > with a short message describing your changes. 
#     #  This will help you remember what you did while looking through many commits later.
# # git push || This will actually send teh committed changes to your GH repo

# AC - Note to Self:
# Once finished with GH demo, walk through the exact exercise as an additional overview

# Exercises: How to Write Code

# The following commands might already be familiar to you. 
# Practicing them and using the commands many times over makes them second nature. 
# Once you are comfortable with them the speed at which you can execute them and move swiftly through your 
# terminal for common tasks becomes an excellent tool at your disposal!


# 1.  Using your terminal, navigate to your Home directory using cd ~.

# 2.  Use ls to view the contents of your Home directory.

# 3.  Use cd to move into your Desktop directory. For most, the command to do this is cd Desktop/ since the Desktop is most often a child of the Home directory.

# 4.  In the terminal, use mkdir to create a folder on the Desktop called ‘my_first_directory’. Look on your Desktop. Do you see it?

# 5.  Use cd my_first_directory/ to move inside that directory.

# 6.  pwd to check your location.

# 7.  There, make a file called ‘my_first_file.txt’ with touch my_first_file.txt.

# 8.  Open the file and write yourself a message!

# 9.  Back in the terminal, list the contents of your current directory from the terminal with ls.

# 10. Make a copy of your ‘my_first_file.txt’ from it’s current spot to directly on the Desktop with cp my_first_file.txt ../my_first_copy.txt.

# 11. Move back out to your Desktop directory from the terminal with cd ...

# 12. Use ls in the terminal to verify your ‘my_first_copy.txt’ on your Desktop. Print the contents of the file to standard out with the cat command. Is it the same as your first file?

# 13. Move your copied file into your ‘my_first_directory’ with mv my_first_copy.txt my_first_directory/.

# 14. Use ls to see that the copied file is no longer on your Desktop.

# 15. Type cd my_first_directory/, followed by ls to confirm that your copy has been moved into ‘my_first_directory’.

# 16. cd .. to get back out to your Desktop.

# 17. Type rm -r my_first_directory/ and do a visual check, as well as ls on your terminal, to verify that the directory has been removed.
