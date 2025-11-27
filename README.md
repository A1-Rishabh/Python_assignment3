# Python_assignment3
[A]
(Method Overriding)

1-Method overriding occurs when a subclass provides a new implementation of a method that already exists in its parent class.

2-It requires inheritance and always involves at least two classes.

3-The method in the parent and child classes must have the same name and the same parameters.

It allows the child class to modify, extend, or customize the behavior that it inherits from the parent class.

Method overriding supports run-time polymorphism and is essential for achieving dynamic behavior in object-oriented programming.


(Method Overloading)

1-Method overloading refers to the use of the same method name to perform different tasks by varying the number or type of parameters.

2-It takes place within the same class.

3-This allows a single method name to operate differently depending on the arguments passed to it.

4-Although Python does not strictly support traditional overloading, a similar effect can be achieved by using default parameters or variable-length arguments.

5-Method overloading improves code flexibility, readability, and reusability.



[B]
(Role of Constructors in Python)

1-A constructor is a special method that is automatically called when an object of a class is created.

2-It is mainly used to initialize the data members (variables) of the class.

3-The constructor prepares the object for use by assigning initial values, allocating memory, and performing setup operations.

4-It improves code efficiency by eliminating the need to call initialization methods separately.

5-In Python, the constructor method is always written as __init__(self, ...).


(Types of Constructors in Python)

->Default Constructor

This constructor does not take any argument other than self.

It is used when no initial values are required for the object.

->Parameterized Constructor

This constructor accepts parameters along with self.

It allows each object to be initialized with different values.

->Constructor with Default Arguments

This is a variation where default values are provided to the parameters.

It allows flexibility in object creation by making parameters optional.
