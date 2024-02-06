number = 10
assert number < 5, f"The number should not exceed 5. ({number=})"
print(number)

#However, you shouldn’t rely on assertions for catching crucial run conditions of your program in production. 
#That’s because Python globally disables assertions when you run it in optimized mode using the -O and -OO command line options:
"""
Note: Picking the right exception type can sometimes be tricky. Python comes with many built-in exceptions that are hierarchically related, so if you browse the documentation, you’re likely to find a fitting one.

Python even groups some of the exceptions into categories, such as warnings that you should use to indicate warning conditions, and OS exceptions that Python raises depending on system error codes.

If you still didn’t find a fitting exception, then you can create a custom exception.

Lesson to learn: Asserts in Python are mainly meant to be used in tests and only during development phase just to ensure that things are not deviating from what is being expected e.g. that functions return sane values and that state variables do not contradict each other, and similar conditions. 
Also asserts are meant to fail early (in the spot where the error was detected) and thus AssertErrors are not really meant to be captured or handled programmatically.
"""
