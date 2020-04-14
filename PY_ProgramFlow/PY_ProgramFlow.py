
"""
1.1.1 Basic Programming & Variables	    https://youtu.be/3phV29yvWO8
1.1.2 Functions                 	    https://youtu.be/SytwpgZ5k6U
1.1.3 Logic & Conditional Expressions	https://youtu.be/CyjsNEFjLVk
1.1.4 Iteration                     	https://youtu.be/MIjqvWgfdq8
"""
# coding: utf-8

# In[17]:


# get_ipython().run_line_magic('logstop', '')
# get_ipython().run_line_magic('logstart', '-rtq ~/.logs/PY_ProgramFlow.py append')
# get_ipython().run_line_magic('matplotlib', 'inline')
# import matplotlib
# import seaborn as sns
# sns.set()
# matplotlib.rcParams['figure.dpi'] = 144


# In[3]:


# import expectexception


# # Program Flow
# <!-- requirement: images/high_score_flowchart.png -->
# <!-- requirement: images/nested_logic_flowchart.png -->

# ## What is a computer program?
# 
# At its simplest, a program is a list of instructions that a computer carries out in order. A program could be long and complicated, but it is built of simple parts. Let's look at some simple operations in Python, and think about what the computer does for each one:

# In[4]:


1 + 1


# In[5]:


2 * 3.5


# In[6]:


1 + 1
2 * 3.5


# In the first cell we compute `1 + 1`, and Python returns the result `2`. We can think of this as a very short program. Similarly, in the second cell we compute `2 * 3.5`, and Python returns the result `7.0`.
# 
# However, in the third cell, when we combine these two statements as sequential lines, we only see Python return `7.0`. Why is that?
# 
# Python can only return one result at the end of the cell, so the first line is evaluated, but we never see the result. One way we can report intermediate results is using `print`.

# In[7]:


print(1 + 1)
print(2 * 3.5)


# We can also include lines in the code that the computer won't execute. We call these lines **comments**, because they are used to add notes and explanations to the code. We use `#` to indicate that we are making a comment.

# In[8]:


print('1 + 1 is', 1 + 1)
# this is a comment, Python won't try to execute it
print('All done!')


# Often we won't want to only print intermediate results, but _store_ them for later use. We can store a result in the computer's memory by assigning it to a **variable**.

# In[9]:


first_result = 1 + 1
final_result = first_result * 3.5

print(final_result)


# Here we were able to use the result of the first calculation (stored in the variable `first_result`) in our second calculation. We store the second result in `final_result`, which we can print at the end of the cell.
# 
# Variables help us keep track of the information we need to successfully execute a program. Variables can be used to store a variety of types of information.

# In[10]:


my_name = 'Dylan'
my_age = 28
my_favorite_number = 2.718
has_dog = True

print('My name is', my_name)
print('My age is', my_age)
print('My favorite number is', my_favorite_number)
print('I own a dog:', has_dog)


# Since variables can be used to store so many types of information, it's a good idea to give those variables descriptive names like I did. This helps us write code that is easy to read, which helps when we're trying to find and fix mistakes, or share code with others.

# In[11]:


print(type(my_name))
print(type(my_age))
print(type(my_favorite_number))
print(type(has_dog))


# A **string** is a sequence of characters. An **integer** has the same meaning as in mathematics (i.e. "whole numbers"). A **float** or **floating point number** refers to a decimal number (i.e. "real number" in mathematics); it is called a float because the decimal point is allowed to "float" through the digits, allowing us to represent both big numbers (e.g. 204939.12) and small numbers (e.g. 0.000239). A **bool** or **boolean** refers to a variable that is either true or false.
# 
# These are just a few types of data we will encounter, and we will explore others later on in the course.
# 
# In Python, we can assign any type of data to a variable without declaring what type the variable will be in advance. Not all programming languages behave this way.

# ### Exercises
# 
# 1. Define `my_name` and `my_age` variables with values corresponding to your own name and age and print them.
# 1. Use your `my_age` variable to print out how old you will be in 10 years.

# In[15]:


my_name = 'Joatam'
my_age = 31
print(my_name)
print(my_age)
decade = my_age + 10
print("In 10 years, I will be {} years old.".format(my_age + 10))


# ## Functions
# 
# Many programs react to user input. Functions allow us to define a task we would like the computer to carry out based on input. A simple function in Python might look like this:

# In[19]:


def square(number):
    return number**2


# We define functions using the `def` keyword. Next comes the name of the function, which in this case is `square`. We then enclose the function's input in parentheses, in this case `number`. We use `:` to tell Python we're ready to write the body of the function.
# 
# In this case the body of the function is very simple; we return the square of `number` (we use `**` for exponents in Python). The keyword `return` signals that the function will generate some output. Not every function will have a `return` statement, but many will. A `return` statement ends a function.
# 
# Let's see our function in action:

# In[20]:


# we can store function output in variables
squared = square(5.5)

print(squared)

my_number = 6
# we can also use variables as function input
print(square(my_number))


# We can pass different input to the `square` function, including variables. When we passed a float to `square`, it returned a float. When we passed an integer, `square` returned an integer. In both cases the input was interpreted by the function as the argument `number`.
# 
# Not all possible inputs are valid.

# In[21]:


# get_ipython().run_cell_magic('expect_exception', 'TypeError', "\nprint(square('banana'))")


# We ran into an error because `'banana'` is a string, not a number. We should be careful to make sure that the input for a function makes sense for that function's purpose. We'll talk more about errors like this one later on.
# 
# ### Exercises
# 
# 1. Write a function to cube a number.
# 2. Write a function, `say_hello` which takes in a name variable and print out "Hello name".  `say_hello("zach")` should print `"Hello zach"`.

# In[35]:


def cube(number):
    return number**3

assert cube(3) == 27

def say_hello(name):
    print("Hello {}".format(name))

say_hello('Joatam')


# ### Why Functions?
# We can see that functions are useful for handling user input, but they also come in handy in numerous other cases.  One example is when we want to perform an action multiple times on different input.  If I want to square a bunch of numbers, in particular the numbers between 1 and 10, I can do this pretty easily (later we will learn about iteration which will make this even easier!)

# In[36]:


1**2
2**2
3**2
4**2
5**2
6**2
7**2
8**2
9**2


# It seems I forgot to save the answers or at least print them.  This is easy:

# In[37]:


print(1**2)
print(2**2)
print(3**2)
print(4**2)
print(5**2)
print(6**2)
print(7**2)
print(8**2)
print(9**2)


# That worked!  However, what if I now want to go back and add two to all the answers?  Clearly changing each instance is not the right way to do it.  Lets instead define a function to do the work for us.

# In[38]:


def do_it(x):
    print(x**2 + 2)


# Now we can just call the function on every element.  If we want to change the output, we just need to change the function in one place, not in all places we want to use the function!

# In[39]:


do_it(1)
do_it(2)
do_it(3)
do_it(4)
do_it(5)
do_it(6)
do_it(7)
do_it(8)
do_it(9)


# Splitting out the work into functions is often a way to make code more modular and understandable.  It also helps ensure your code is correct.  If we write a function and test it to be correct, we know it will be correct every time we use it.  If we don't break out code into a function, it is very easy to make typos or other errors which will cause our programs to break.  
# 
# ### Exercises
# 
# 1. Modify the `do_it` function to print the square of the value it currently prints.

# In[46]:


def do_it(x):
    print((x**2 + 2)**2)
    
do_it(1)


# ## Syntax
# 
# As our instructions to the computer become more complicated, we will need to organize them in a way the computer understands. We've already seen an example of this with our `square` function. There was a specific order to the words and specific symbols we had to use to let Python know which part of the function was the definition and which part was the body, or which part was the name of the function and which part was the argument. We call the rules for organizing code the programming language's **syntax**.
# 
# Python's syntax is very streamlined so that code is readable and intuitive. Python accomplishes this by using whitespace to organize code. Let's look at some examples.

# In[47]:


def example_a():
    print('example_a is running')
    print('returning value "a"')
    return 'a'

example_a()


# In[48]:


def example_b():
    print('example_b is running')
    print('exiting without returning a value')

example_b()


# The function `example_a` ends with a return statement, but `example_b` has no return statement. How does Python know where `example_b` ends? We use indentation to indicate which lines are part of the function and which aren't. The indented lines are all grouped together under the function definition. We'll see this format again for controlling whether certain sections of code execute.

# ## Conditionals and logic
# 
# We'll often want the computer only to take an action under certain circumstances. For example, we might want a game to print the message 'High score!', but only if the player's score is higher than the previous high score. We can write this as a formal logical statement: *if* the player's score is higher than the previous high score _then_ print 'High score!'.
# 
# The syntax for expressing this logic in Python is very similar. Let's define a function that accepts the player's score and the previous high score as arguments. If the player's score is higher, then it will print 'High score!'. Finally, it will return the new high score (whichever one that is).

# In[49]:


def test_high_score(player_score, high_score):
    if player_score > high_score:
        print('High score!')
        high_score = player_score

    return high_score


# In[50]:


print(test_high_score(83, 98))


# In[51]:


print(test_high_score(95, 93))


# With `if` statements we use a similar syntax as we used for organizing functions. With functions we had a `def` statement ending with `:`, and an indented body. Similarly for a conditional, we have an `if` statement ending with `:`, and an indented body.
# 
# Conditional statements are used to control program flow. We can visualize our example, `test_high_score`, in a decision tree.
# 
# ![simple_logic_flowchart](images/high_score_flowchart.png)
# 
# We can nest `if` statements to make more complicated trees.

# In[52]:


def nested_example(x):
    if x < 50:
        if x % 2 == 0:
            return 'branch a'
        else:
            return 'branch b'
    else:
        return 'branch c'

print(nested_example(42))
print(nested_example(51))
print(nested_example(37))


# In this example, we have an `if` statement nested under another `if` statement. As we change the input, we end up on different branches of the tree.
# 
# ![nested_logic_flowchart](images/nested_logic_flowchart.png)
# 
# The statement that follows the `if` is called the **condition**. The condition can be either true or false. If the condition is true, then we execute the statements under the `if`. If the condition is false, then we execute the statements under the `else` (or if there is no `else`, then we do nothing).
# 
# Conditions themselves are instructions that Python can interpret.

# In[53]:


print(50 > 10)
print(2 + 2 == 4)
print(-3 > 2)


# Conditions are evaluated as booleans, which are `True` or `False`. We can combine conditions by asking of condition A _and_ condition B are true. We could also ask if condition A *or* condition B are true. Let's consider whether such statements are true overall based on the possible values of condition A and condition B.
# 
# |Condition A|Condition B|Condition A and Condition B|Condition A or Condition B|
# |:---------:|:---------:|:-------------------------:|:------------------------:|
# |True|True|True|True|
# |True|False|False|True|
# |False|True|False|True|
# |False|False|False|False|

# In[54]:


print(True and True)
print(True and False)
print(False and True)
print(False and False)


# In[55]:


print(True or True)
print(True or False)
print(False or True)
print(False or False)


# In[56]:


x = 5
y = 3

print(x > 4 and y > 2)
print(x > 7 and y > 2)
print(x > 7 or y > 2)


# The keywords `or` and `and` are called **logical operations** (in the same sense that we call `+`, `-`, `*`, etc. arithmetic operations). The last logical operation is `not`: `not True` is `False`, `not False` is `True`.

# In[57]:


print(not True)
print(not False)


# In[58]:


x = 10
y = 8

print(x > 7 or y < 7)
print(not x > 7 or y < 7)
print(not x > 7 or not y < 7)
print(not (x > 7 or y < 7))


# ### Exercises
# 
# 1. Write a function which takes in a number and returns True if it is greater than 10 but less than 20 or it is less than -100.
# 2. In the code above we have used the `%` operator.  What does this do?

# In[82]:


def compare(number):
    if (number > 10 and number < 20) or number < -100:
        return True
    return False


# In[83]:


compare(-101)


# In[71]:


# Function to calculate the remainder of a division
def remainder(dividen, divisor):
    # the '%' operator gets the remainder of a division
    return dividen % divisor


# In[77]:


assert remainder(4, 2) == 0
assert remainder(5, 2) == 1


# ## Iteration
# 
# Conditionals are very useful because they allow our programs to make decisions based on some information. These decisions control the flow of the program (i.e. which statements get executed). We have one other major tool for controlling  program flow, which is repetition. In programming, we will use repetitive loops to execute the same code many times. This is called **iteration**. The most basic kind of iteration is the `while` loop. A `while` loop will keep executing so long as the condition after the `while` is `True`.

# In[78]:


x = 0
while x < 5:
    print(x)
    x = x + 1


# We will often use iteration to perform a task a certain number of times, but we might also use it to carry out a process to a certain stage of completion.
# 
# As an example of these different cases, we'll consider the Fibonacci sequence. The Fibonacci sequence is a sequence of numbers where the next number in the sequence is given by the sum of the previous two numbers. The first two numbers are given as 0 and 1. So the sequence begins 0, 1, 1, 2, 3, 5, 8...
# 
# The Fibonacci sequence goes on infinitely, so we can only ever compute part of it. Below we define two functions to compute part of the Fibonacci sequence; the first function computes the first `n` terms, while the second function computes all the terms less than an upper limit, `x`.

# In[79]:


def first_n_fibonacci(n):
    prev_num = 0
    curr_num = 1
    count = 2

    print(prev_num)
    print(curr_num)

    while count <= n:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1

def below_x_fibonacci(x):
    prev_num = 0
    curr_num = 1

    if curr_num < x:
        print(prev_num)
        print(curr_num)
    elif prev_num < x:
        print(prev_num)
    
    while curr_num + prev_num < x:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num


# In[80]:


m = 7
print('First %d Fibonacci numbers' % m)
first_n_fibonacci(m)


# In[81]:


print()

y = 40
print('Fibonacci numbers below %d' % y)
below_x_fibonacci(y)        


# Sometimes we will want our program to take a repeated action, but we won't know how many repetitions we will have to do, or it might be difficult to know ahead of time when the program should stop. For example, we could write a program that prints out cooking instructions. We don't know in advance how many instructions there will be in the recipe (some meals take a long time to cook and have many steps, while others are short and simple to make). We also don't know what the last instruction might be, so it would be difficult to write a conditional telling the program when to stop. How are we going to solve the problem? Let's look at an example.
# 
# Instructions for making bread:  
# 1) Dissolve salt in water  
# 2) Mix yeast into water  
# 3) Mix water with flour to form dough  
# 4) Knead dough  
# 5) Let dough rise  
# 6) Shape dough  
# 7) Bake  
# 
# The recipe has an ordered `list` of instructions. In Python we can use a list of strings to represent the instructions.

# In[84]:


bread_recipe = ['Dissolve salt in water', 'Mix yeast into water', 'Mix water with flour to form dough', 
                'Knead dough', 'Let dough rise', 'Shape dough', 'Bake']


# We will discuss lists more in the [Data Structures lecture](PY_DataStructures.ipynb). We could store different recipes in different lists.

# In[85]:


soup_recipe = ['Dissolve salt in water', 'Boil  water', 'Add bones to boiling water', 'Chop onions', 
               'Chop garlic', 'Chop carrot', 'Chop celery', 'Remove bones from water', 
               'Add vegetables to boiling water', 'Add meat to boiling water']

beans_recipe = ['Soak beans in water', 'Dissolve salt in water', 'Heat water and beans to boil', 
                'Drain beans when done cooking']


# Each of these lists has different instructions, and they are not all the same length. The beans recipe has four steps while the soup recipe has ten. It would be hard to write a `while` loop to print out each step. It is much easier to do it using a `for` loop.
# 
# A `for` loop does an action for each item in a `list` (or more precisely, in an **iterable**).

# In[86]:


def print_recipe(instructions):
    for step in instructions:
        print(step)


# In[87]:


print_recipe(soup_recipe)


# In[88]:


print_recipe(bread_recipe)


# In[89]:


print_recipe(beans_recipe)


# We can also use a `for` loop to repeat a task a certain number of times, like printing out the first `n` numbers in the Fibonacci sequence. Compare these two Fibonacci functions:

# In[90]:


def first_n_fibonacci_while(n):
    prev_num = 0
    curr_num = 1
    count = 2

    print(prev_num)
    print(curr_num)

    while count <= n:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1

def first_n_fibonacci_for(n):
    prev_num = 0
    curr_num = 1

    print(prev_num)
    print(curr_num)

    for count in range(2, n + 1):
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num


# In[91]:


first_n_fibonacci_while(7)


# In[92]:


first_n_fibonacci_for(7)


# ### Exercises
# 
# 1. Compare `first_n_fibonacci_while` and `first_n_fibonacci_for`, which one is "better"?

# It depends of its usage.
# `while` loop would be better for undifined times to loop.
# `For` loop is better for fixed iteration times.
# For example:
# I'll use `while` when I want to execute instructions untill a comparison checks.
# In the other hand, I'll use `For` to iterate a list of objects.

# ### Aside (Recursion)
# 
# Another way to get something like iteration is called _recursion_ which is when we define a function in terms of itself.  Lets write the Fibonacci sequence recursively.  This will be slightly different in that it will only calculate the nth Fibonacci number.

# In[93]:


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1)  + fibonacci_recursive(n-2)


# In[94]:


fibonacci_recursive(7)


# Here we make use of the fact that a Fibonacci number $F_n$ can be defined in terms of $F_{N-1}$ and $F_{N-2}$ with some base cases $F_0=0$ and $F_1=1$.  We will not be using recursion in this course, but it is an interesting and useful programming construct.

# ## Putting it all together
# 
# We've learned two of the major components of programs: **variables** and **functions**. We've also learned two of the major components of program control: **conditionals** (`if` statements) and **iteration** (`for` and `while` loops). We can use these ideas and tools to write code to perform complex tasks. Let's look at an example, involving all of these ideas put together.
# 
# Below we write a function that prints out all the prime numbers up to some number `n`. We will use iteration to check if each number is prime. We will use a conditional to print out numbers only if they are prime. We will also break up the task into small pieces so our code is easy to read and understand. This means we will use (or _call_) helper functions inside of our solution.

# In[95]:


def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def print_primes(n):
    for number in range(1, n):
        if is_prime(number):
            print('%d is prime' % number)


# In[96]:


print_primes(42)


# The other application of functions might be to do something many times (not necessarily in an iteration).  One specific and natural way to understand this is to have a list elements and apply a function to each element of the `list`.  Lets take a list of the first 20 numbers and find which ones are prime.  We will do this and save the result in a `list`. Lists have an `append` method which allows us to add to the end of the list (we will see more about lists in the next lecture).

# In[97]:


list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
prime_list = []
for number in list_of_numbers:
    if is_prime(number):
        prime_list.append(number)
prime_list


# Python provides a nice construct to apply a function to every element of a list, called a `list comprehension`, here is an example of one:

# In[98]:


[number for number in list_of_numbers if is_prime(number)]


# Note that this is a simple bit of code that is very understandable.  We don't need to care **how** the `is_prime` computation is occurring, only that its occurring for every element of `list_of_numbers`.  This means that we can more view our program at a high level without caring about the small details (which hopefully we have already designed well and tested).

# ## More About Functions
# 
# Notice that the `example_a` and `example_b` had no input, but other functions like `test_high_score` had multiple variables as input.  Remember that a function argument is just a placeholder for a name and will be bound to whatever is passed into the function.  For example:

# In[99]:


def print_this(a):
    print('inside print_this: ', a)

a = 5
print_this(2)
print('a = ', a)


# Notice that even though `print_this` was printing the variable `a` inside the function and there was a variable `a` defined outside of the function, the `print` function inside `print_this` still printed what was passed in.  However, I can also 

# In[100]:


def print_it():
    print('inside print_it: ', a)
    
a = 5
print_it()
print('a = ', a)


# Here there is no variable passed into the function so Python uses the variable from the outer scope.  Be careful with this second paradigm as it can be dangerous. The danger lies in the fact that the output of the function depends upon the overall state of the program (namely the value of `a`) as opposed to `print_this` which depends only on the input of the function.  Functions like `print_this` are much easier to reason about, test, and use, they should be preferred in many contexts.
# 
# That said, there is a very powerful technique called `function closure` which we can make use of this ability.  Lets say we want a function which will raise a number to some exponent, but we don't know which exponent ahead of runtime.  We can define such a function like this.

# In[101]:


def some_exponent(exponent):
    def func(x):
        return x**exponent
    return func


# In[102]:


some_exponent(2)(2), some_exponent(3)(2)


# Now that we understand how normal arguments work, lets look at a few conveniences Python provides for making functions easier to create.  The first is default arguments.  Let's suppose we have a function which had a bunch of arguments, but most of them had sane defaults, for example:

# In[ ]:


def print_todo(watch_tv, read, eat, sleep):
    print('I need to:')
    if watch_tv:
        print('  watch_tv')
    if read:
        print('  read')
    if eat:
        print('  eat')
    if sleep:
        print('  sleep')
print_todo(True, True, True, True)


# I know that I almost always need to eat and sleep, so I can use a default argument for these instead.  This means I don't need to define the value of `eat` and `sleep` unless they are different than the default.

# In[ ]:


def print_todo_default(watch_tv, read, eat=True, sleep=True):
    print('I need to:')
    if watch_tv:
        print('  watch_tv')
    if read:
        print('  read')
    if eat:
        print('  eat')
    if sleep:
        print('  sleep')
print_todo_default(True, True)


# These default arguments can allow us to create complex function with many inputs while also maintaining ease of use by setting sane defaults. 
# 
# Another thing we might want to do is take a variable list of arguments, lets write a similar `to do` function as before, but this time we will allow it to pass in any number of arguments.  Here we will make use of the `*args` syntax.  This `*` tells python to gather the rest of the arguments into the tuple `args`.

# In[ ]:


def print_todo_args(*args):
    print('I need to:')
    for arg in args:
        print('  ' + arg)
print_todo_args('watch_tv', 'read', 'eat', 'sleep')


# This sort of syntax can be very useful in large programs where abstract functions may all a variety of different functions with different arguments.

# ### Some topics we haven't discussed, but have used:
# - [String formatting](https://pyformat.info/)
# - Exceptions (e.g. `TypeError`)

# *Copyright &copy; 2020 The Data Incubator.  All rights reserved.*
