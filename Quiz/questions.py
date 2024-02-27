final_score = 0
python_question = {
    "one": """
What is the correct syntax for printing "Hello, World!" in Python?

   1. echo("Hello, World!")

   2. print("Hello, World!")

   3. Console.log("Hello, World!")

   4. println("Hello, World!")
    """,
    "two": """
    In Python, which of the following is a mutable data type?

   1. Tuple

   2. String

   3. List

   4. Set
    """,
    "three": """
    What does the `if __name__ == "__main__":` block indicate in a Python script?

   1. It checks if the script is running as the main program.

   2. It defines a main function for the script.

   3. It is used to compare two names.

   4. It is a comment and has no effect on the script.
    """,
    "four": """
    How is an empty list created in Python?

   1. `emptyList = []`

   2. `emptyList = list()`

   3. `emptyList = {}`

   4. `emptyList = new List()`
    """,
    "five": """
    What is the purpose of the `self` parameter in Python class methods?

   1. It refers to the instance of the class.

   2. It represents the superclass.

   3. It is used to create a new instance of the class.

   4. It is a reserved keyword and has no specific purpose.
    """,
    "six": """
    In Python, what is the purpose of the `__init__` method in a class?

   1. It initializes the class variables.

   2. It defines the main method of the class.

   3. It initializes the object when it is created.

   4. It is a reserved keyword and has no specific purpose.
    """,
    "seven": """
    What is the difference between a shallow copy and a deep copy of a list in Python?

   1. Shallow copy copies the elements of the list, while deep copy creates a new list.

   2. Shallow copy creates a new list, while deep copy copies only the references to the elements.

   3. Shallow copy copies the references to the elements, while deep copy creates a new list.

   4. There is no difference between shallow copy and deep copy.
    """,
    "eight": """
    How is inheritance implemented in Python?

   1. Using the `extends` keyword.

   2. Using the `inherits` keyword.

   3. By defining a new class with the same methods and attributes of the base class.

   4. By using the `super` keyword.
    """,
    "nine": """
    What is the purpose of the `super()` function in Python?

   1. It calls the superclass constructor.

   2. It creates an instance of the superclass.

   3. It refers to the current instance of the class.

   4. It is a reserved keyword and has no specific purpose.
    """,
    "ten": """
     What is the purpose of the `@staticmethod` decorator in Python?

    1. It defines a static method that can be called on the class.

    2. It declares a method as private.

    3. It indicates that the method is a class constructor.

    4. It is used for method overloading.

    """,
    "eleven": """
    What is the purpose of the `try`, `except`, and `finally` blocks in Python?

    1. `try` is used for normal code, `except` is used to handle exceptions, and `finally` is executed regardless of whether an exception occurs or not.

    2. `try` is used for exception handling, `except` is used for normal code, and `finally` is executed only if an exception occurs.

    3. `try` is used for normal code, `except` is used for cleanup code, and `finally` is executed only if an exception occurs.

    4. `try` is used for normal code, `except` is used to handle exceptions, and `finally` is not necessary.
    """,
    "twelve": """
    How can you open a file in binary mode in Python?

    1. `file = open("filename.txt", "rb")`

    2. `file = open("filename.txt", "r")`

    3. `file = open("filename.txt", "wb")`

    4. `file = open("filename.txt", "br")`
    """,
    "thirteen": """
    What is the purpose of the `with` statement in Python?

    1. To create a new scope for variables.

    2. To define a context manager for resource management.

    3. To create a new instance of a class.

    4. To handle exceptions.
    """,
    "fourteen": """
    What is the output of the following code?

    ```python
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Division by zero")
    finally:
        print("Finally block")
    ```

    1. Division by zero

    2. Finally block

    3. Division by zero, Finally block

    4. No output
    """,
    "fifteen": """
    How can you read the contents of a file line by line in Python?

    1. `file.readLines()`

    2. `file.read_all_lines()`

    3. `file.readlines()`

    4. `file.read_lines()`
    """,
    "sixteen": """
    What is the purpose of the `lambda` function in Python?

    1. To create anonymous functions.

    2. To define a function with a variable number of arguments.

    3. To declare a constant variable.

    4. To access the global namespace.
    """,
    "seventeen": """
    What is the purpose of the `map` function in Python?

    1. To apply a function to each element of an iterable.

    2. To create a new iterable from an existing one.
       
    3. To filter elements in an iterable.
    
    4. To concatenate multiple iterables.
    """,
    "eighteen": """
    What is the output of the following code?

    ```python
    def func(x):
        return x + 5

    numbers = [1, 2, 3, 4]
    result = list(map(func, numbers))
    print(result)
    ```

    1. [6, 7, 8, 9]

    2. [1, 2, 3, 4]

    3. [5, 10, 15, 20]

    4. [1, 4, 9, 16]
    """,
    "nineteen": """
    What is the purpose of the `filter` function in Python?

    1. To remove elements from an iterable.

    2. To apply a function to each element of an iterable.

    3. To filter elements based on a condition.

    4. To concatenate multiple iterables.
    """,
    "twenty": """
    What is the purpose of the `decorators` in Python?

    1. To add comments to functions.

    2. To modify or extend the behavior of functions without changing their code.

    3. To declare variables.

    4. To define classes.
    """
}
python_answers = {
    "one": 2,
    "two": 3,
    "three": 1,
    "four": 1,
    "five": 1,
    "six": 3,
    "seven": 1,
    "eight": 3,
    "nine": 1,
    "ten": 1,
    "eleven": 1,
    "twelve": 1,
    "thirteen": 2,
    "fourteen": 3,
    "fifteen": 3,
    "sixteen": 1,
    "seventeen": 1,
    "eighteen": 1,
    "nineteen": 3,
    "twenty": 2
}
# -------------------------------------------------------------------------------------------------------------

# JavaScript
javascript_questions = {
    "one": """
What is the correct way to include an external JavaScript file in an HTML document?

   A. `<js src="script.js">`

   B. `<script type="text/javascript" href="script.js">`

   C. `<script src="script.js" type="text/javascript"></script>`

   D. `<javascript file="script.js">`
""",
    "two": """
 In JavaScript, which of the following is a falsy value?

   A. `null`

   B. `1`

   C. `"true"`

   D. `undefined`
""",
    "three": """
How can you convert a string to an integer in JavaScript?

   A. `parseInt("42")`

   B. `str.toInteger()`

   C. `Number("42")`

   D. `str.convertToInt()`
""",
    "four": """
What will be the output of `console.log(typeof NaN);`?

   A. "number"

   B. "string"

   C. "undefined"

   D. "NaN"
""",
    "five": """
What does the `===` operator in JavaScript compare?

   A. Values only

   B. Values and types

   C. Types only

   D. Reference in memory
""",
    "six": """
What is the purpose of the `bind` method in JavaScript?

   A. To bind a function to an event listener.

   B. To create a new function with a specified `this` value.

   C. To bind variables to a function.

   D. To attach a function to a DOM element.
""",
    "seven": """
What is a closure in JavaScript?

   A. A function that takes no arguments.

   B. A combination of a function and the lexical environment within which that function was declared.

   C. A loop that never ends.

   D. An object that encapsulates data and behavior.
""",
    "eight": """
How does the `call` method differ from the `apply` method in JavaScript?

   A. `call` is used for asynchronous functions, while `apply` is used for synchronous functions.

   B. `call` is used for functions with a variable number of arguments, while `apply` is used for functions with a fixed number of arguments.

   C. `call` is used to invoke a function with a specific `this` context and arguments provided individually, while `apply` is used to invoke a function with a specific `this` context and arguments provided as an array.

   D. There is no difference between `call` and `apply`.
""",
    "nine": """
What is the output of the following code?

   ```javascript
   var x = 10;
   function foo() {
       console.log(x);
   }
   function bar() {
       var x = 20;
       foo();
   }
   bar();
   ```

   A. 10

   B. 20

   C. undefined

   D. ReferenceError
""",
    "ten": """
What is the value of `result` in the following code?

    ```javascript
    var result = (function() {
        return typeof arguments;
    })();
    ```

    A. "object"

    B. "array"

    C. "undefined"

    D. "function"
""",
    "eleven": """
What is the purpose of the `setTimeout` function in JavaScript?

    A. To delay the execution of a function by a specified time.

    B. To set a timeout for AJAX requests.

    C. To create a timer for the entire application.

    D. To synchronize asynchronous operations.
""",
    "twelve": """
What is a Promise in JavaScript?

    A. A guarantee that a function will always return a value.

    B. A pattern for handling asynchronous operations and representing a value which might be available now, or in the future, or never.

    C. A function that returns another function.

    D. A way to declare constants in JavaScript.
""",
    "thirteen": """
How does `async/await` differ from using Promises directly?

    A. `async/await` is a newer syntax for Promises, and they are interchangeable.

    B. `async/await` provides a more concise syntax for working with Promises, making code look more synchronous.

    C. `async/await` can only be used for certain types of asynchronous operations, while Promises can handle any asynchronous operation.

    D. There is no difference between `async/await` and Promises.
""",
    "fourteen": """
What is the purpose of the `fetch` function in JavaScript?

    A. To fetch resources synchronously from the server.

    B. To fetch resources asynchronously from the server.

    C. To fetch resources from the local storage.

    D. To fetch resources from external APIs.
""",
    "fifteen": """
What is the event loop in JavaScript?

    A. A loop used for iterating over arrays.

    B. A loop that ensures JavaScript code runs in a single thread and handles asynchronous operations using the call stack and message queue.

    C. A loop that monitors the performance of the application.

    D. A loop that handles events in the DOM.
""",
    "sixteen": """
 How would you implement a deep copy of an object in JavaScript?

    A. `const newObj = Object.create(oldObj);`

    B. `const newObj = oldObj.clone();`

    C. `const newObj = { ...oldObj };`

    D. `const newObj = Object.assign({}, oldObj);
 """,
    "seventeen": """
What does the `Object.freeze` function do in JavaScript?

    A. Prevents the creation of new objects.

    B. Makes an object immutable, preventing the addition, modification, or deletion of properties.

    C. Freezes the memory space occupied by an object.

    D. Creates a shallow copy of an object.
""",
    "eighteen": """
What is the purpose of the 'use strict' directive in JavaScript?

    A. Enforces a strict mode of code execution.

    B. Declares a variable in strict mode.

    C. Initiates asynchronous operations in strict mode.

    D. It is a comment and has no effect on code execution.
""",
    "nineteen": """
How can you create a private variable in JavaScript?

    A. Use the 'private' keyword.

    B. Prefix the variable name with an underscore (_).

    C. Enclose the variable in a closure.

    D. Use the 'secret' keyword.
""",
    "twenty": """
What is memoization in JavaScript?

    A. The process of converting a function into a closure.

    B. A technique to optimize the performance of functions by caching their results.

    C. A method to manipulate data structures efficiently.

    D. The act of converting a synchronous function into an asynchronous one.
"""
}
javascript_answers = {
    "one": 3,
    "two": 1,
    "three": 1,
    "four": 1,
    "five": 2,
    "six": 2,
    "seven": 2,
    "eight": 3,
    "nine": 1,
    "ten": 1,
    "eleven": 1,
    "twelve": 2,
    "thirteen": 2,
    "fourteen": 2,
    "fifteen": 2,
    "sixteen": 3,
    "seventeen": 2,
    "eighteen": 1,
    "nineteen": 2,
    "twenty": 2
}

# --------------------------------------------------------------------------------------------------------

java_questions = {
"one": """
What is the correct syntax for declaring the main method in a Java class?

   1. `public static void Main(String[] args)`

   2. `public static void main(String[] args)`

   3. `static void Main(String[] args)`

   4. `void main(String[] args)`
""",
"two": """
Which of the following is true about the `==` operator in Java?

   1. It compares the values of two objects.

   2. It compares the memory addresses of two objects.

   3. It compares the contents of two arrays.

   4. It can be used to compare objects for equality.
""",
"three": """
What is the purpose of the `super` keyword in Java?

   1. To access the superclass methods or fields.

   2. To call a static method.

   3. To invoke the constructor of the current class.

   4. To define a superclass.
""",
"four": """
What is the difference between `ArrayList` and `LinkedList` in Java?

   1. `ArrayList` is faster than `LinkedList` for random access.

   2. `LinkedList` is more memory-efficient than `ArrayList`.

   3. `ArrayList` allows faster insertion and deletion of elements.

   4. `LinkedList` is a synchronized collection, while `ArrayList` is not.
""",
"five": """
What does the `final` keyword signify in Java?

   1. The variable can be reassigned.

   2. The method can be overridden.

   3. The class cannot be instantiated.

   4. The variable must be initialized at the time of declaration.
""",
"six": """
In Java, what is the purpose of the `interface` keyword?

   1. To define a class.

   2. To declare an abstract class.

   3. To declare an interface.

   4. To define a method.
""",
"seven": """What is method overloading in Java?

   1. Defining multiple methods with the same name in a class.

   2. Overriding a method in a subclass.

   3. Redefining a method in the same class.

   4. Declaring a method with multiple parameters.
""",
"eight": """What is the purpose of the `static` keyword in Java?

   1. To define a constant variable.

   2. To declare a variable that belongs to the class rather than an instance of the class.

   3. To make a method synchronized.

   4. To declare a method that cannot be overridden.""",
"nine": """In Java, what is the difference between composition and inheritance?

   1. Composition is a way to achieve code reusability through class hierarchy.

   2. Inheritance allows a class to inherit the properties and methods of another class.

   3. Composition is a way to create a relationship between classes by including an instance of one class inside another.

   4. Inheritance is a way to combine multiple classes into a single class.""",
"ten": """What is the purpose of the `this` keyword in Java?

    1. To refer to the current instance of the class.

    2. To access the superclass methods.

    3. To declare a static variable.

    4. To create an instance of a class.""",
"eleven": """How is the `try`, `catch`, and `finally` block used in Java exception handling?

    1. `try` is used for normal code, `catch` is used to handle exceptions, and `finally` is executed regardless of whether an exception occurs or not.

    2. `try` is used for exception handling, `catch` is used for normal code, and `finally` is executed only if an exception occurs.

    3. `try` is used for normal code, `catch` is used for cleanup code, and `finally` is executed only if an exception occurs.

    4. `try` is used for normal code, `catch` is used to handle exceptions, and `finally` is not necessary.""",
"twelve": """What is the purpose of the `Runnable` interface in Java?

    1. To define a method that can be executed asynchronously.

    2. To create a thread by extending the `Thread` class.

    3. To represent a group of threads.

    4. To implement a callback function.""",
"thirteen": """How can you prevent multiple threads from accessing a shared resource simultaneously in Java?

    1. Using the `synchronized` keyword.

    2. Using the `volatile` keyword.

    3. Using the `final` keyword.

    4. Using the `static` keyword.""",
"fourteen": """ What is the purpose of the `wait` and `notify` methods in Java?

    1. To pause and resume the execution of a thread.

    2. To signal that a thread has finished its execution.

    3. To wait for user input.

    4. To synchronize the execution of threads.""",
"fifteen": """Which of the following statements about Java's `Thread.sleep()` method is correct?

    1. It pauses the thread for a specific duration in milliseconds.

    2. It permanently stops the thread.

    3. It waits for the completion of another thread.

    4. It is used to release the lock on an object.""",
"sixteen": """What is the purpose of Java Streams?

    1. To provide input/output operations.

    2. To represent a sequence of elements and facilitate functional-style operations.

    3. To manage database connections.

    4. To create graphical user interfaces.""",
"seventeen": """What is the primary advantage of using Lambda Expressions in Java?

    1. They provide a concise syntax for creating anonymous classes.

    2. They enable parallel processing of data.

    3. They eliminate the need for the `final` keyword.

    4. They allow direct manipulation of memory.""",
"eighteen": """What is the output of the following code?

    ```java
    List<String> fruits = Arrays.asList("Apple", "Banana", "Orange");
    fruits.stream().filter(fruit -> fruit.startsWith("A")).forEach(System.out::println);
    ```

    1. Apple

    2. Banana

    3. Orange

    4. Apple, Banana, Orange""",
"nineteen": """What is a functional interface in Java?

    1. An interface that is used to define methods for functional programming.

    2. An interface that has exactly one abstract method and may contain multiple default or static methods.

    3. An interface that is used for input/output operations.

    4. An interface that has no methods.""",
"twenty": """
What is the purpose of the package statement in Java?

1. To define a new package.

2. To import classes from another package.

3. To specify the superclass of a class.

4. To declare a variable.
"""
}

java_answers = {
"one": 2,
"two": 2,
"three": 1,
"four": 1,
"five": 3,
"six": 3,
"seven": 1,
"eight": 2,
"nine": 3,
"ten": 1,
"eleven": 1,
"twelve": 1,
"thirteen": 1,
"fourteen": 1,
"fifteen": 1,
"sixteen": 2,
"seventeen": 1,
"eighteen": 1,
"nineteen": 2,
"twenty": 1
}

# -----------------------------------------------------------------------------------------------------------------------------------------
# C Language

c_questions = {
"one": """What is the correct syntax for printing "Hello, World!" in C?

   A. `echo("Hello, World!");`

   B. `print("Hello, World!");`

   C. `Console.log("Hello, World!");`

   D. `printf("Hello, World!");`""",
"two": """In C, what is the purpose of the `#include` directive?

   A. To define a new function.

   B. To include the contents of a header file.

   C. To create a new variable.

   D. To declare a constant.""",
"three": """How is an integer variable initialized to the value 5 in C?

   A. `int x; x = 5;`

   B. `int x = 5;`

   C. `x = int(5);`

   D. `int(5) = x;`""",
"four": """What does the `&` operator do in C?

   A. Represents the power operator.

   B. Returns the remainder of a division.

   C. Retrieves the address of a variable.

   D. Performs bitwise AND operation.""",
"five": """How is an array initialized in C?

   A. `int arr = {1, 2, 3};`

   B. `array<int> arr = {1, 2, 3};`

   C. `int arr[] = {1, 2, 3};`

   D. `array<int> arr[] = {1, 2, 3};`""",
"six": """ What is the purpose of the `if` statement in C?

   A. To declare a variable.

   B. To iterate over a sequence of elements.

   C. To conditionally execute a block of code.

   D. To define a function.""",
"seven": """How do you write a `for` loop that iterates from 1 to 10 in C?

   A. `for (i = 1; i <= 10; i++)`

   B. `for (i = 1; i < 10; i++)`

   C. `for (i = 10; i > 0; i--)`

   D. `for (i = 0; i < 10; i++)`""",
"eight": """What is the purpose of the `switch` statement in C?

   A. To define a case-sensitive variable.

   B. To handle multiple conditions based on the value of an expression.

   C. To create a nested loop.

   D. To perform arithmetic calculations.""",
"nine": """How can you exit a loop prematurely in C?

   A. `stop;`

   B. `exit;`

   C. `break;`

   D. `continue;`""",
"ten": """What does the `do-while` loop in C do?

    A. Repeats a block of code while a condition is true.

    B. Iterates over a range of values.

    C. Executes a block of code at least once, then repeats as long as a condition is true.

    D. Performs bitwise OR operation.""",
"eleven": """How is a function declared in C?

    A. `function myFunction() { }`

    B. `def myFunction():`

    C. `void myFunction() { }`

    D. `function void myFunction() { }`""",
"twelve": """What is the purpose of the `return` statement in a function in C?

    A. To print a value to the console.

    B. To exit the program.

    C. To return a value from the function.

    D. To define a function.""",
"thirteen": """How do you pass an array to a function in C?

    A. By using a global variable.

    B. By passing the array's size.

    C. By passing the array's elements one by one.

    D. By passing the array's address.""",
"fourteen": """What is the purpose of the `malloc()` function in C?

    A. To allocate memory for a variable.

    B. To free allocated memory.

    C. To declare a new function.

    D. To perform mathematical calculations.""",
"fifteen": """How do you declare a pointer variable in C?

    A. `int* ptr;`

    B. `ptr int;`

    C. `pointer int;`

    D. `int ptr();`
""",
"sixteen": """How can you open a file named "example.txt" for writing in C?

    A. `fopen("example.txt", "r");`

    B. `open("example.txt", "w");`

    C. `fopen("example.txt", "w");`

    D. `file_open("example.txt", "w");`""",
"seventeen": """What is the purpose of the `struct` keyword in C?

    A. To define a new function.

    B. To declare a constant.

    C. To create a structure to hold multiple variables.

    D. To perform string manipulation.""",
"eighteen": """How do you access a member of a structure in C?

    A. `struct.member;`

    B. `struct->member;`

    C. `struct::member;`

    D. `struct[member];`
""",
"nineteen": """What does the `fwrite()` function do in C?

    A. Reads from a file.

    B. Writes to a file.

    C. Frees allocated memory.

    D. Closes a file.""",
"twenty": """
How can you define an array of structures in C?

    A. `array<struct> myArray;`

    B. `struct array myArray[];`

    C. `struct myArray[];`

    D. `struct myArray[10];`
"""
}

c_answers = {
"one": 4,
"two": 2,
"three": 2,
"four": 3,
"five": 3,
"six": 3,
"seven": 1,
"eight": 2,
"nine": 3,
"ten": 3,
"eleven": 3,
"twelve": 3,
"thirteen": 4,
"fourteen": 1,
"fifteen": 1,
"sixteen": 3,
"seventeen": 3,
"eighteen": 2,
"nineteen": 2,
"twenty": 4
}

# -----------------------------------------------------------------------------------------------------------------------------

# cplusplus

cplusplus_questions = {
"one": """What is the correct syntax for printing "Hello, World!" in C++?

   A. `echo("Hello, World!");`

   B. `print("Hello, World!");`

   C. `Console.log("Hello, World!");`

   D. `cout << "Hello, World!";`""",
"two": """In C++, which of the following is a valid way to initialize an integer variable?

   A. `int x;`

   B. `integer x;`

   C. `x = int;`

   D. `x = 5;`""",
"three": """What is the purpose of the `#include` directive in C++?

   A. To define a new class.

   B. To include the declaration of a function.

   C. To include the contents of a header file.

   D. To import a library.""",
"four": """How is an array initialized in C++?

   A. `int array = {1, 2, 3};`

   B. `array<int> arr = {1, 2, 3};`

   C. `int array[] = {1, 2, 3};`

   D. `array<int> arr[] = {1, 2, 3};`""",
"five": """What does the `new` keyword do in C++?

   A. Creates a new object.

   B. Allocates memory for a dynamic variable.

   C. Initializes a new class.

   D. Declares a new function.
""",
"six": """In C++, what is the purpose of the `class` keyword?

   A. To create an instance of a class.

   B. To declare a variable.

   C. To define a new class.

   D. To initialize a class.""",
"seven": """What is method overloading in C++?

   A. Defining multiple methods with the same name but different return types.

   B. Overriding a method in a subclass.

   C. Redefining a method in the same class.

   D. Defining multiple methods with the same name but different parameters.""",
"eight": """What is the purpose of the `this` pointer in C++?

   A. To refer to the current instance of the class.

   B. To access the superclass methods.

   C. To create an instance of a class.

   D. To declare a static variable.""",
"nine": """In C++, what is the difference between a constructor and a destructor?

   A. A constructor is called when an object is created, while a destructor is called when an object is destroyed.

   B. A constructor is called when an object is destroyed, while a destructor is called when an object is created.

   C. A constructor is used to initialize variables, while a destructor is used to declare variables.

   D. There is no difference between a constructor and a destructor.""",
"ten": """What is encapsulation in C++?

    A. A process of creating a copy of an object.

    B. A process of wrapping data and the methods that operate on the data into a single unit.

    C. A process of defining multiple methods with the same name.

    D. A process of converting a class to an interface.""",
"eleven": """What is the purpose of the `try`, `catch`, and `finally` blocks in C++?

    A. `try` is used for normal code, `catch` is used to handle exceptions, and `finally` is executed regardless of whether an exception occurs or not.

    B. `try` is used for exception handling, `catch` is used for normal code, and `finally` is executed only if an exception occurs.

    C. `try` is used for normal code, `catch` is used for cleanup code, and `finally` is executed only if an exception occurs.

    D. `try` is used for normal code, `catch` is used to handle exceptions, and `finally` is not necessary.""",
"twelve": """How can you open a file for writing in C++?

    A. `file = open("filename.txt", "r");`

    B. `file = fopen("filename.txt", "w");`

    C. `file = open("filename.txt", "wb");`

    D. `file = fopen("filename.txt", "a");`""",
"thirteen": """What is the purpose of the `ifstream` class in C++?

    A. To write data to a file.

    B. To open a file for input.

    C. To close a file.

    D. To create a new file.""",
"fourteen": """What is the output of the following code?

    ```cpp
    try {
        throw 10;
    }
    catch (int x) {
        cout << "Caught " << x;
    }
    ```

    A. Caught 10

    B. 10

    C. Exception thrown

    D. No output
""",
"fifteen": """How can you write a string to a file in C++?

    A. `file.write("Hello, World!", 13);`

    B. `file << "Hello, World!";`

    C. `file.print("Hello, World!");`

    D. `file.append("Hello, World!");`""",
"sixteen": """What is the purpose of the `auto` keyword in C++?

    A. To define a variable with a fixed type.

    B. To declare a variable that cannot be modified.

    C. To automatically deduce the type of a variable at compile time.

    D. To create an anonymous function.""",
"seventeen": """What is the purpose of the `vector` container in C++?

    A. To represent a dynamic array.

    B. To store key-value pairs.

    C. To represent a linked list.

    D. To store elements in a sorted order.
""",
"eighteen": """What is the output of the following code?

    ```cpp
    int x = 5;
    int& y = x;
    y++;
    cout << x;
    ```

    A. 5

    B. 6

    C. Compilation error

    D. Runtime error
""",
"nineteen": """What is the purpose of the `virtual` keyword in C++?

    A. To declare a variable that can be modified.

    B. To define a method that cannot be overridden.

    C. To enable polymorphism by allowing a derived class to override a base class method.

    D. To declare a variable with a fixed type.""",
"twenty": """What is the purpose of the `nullptr` keyword in C++?

    A. To

 define a null pointer.

    B. To declare a variable with a null value.

    C. To represent an undefined value.

    D. To indicate a variable with a value of zero."""
}

cplusplus_answers = {
"one": 4,
"two": 1,
"three": 3,
"four": 3,
"five": 2,
"six": 3,
"seven": 4,
"eight": 1,
"nine": 1,
"ten": 2,
"eleven": 1,
"twelve": 2,
"thirteen": 2,
"fourteen": 1,
"fifteen": 2,
"sixteen": 3,
"seventeen": 1,
"eighteen": 2,
"nineteen": 3,
"twenty": 1
}

# ---------------------------------------------------------------------------------------------------------------------------

# Kotlin

kotlin_questions = {
"one": """How do you print "Hello, World!" in Kotlin?

A. System.out.println("Hello, World!")

B. print("Hello, World!")

C. echo("Hello, World!")

D. Console.log("Hello, World!")""",
"two": """In Kotlin, what is the correct way to declare a variable named x with the type Int?

A. val x: Int;

B. let x = 5

C. var x: Int

D. x = 5""",
"three": """What is the purpose of the val keyword in Kotlin?

A. To declare a variable that can be modified.

B. To create a constant.

C. To specify a nullable variable.

D. To define a function.""",
"four": """How do you create an array in Kotlin?

A. val array = [1, 2, 3]

B. val array = Array(3, {i -> i + 1})

C. val array: Array<Int> = [1, 2, 3]

D. val array = array![1, 2, 3]""",
"five": """What does the when keyword do in Kotlin?

A. Defines a loop.

B. Checks a value against a series of patterns.

C. Creates a switch statement.

D. Represents the power operator.""",
"six": """What is the purpose of the ? operator in Kotlin?

A. To define a nullable variable.

B. To perform mathematical calculations.

C. To declare a constant.

D. To create a loop.""",
"seven": """How do you define an extension function in Kotlin?

A. fun String.capitalize() { ... }

B. String.capitalize() { ... }

C. extension fun String.capitalize() { ... }

D. fun capitalize(String) { ... }""",
"eight": """What is the safe call operator in Kotlin?

A. ?.

B. !!

C. ::

D. ?:""",
"nine": """How do you handle null values with the Elvis operator in Kotlin?

A. val result = value ?: defaultValue

B. val result = value ?: throw Exception("Value is null")

C. val result = if (value != null) value else defaultValue

D. val result = value ? defaultValue : value""",
"ten": """What is the purpose of the let function in Kotlin?

A. To define a lambda expression.

B. To perform an operation on a non-null object.

C. To create an extension function.

D. To define a constant.""",
"eleven": """How do you filter a list in Kotlin using a lambda expression?

A. list.filter { it > 5 }

B. list.filter(it > 5)

C. list.filter { item -> item > 5 }

D. filter(list, { it > 5 })""",
"twelve": """What is the purpose of the map function in Kotlin?

A. To create a new list with transformed elements.

B. To iterate over the elements of a list.

C. To perform a conditional operation.

D. To remove elements from a list.""",
"thirteen": """How do you create a mutable list in Kotlin?

A. val list = listOf(1, 2, 3)

B. val list = mutableListOf(1, 2, 3)

C. val list: MutableList<Int> = [1, 2, 3]

D. val list = array![1, 2, 3""",
"fourteen": """What is the purpose of the groupBy function in Kotlin?

A. To group elements in a list based on a predicate.

B. To create a new list with grouped elements.

C. To perform a mathematical operation.

D. To filter elements in a list.""",
"fifteen": """How do you use the reduce function in Kotlin?

A. list.reduce { acc, element -> acc + element }

B. reduce(list, { acc, element -> acc + element })

C. list.map { acc, element -> acc + element }

D. reduce(list, acc + element)""",
"sixteen": """What is the primary constructor in Kotlin?

A. The constructor defined inside a class.

B. The constructor with the init block.

C. The constructor with parameters defined after the class name.

D. The default constructor provided by Kotlin.""",
"seventeen": """How do you create an instance of a class in Kotlin?

A. val obj = MyClass.create()

B. val obj = new MyClass()

C. val obj = MyClass()

D. val obj = create(MyClass)""",
"eighteen": """What is the purpose of the data keyword in Kotlin?

A. To declare a variable that can be modified.

B. To define a constant.

C. To create a data class.

D. To perform file I/O operations.""",
"nineteen": """How do you define a class with a secondary constructor in Kotlin?

A. class MyClass { constructor() }

B. class MyClass { secondary constructor() }

C. class MyClass constructor() { }

D. class MyClass { constructor() {} }""",
"twenty": """What is the difference between a data class and a regular class in Kotlin?

A. A data class cannot have methods.

B. A data class automatically generates equals, hashCode, and toString methods.

C. A regular class cannot have properties.

D. A regular class is immutable by default."""
}

kotlin_answers = {
"one": 1,
"two": 1,
"three": 2,
"four": 2,
"five": 2,
"six": 1,
"seven": 1,
"eight": 1,
"nine": 1,
"ten": 2,
"eleven": 1,
"twelve": 1,
"thirteen": 2,
"fourteen": 1,
"fifteen": 1,
"sixteen": 3,
"seventeen": 3,
"eighteen": 3,
"nineteen": 4,
"twenty": 2
}

# --------------------------------------------------------------------------------------------------------------------------
# Rust

rust_questions = {
"one": """How do you print "Hello, World!" in Rust?

A. echo!("Hello, World!");

B. print!("Hello, World!");

C. Console.log("Hello, World!");

D. println!("Hello, World!");""",
"two": """In Rust, what is the correct way to declare a variable named x with the type i32?

A. let x: i32;

B. let x = 5;

C. let x i32;

D. x = 5;""",
"three": """What is the purpose of the mut keyword in Rust?

A. To declare a constant.

B. To specify a mutable variable.

C. To include external modules.

D. To create a structure.""",
"four": """How do you create a vector in Rust?

A. let vec = [1, 2, 3];

B. let vec = Vec::new();

C. let vec: Vec<i32> = Vec::new();

D. let vec = vector![1, 2, 3];
""",
"five": """What does the match keyword do in Rust?

A. Defines a macro.

B. Checks a value against a series of patterns.

C. Creates a loop.

D. Represents the power operator.""",
"six": """What is the purpose of the ownership system in Rust?

A. To track memory leaks.

B. To ensure thread safety.

C. To manage ownership and lifetimes of memory.

D. To prevent stack overflow.""",
"seven": """How do you borrow a reference to a variable in Rust?

A. let ref x = &variable;

B. let x = &variable;

C. let x = borrow(variable);

D. let x = variable.borrow();""",
"eight": """What is the difference between String and &str in Rust?

A. String is mutable, and &str is immutable.

B. String is for static strings, and &str is for dynamic strings.

C. There is no difference; they are interchangeable.

D. String is a reference type, and &str is a value type.""",
"nine": """How do you return a value from a function in Rust?

A. return value;

B. value;

C. -> value;

D. -> Result<T, E> { value }""",
"ten": """What is the purpose of the Option type in Rust?

A. To represent nullable values.

B. To perform pattern matching.

C. To define constants.

D. To create generic types.""",
"eleven": """How do you use the Result type for error handling in Rust?

A. let result = Result::Ok(value);

B. let result = Result::Err("Error message");

C. let result: Result<i32, &str> = Ok(value);

D. let result: Result = Ok(value);""",
"twelve": """What is an enum in Rust?

A. A keyword for defining functions.

B. A collection of variables.

C. A type that represents a value from a finite set of possibilities.

D. An error handling mechanism.""",
"thirteen": """How do you match on an enum variant in Rust?

A. match enum { Variant => ... }

B. enum.match { Variant => ... }

C. match enum { Enum::Variant => ... }

D. match Variant { ... }""",
"fourteen": """What is the purpose of the Option::unwrap method in Rust?

A. To unwrap an Option and get its value.

B. To check if an Option is empty.

C. To create an Option instance.

D. To perform pattern matching on an Option.""",
"fifteen": """How do you define a custom error type in Rust?

A. enum CustomError { ... }

B. struct CustomError { ... }

C. error CustomError { ... }

D. trait CustomError { ... }""",
"sixteen": """What is a lifetime in Rust?

A. The duration for which a variable is valid.

B. A keyword for defining thread lifetimes.

C. The duration for which a program runs.

D. A keyword for defining loop lifetimes.""",
"seventeen": """How do you spawn a new thread in Rust?

A. thread::spawn(my_function);

B. spawn_thread(my_function);

C. spawn(my_function);

D. my_function.spawn();""",
"eighteen": """What is the purpose of the Arc type in Rust?

A. To perform atomic reference counting.

B. To create mutable references.

C. To handle errors.

D. To define constant values.""",
"nineteen": """How do you define a trait in Rust?

A. trait MyTrait { ... }

B. struct MyTrait { ... }

C. interface MyTrait { ... }

D. type MyTrait = { ... }""",
"twenty": """What does the async keyword indicate in Rust?

A. A type that represents asynchronous operations.

B. A keyword for defining async functions.

C. An error handling mechanism.

D. A lifetime specifier."""
}

rust_answers = {
"one": 4,
"two": 1,
"three": 2,
"four": 3,
"five": 2,
"six": 3,
"seven": 2,
"eight": 1,
"nine": 3,
"ten": 1,
"eleven": 3,
"twelve": 3,
"thirteen": 3,
"fourteen": 1,
"fifteen": 2,
"sixteen": 1,
"seventeen": 1,
"eighteen": 1,
"nineteen": 1,
"twenty": 2
}

# ----------------------------------------------------------------------------------------------------------------------------

# go

go_questions = {
"one": """What is the correct way to print "Hello, World!" in Go?

   A. `echo("Hello, World!")`

   B. `fmt.print("Hello, World!")`

   C. `print("Hello, World!")`

   D. `fmt.Println("Hello, World!")`""",
"two": """In Go, how do you declare a variable named `x` with the type `int`?

   A. `x int`

   B. `var x int`

   C. `let x int`

   D. `x = 5`""",
"three": """What is the purpose of the `package` keyword in Go?

   A. To define a new function.

   B. To declare a variable.

   C. To specify the package to which a file belongs.

   D. To include external modules.""",
"four": """ How do you initialize a slice in Go?

   A. `slice = [1, 2, 3]`

   B. `slice := []int{1, 2, 3}`

   C. `slice = make([]int, 3)`

   D. `slice = (1, 2, 3)`""",
"five": """What does the `defer` keyword do in Go?

   A. Delays the execution of a function until the surrounding function returns.

   B. Closes a file.

   C. Defers the declaration of a variable.

   D. Represents the power operator.""",
"six": """In Go, what is the purpose of the `if` statement?

   A. To declare a variable.

   B. To conditionally execute a block of code.

   C. To create a loop.

   D. To define a function.
""",
"seven": """How do you write a `for` loop that iterates from 1 to 10 in Go?

   A. `for i := 1; i <= 10; i++`

   B. `for i := 1; i < 10; i++`

   C. `for i := 10; i > 0; i--`

   D. `for i := 0; i < 10; i++`""",
"eight": """What is the purpose of the `switch` statement in Go?

   A. To handle multiple conditions based on the value of an expression.

   B. To define a case-sensitive variable.

   C. To create a nested loop.

   D. To perform arithmetic calculations.""",
"nine": """ How can you exit a loop prematurely in Go?

   A. `stop`

   B. `exit`

   C. `break`

   D. `continue`""",
"ten": """What does the `range` keyword do in a `for` loop in Go?

    A. Generates a range of numbers.

    B. Iterates over the elements of an array, slice, string, or map.

    C. Defines the range of values for a loop.

    D. Represents the power operator.""",
"eleven": """How is a function declared in Go?

    A. `function myFunction() { }`

    B. `def myFunction():`

    C. `func myFunction() { }`

    D. `function void myFunction() { }`""",
"twelve": """What is the purpose of the `return` statement in a function in Go?

    A. To print a value to the console.

    B. To exit the program.

    C. To return a value from the function.

    D. To define a function.
""",
"thirteen": """How do you pass a slice to a function in Go?

    A. By using a global variable.

    B. By passing the slice's length.

    C. By passing the slice's elements one by one.

    D. By passing the slice's reference.""",
"fourteen": """What is the purpose of the `new` keyword in Go?

    A. To allocate memory for a variable.

    B. To free allocated memory.

    C. To declare a new function.

    D. To perform mathematical calculations.""",
"fifteen": """How do you declare a pointer variable in Go?

    A. `var ptr *int;`

    B. `ptr int;`

    C. `pointer int;`

    D. `int* ptr;`""",
"sixteen": """What is goroutine in Go?

    A. A variable with a fixed type.

    B. A function that runs concurrently with other functions.

    C. A type of loop.

    D. A built-in package for file handling.""",
"seventeen": """How can you create a channel in Go?

    A. `channel := make(chan int)`

    B. `newChannel := createChannel(int)`

    C. `channel := new(int)`

    D. `newChannel := makeChannel()`""",
"eighteen": """What is the purpose of the `select` statement in Go?

    A. To select a case in a switch statement.

    B. To perform a non-blocking receive on multiple channels.

    C. To check if a variable is defined.

    D. To declare a new function.""",
"nineteen": """How do you close a channel in Go?

    A. `close(myChannel)`

    B. `myChannel.close()`

    C. `myChannel = nil`

    D. `closeChannel(myChannel)`""",
"twenty": """What is the purpose of the `sync` package in Go?

    A. To create synchronization barriers.

    B. To declare variables with synchronized access.

    C. To perform mathematical calculations.

    D. To handle file I/O operations."""
}

go_answers = {
"one": 4,
"two": 2,
"three": 3,
"four": 2,
"five": 1,
"six": 2,
"seven": 1,
"eight": 1,
"nine": 3,
"ten": 2,
"eleven": 3,
"twelve": 3,
"thirteen": 4,
"fourteen": 1,
"fifteen": 1,
"sixteen": 1,
"seventeen": 1,
"eighteen": 2,
"nineteen": 1,
"twenty": 1
}

# ----------------------------------------------------------------------------------------------------------------------------

# swift

swift_questions = {
"one": """How do you print "Hello, World!" in Swift?

A. print("Hello, World!")

B. System.out.println("Hello, World!")

C. Console.log("Hello, World!")

D. echo("Hello, World!")
""",
"two": """In Swift, what is the correct way to declare a variable named x with the type Int?

A. let x: Int;

B. var x: Int;

C. let x = 5;

D. x: Int = 5;""",
"three": """What is the purpose of the let keyword in Swift?

A. To declare a variable that can be modified.

B. To create a constant.

C. To specify a nullable variable.

D. To define a function.""",
"four": """How do you create an array in Swift?

A. let array = [1, 2, 3]

B. let array = Array(1...3)

C. let array: [Int] = [1, 2, 3]

D. let array = array![1, 2, 3]""",
"five": """What does the if let syntax do in Swift?

A. Performs a conditional check.

B. Unwraps an optional and executes the block if the value is not nil.

C. Creates a loop.

D. Represents the power operator.""",
"six": """What is an optional in Swift?

A. A type that represents multiple values.

B. A variable that can be modified.

C. A type that represents values that may be absent.

D. A type that requires explicit casting.""",
"seven": """How do you unwrap an optional using forced unwrapping in Swift?

A. let unwrappedValue = optionalValue!

B. let unwrappedValue = unwrap(optionalValue)

C. let unwrappedValue = optionalValue.unwrap()

D. let unwrappedValue = optionalValue?""",
"eight": """What is the purpose of the guard statement in Swift?

A. To perform a conditional check.

B. To create a loop.

C. To unwrap an optional.

D. To define a constant.""",
"nine": """
How do you use optional chaining in Swift?

A. let result = object.method()

B. let result = object?.method()

C. let result = object!.method()

D. let result = object::method()""",
"ten": """
What does the nil coalescing operator (??) do in Swift?

A. Performs a bitwise XOR operation.

B. Unwraps an optional and provides a default value if it's nil.

C. Checks if a variable is nil.

D. Creates a loop.""",
"eleven": """
How do you define a function in Swift?

A. function myFunction() { }

B. def myFunction():

C. func myFunction() { }

D. function void myFunction() { }""",
"twelve": """
What is the purpose of the return keyword in a function in Swift?

A. To print a value to the console.

B. To exit the program.

C. To return a value from the function.

D. To define a function.""",
"thirteen": """
How do you declare a closure in Swift?

A. let closure = { (parameters) -> returnType in ... }

B. closure { (parameters) -> returnType in ... }

C. func closure(parameters) -> returnType { ... }

D. let closure: (parameters) -> returnType = { ... }""",
"fourteen": """
What is the purpose of the inout keyword in Swift?

A. To define a constant.

B. To specify a nullable variable.

C. To create an inout parameter that can be modified.

D. To perform file I/O operations.""",
"fifteen": """
How do you capture values in a closure in Swift?

A. capture { value in ... }

B. let capture = { value in ... }

C. capture(value) { ... }

D. let capture { value in ... }""",
"sixteen": """
What is a protocol in Swift?

A. A keyword for defining classes.

B. A collection of variables.

C. A type that defines a blueprint of methods and properties.

D. An error handling mechanism.""",
"seventeen": """
How do you create an instance of a class in Swift?

A. let obj = MyClass.create()

B. let obj = new MyClass()

C. let obj = MyClass()

D. let obj = create(MyClass)""",
"eighteen": """
What is the purpose of the super keyword in Swift?

A. It refers to the superclass.

B. It creates an instance of the superclass.

C. It defines a method that can be called on the class, not on instances.

D. It performs type casting.
""",
"nineteen": """
How do you define a computed property in Swift?

A. var myProperty: Int { get { return value } }

B. computed var myProperty: Int { return value }

C. let myProperty: Int { get { return value } }

D. var myProperty { return value }""",
"twenty": """
What is the purpose of the final keyword in Swift?

A. To declare a variable that cannot be modified.

B. To prevent a class, method, or property from being overridden.

C. To define a constant.

D. To indicate the end of a program."""
}

swift_answers = {
"one": 1,
"two": 2,
"three": 2,
"four": 3,
"five": 2,
"six": 3,
"seven": 1,
"eight": 3,
"nine": 2,
"ten": 2,
"eleven": 3,
"twelve": 3,
"thirteen": 1,
"fourteen": 3,
"fifteen": 2,
"sixteen": 3,
"seventeen": 3,
"eighteen": 1,
"nineteen": 1,
"twenty": 2
}

# ------------------------------------------------------------------------------------------------------------------------

# Typescript

typescript_questions = {
"one": """What is the correct syntax for declaring a variable of type string in TypeScript?

   A. `let x: string;`

   B. `const x = "Hello";`

   C. `var x: string = "World";`

   D. `string x;`""",
"two": """In TypeScript, what is the purpose of the `interface` keyword?

   A. To define a class.

   B. To declare a variable.

   C. To create a type for objects.

   D. To import external modules.""",
"three": """How is an arrow function defined in TypeScript?

   A. `function add(x, y) => x + y;`

   B. `const add = (x, y) => { return x + y; }`

   C. `const add: (x: number, y: number) => number = function(x, y) { return x + y; };`

   D. `function add(x, y) { return x + y; }`""",
"four": """What is the purpose of the `readonly` modifier in TypeScript?

   A. It makes a variable immutable.

   B. It restricts access to a variable.

   C. It specifies a required property in an interface.

   D. It is used for defining generic types.""",
"five": """How can you explicitly specify the type of a variable in TypeScript?

   A. `let x = 5;`

   B. `let x: any = 5;`

   C. `let x: number; x = 5;`

   D. `let x = "Hello";`""",
"six": """What does the `keyof` keyword do in TypeScript?

   A. Retrieves the type of an object.

   B. Iterates over the keys of an object.

   C. Checks if a key exists in an object.

   D. Returns a union type of an object's keys.""",
"seven": """How do you define a generic function in TypeScript?

   A. `function example<T>(arg: T): T { return arg; }`

   B. `function example(arg): any { return arg; }`

   C. `function example<T>: T { return T; }`

   D. `function example(arg): T { return arg; }`""",
"eight": """What is the purpose of the `as` keyword in TypeScript?

   A. To import external modules.

   B. To cast one type to another.

   C. To declare a variable.

   D. To create an alias for a type.""",
"nine": """How can you create an intersection type in TypeScript?

   A. `type Intersection = A & B;`

   B. `type Intersection = A | B;`

   C. `type Intersection = A + B;`

   D. `type Intersection = A * B;`""",
"ten": """What is the difference between the `unknown` and `any` types in TypeScript?

    A. There is no difference; they can be used interchangeably.

    B. `unknown` is more restrictive than `any` and requires type checking before usage.

    C. `any` is more restrictive than `unknown` and requires type checking before usage.

    D. `unknown` is a subtype of `any`.""",
"eleven": """How is inheritance implemented in TypeScript?

    A. Using the `extends` keyword.

    B. Using the `implements` keyword.

    C. By defining a new class with the same methods and attributes of the base class.

    D. By using the `super` keyword.""",
"twelve": """What is the purpose of the `super()` keyword in TypeScript?

    A. It calls the superclass constructor.

    B. It creates an instance of the superclass.

    C. It refers to the current instance of the class.

    D. It is used for method overloading.""",
"thirteen": """How can you make a method in a class optional in TypeScript?

    A. By using the `?` operator.

    B. By declaring the method with an empty body.

    C. By using the `optional` keyword.

    D. It's not possible; all methods in a class are mandatory.""",
"fourteen": """What is the purpose of the `static` keyword in TypeScript?

    A. It declares a variable that can be modified.

    B. It defines a method that can be called on the class, not on instances.

    C. It enables polymorphism.

    D. It refers to the current instance of the class.""",
"fifteen": """What is a generic class in TypeScript?

    A. A class that can be used without specifying a type.

    B. A class with methods that accept generic arguments.

    C. A class that can be extended by other classes.

    D. A class that is defined using the `generic` keyword.""",
"sixteen": """How can you export a function or variable from a module in TypeScript?

    A. `export function myFunction() { }`

    B. `export myFunction = function() { }`

    C. `module.exports = myFunction;`

    D. `myFunction.export();`
""",
"seventeen": """What is the purpose of the `import` statement in TypeScript?

    A. To include the contents of a module.

    B. To declare a new variable.

    C. To create a namespace.

    D. To define a type alias.""",
"eighteen": """How do you create a default export in TypeScript?

    A. `export default myFunction;`

    B. `export myFunction as default;`

    C. `default export myFunction;`

    D. `export default = myFunction;`""",
"nineteen": """What is the difference between a namespace and a module in TypeScript?

    A. There is no difference; they can be used interchangeably.

    B. A namespace is used for internal organization, while a module is for external dependencies.

    C. A module is used for internal organization, while a namespace is for external dependencies.

    D. A module is a collection of types, while a namespace is a collection of variables.""",
"twenty": """How can you use the `/// <reference path="..." />` directive in TypeScript?

    A. To import external modules.

    B. To reference another TypeScript file.

    C. To declare a variable.

    D. To create a type alias."""
}

typescript_answers = {
"one": 1,
"two": 3,
"three": 2,
"four": 1,
"five": 3,
"six": 4,
"seven": 1,
"eight": 2,
"nine": 1,
"ten": 2,
"eleven": 1,
"twelve": 1,
"thirteen": 1,
"fourteen": 2,
"fifteen": 2,
"sixteen": 1,
"seventeen": 1,
"eighteen": 1,
"nineteen": 2,
"twenty": 2
}

# ----------------------------------------------------------------------------------------------------------------------------------

