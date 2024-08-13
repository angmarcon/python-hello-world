
# # # Definitions
# # # Value - is a specific piece of data, such as a word or a number. Some examples are 5, 5.2, and "Hello, World!".
# # # Each value is a specific data type

# # # Basic Data types

# # ## Numeric
# # # int
# # x = 10
# # print(type(x))
# # print("int:", x)

# # # float
# # y = 3.14
# # print(type(y))
# # print("float:", y)

# # # complex
# # z = 3 + 4j
# # print(type(z))
# # print("complex:", z)

# # # Don't use commas in numeric values, or else it will treat the numbers like a pair of values
# # print(42000)
# # print(42,000) # Prints as 42 0 instead of 42000

# # # boolean
# # is_active = True
# # print("bool:", is_active)

# # # str
# # s = "Hello, World!"
# # print("str:", s)

# # # if numbers are in quotation marks, they are strings
# # print(type("17"))
# # print(type("3.2"))

# # # Strings in Python can be enclosed in either single quotes (') or double quotes (").

# # # None (like Null)
# # n = None
# # print("NoneType:", n)


# # Data type conversion
# # Implicit type conversion is when Python converts a variable to a different type without any extra effort from us as programmers. 
# # For example, if you add a variable of type int and a variable of type float together, the resulting sum is a float. 
# # With implicit type conversion, Python will always convert to a larger data type so no data is lost.
# # If you try to add an integer and a string together, you may notice that Python cannot convert the result to a data type. 
# # While implicit type conversion is a handy trick, it doesn’t work in every scenario!


# # Explicit type conversion uses functions such as int(), str(), and float() to convert variables of one type to another.
# print(int("2345"))
# print(type(int("2345")))
# print(17)
# print(type(17))

# print(str(17))
# print(str(123.45))
# print(type(str(123.45)))

# # Variables
# # One of the most powerful features of a programming language is the ability to manipulate variables. 
# # A variable is a name that refers to a value. Recall that a value is a single, specific piece of data, 
# # such as a specific number or string. Variables allow us to store values for later use.

# # Assignment statements create new variables and also give them values to refer to. 
# # The syntax for an assignment statement is below.
# # The assignment statement links a name, on the left hand side of the =, 
# # with the value on the right hand side. The value refers to any type of data but I wrapped it in quotations
# # to make it a string in this example (so that the code doesn't error upon running)
# variable_name = "value"

# # Three variables are being assigned values below
# # Note that The = sign does NOT work both ways. 17 = num causes an error. The variable name MUST be on the left, and the value MUST be on the right.
# message = "Python ROCKS!" # The variable named message is being assigned a string value
# print(message)
# print(type(message))
# num = 17 # The variable named num is being assigned an int
# print(num)
# print(type(num))
# pi = 3.14159 #The variable named pi is being assigned a float
# print(pi)
# print(type(pi))

# # Evaluating Variables
# # Once we create a variable and assign it a value, we can use the variable name to refer to that value.
# print("Hello, World!")
# message = "Hello, World!"
# print(message)
# # In the second example just above, the variable name message points to the value "Hello, World". 
# # print(message) means the same thing as print("Hello, World!"), so we say that message evaluates to "Hello, World!"
# message = "Python ROCKS!"
# num = 17
# pi = 3.14159

# print(message)
# print(num)
# print(pi)
# # In each case, the printed result is the value of the variable.

# # Like values, variables also have types. We determine the type of a variable the same way we determine the type of a value, using type().
# message = "What's up, Doc?"
# n = 17
# pi = 3.14159

# print(type(message))
# print(type(n))
# print(type(pi))


# # Reassigning Variables
# # We use variables in a program to store values, like the current score at a football game. 
# # Just like a score, variables can change over time.

# # To see this, read and then run the following program. 
# # Notice how we change the value of day three times. We even give it a value of a different data type.
# # Each time that our program below reassigns the value to the day variable, the old value is overwritten

# day = "Thursday"
# print(day)

# day = "Friday"
# print(day)

# day = 21
# print(day)

# # Naming variables
# # Python provides a broad set of rules for naming variables, but there is no reason to go beyond a few easy-to-remember guidelines:

# # Use only the characters 0-9, a-z, A-Z, and underscore. In other words, do not use special characters or whitespace (space, tab, and so on).
# # Do not start a variable name with a number.
# # Do not use keywords, which are words reserved by Python for use by the language itself. We’ll discuss these in detail in a moment.
# # Following these guidelines will prevent you from creating illegal variable names. While this is important, we should also strive to create good variable names
# # Use descriptive, meaningful names (e.g., total_cost).
# # Follow snake_case convention (e.g., user_name).
# # Avoid reserved keywords (e.g., don't use class).
# # Be consistent with naming styles.
# # Avoid single-letter names, except in simple loops.
# # Start with a letter or underscore (e.g., value1, _counter).
# # Use plural names for collections (e.g., users, items_list).
# # Avoid confusing names (e.g., l, O).
# # Keep names concise but meaningful.
# # Remember Python is case-sensitive.


# # Don't use keywords or reserved words!
# # Python has a set of keywords (also known as reserved words) that have special meanings and are part of the language's syntax. 
# # These keywords cannot be used as variable names, function names, or any other identifiers. Here’s a list of Python keywords:
# # False
# # None
# # True
# # and
# # as
# # assert
# # async
# # await
# # break
# # class
# # continue
# # def
# # del
# # elif
# # else
# # except
# # finally
# # for
# # from
# # global
# # if
# # import
# # in
# # is
# # lambda
# # nonlocal
# # not
# # or
# # pass
# # raise
# # return
# # try
# # while
# # with
# # yield
# # These keywords are essential to the structure of Python code, and they perform specific functions, 
# # such as controlling the flow of a program, defining classes and functions, and managing exceptions.


# # Expressions & Evaluation
# # An expression is a combination of values, variables, operators, and calls to functions. 
# # An expression can be thought of as a formula that is made up of multiple pieces.
# # The evaluation of an expression produces a value, known as the return value. We say that an expression returns a value.
# # Expressions need to be evaluated when the code executes in order to determine the return value, or specific piece of data that should be used. 
# # Evaluation is the process of computing the return value.
# # If you ask Python to print an expression using print(), the interpreter evaluates the expression and displays the result.

# # The expression is 1+1 and print() is the function
# print(1 + 1)

# # Here, we are assigning the return value of the expression to the variable named sum
# # Next, we are printing the return value that is assigned to the variable sum
# sum = 1 + 2
# print(sum)



# # Operators and Operands
# # Now that we can store data in variables, let’s explore how we can generate new data from existing data.

# # An operator is one or more characters that represents a computation like addition, multiplication, or division. 
# # The values an operator works on are called operands.

# # The following are all legal Python expressions whose meaning is more or less clear:
# # 20 + 32
# # hour - 1
# # hour * 60 + minute
# # minute / 60
# # 5 ** 2
# # (5 + 9) * (15 - 7)
# # For example, in the calculation 20 + 32, the operator is + and the operands are 20 and 32.

# # The symbols + and -, and the use of parentheses for grouping, mean in Python what they mean in mathematics. 
# # The asterisk (*) is the symbol for multiplication, and ** is the symbol for exponentiation. 
# # Addition, subtraction, multiplication, and exponentiation all do what you expect.

# print(2 + 3) # Addition
# print(2 - 3) #Subtraction
# print(2 * 3) #Multiplication
# print(2 ** 3) #Exponentiation - 2 raised to the power of 3
# print(3 ** 2) #Exponentiation - 3 raised to the power of 2

# # We use the same terminology as before, stating that 2 + 3 returns the value 5.

# # When a variable name appears in the place of an operand, it is replaced with the value that it 
# # refers to before the operation is performed. For example, suppose that we wanted to convert 645 minutes 
# # into hours. Division is denoted by the operator /.
# minutes = 645
# hours = minutes / 60
# print(hours)

# # Operator	            Description	                                                                                Example
# # Addition (+)	        Adds the two operands	                                                                    2 + 3 returns 5
# # Subtraction (-)	    Subtracts the two operands	                                                                2 - 3 returns -1
# # Multiplication (*)	Multiplies the two operands	                                                                2 * 3 returns 6
# # Division (/)	        Divides the first operand by the second	                                                    6 / 2 returns 3
# # Modulus (%)	        Aka the remainder operator. Returns the integer remainder of dividing the two operands.	    7 % 5 returns 2
# # Exponentiation (**)	Calculates the base(first operand)to the exponent(second operand)power	                    3 ** 2 returns 9 5 ** -1 returns 0.2
# # Floor Division (//)	Returns the integral or whole number version of the quotient.	                            7 // 2 returns 3 5 // -10 returns -1

# # While the modulus operator (%) is common in programming, it is not used much outside of programming. Let’s explore how it works with a few examples.
# # The % operator returns the remainder obtained by carrying out integer division of the first operand by the second operand. 
# # Therefore, 5 % 3 is 2 because 3 goes into 5 one whole time, with a remainder of 2 left over.
# # 12 % 4 is 0, because 4 divides 12 evenly (that is, there is no remainder)
# # 13 % 7 is 6
# # 6 % 2 is 0
# # 7 % 2 is 1
# # The last two examples illustrate a general rule: An integer x is even exactly when x % 2% is %0% and is odd exactly when %x % 2% is %1%.


# # Order of operations is the same as in mathematics
# # The acronym PEMDAS can be used to remember order of operations:
# # P = parentheses
# # E = exponentiation
# # M = multiplication
# # D = division
# # A = addition
# # S = subtraction

# # Due to an historical quirk, an exception to the left-to-right rule is the exponentiation operator **. 
# # A useful hint is to always use parentheses to force exactly the order you want when exponentiation is involved:

# # the right-most ** operator is applied first
# print(2 ** 3 ** 2)

# # use parentheses to force the order you want
# print((2 ** 3) ** 2)

# # The string operator concatenates strings but it is the plus sign when used on numbers
# print(1 + 1)
# print("1" + "1")

# # Compound Assignment Operators
# # A common programming task is to update the value of a variable in reference to itself.
# x = 1
# x = x + 1
# print(x)
# # Line 2 may seem odd to you at first, since it uses the value of the variable x to update x itself. 
# # This technique is not only legal in Python (and programming in general) but is quite common. 
# # It essentially says, “update x to be one more than its current value.”

# # This action is so common, in fact, that it has a shorthand operator, +=. 
# # The following example has the same behavior as the one above.
# x = 1
# x += 1
# print(x)
# # The expression x += 1 is shorthand for x = x + 1.

# # Compound Assignment Operators
# # Operator name	                    Shorthand	Meaning
# # Addition assignment	            a += b	    a = a + b
# # Subtraction assignment	        a -= b	    a = a - b
# # Multiplication assignment	        a *= b	    a = a * b
# # Division assignment	            a /= b	    a = a / b


# Input with the Input() function
# print() works fine for printing static (unchanging) messages to the screen. 
# If we wanted to print a phrase greeting a specific user, then print("Hello, Dave.") would be OK as long as Dave is the actual user.

# What if we want to greet someone else? We could change the string inside the () to be 'Hello, Sarah' or 
# 'Hello, Elastigirl' or any other name we need. However, this is inefficient. Also, what if we do not know the name of the user beforehand? 
# We need to make our code more general and able to respond to different conditions.

# It would be great if we could ask the user to enter a name, store that string in a variable, and then print a personalized 
# greeting using print(). Variables to the rescue!

# Requesting Data
# To personalize the greeting, we have to get input from the user. This involves displaying a prompt on the screen 
# (e.g. “Please enter a number: “), and then waiting for the user to respond. Whatever information the user enters gets stored for later use.
# As we saw earlier, each programming language has its own way of accomplishing the same task. The Python syntax is input("Please enter your name: ").
# If we want to get user input to print a customized greeting, we can do the following:

user = input("Please enter your name: ")
print("Hello " + user + "!")

# Critical Input Detail
# There is one very important quirk about the input function that we need to remember. Given print(7 + 2), the output would be 9.
# Now explore the following code located in the data-analysis-projects/data-and-variables directory, which prompts the user for two numbers and then prints their sum.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print(num1 + num2)

# Run the program, enter your choice of numbers, and examine the output. Do you see what you expected?
# If we enter 7 and 2, we expect an output of 9. We do NOT expect 72, but that is the result printed. What gives?
# The quirk with the input function is that it treats all entries as strings, so numbers get concatenated rather than added. 
# Just like “Hello, " + “World” outputs as Hello, World, “7” + “2” outputs as 72.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Convert the input strings to integers
num1 = int(num1)
num2 = int(num2)

# Add the integers and print the result
print(num1 + num2)