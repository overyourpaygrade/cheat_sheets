###### 0301 Classes, Instances, Type, Methods and Attributes
```
* Class: a blueprint for an instance
* Instance: a constructed object of the class
* Type: indicates the class the instance belongs to
* Attribute: any object value: object.attribute
* Method: a "callable attribute" defined in the class (function)
```
###### Instance Methods and Attributes
```
* A "car" can be seen as a class of object
* The car class provides the blueprint for a car object
* Each instance of a car does the same things (methods)
* But, each car instance has its own state (attributes)
```
###### An object's interface
```
* An object's interface is made up of its methods
* Methods are like "buttons" that operate the object
* Methods often change an instance's state (its data)
* A method's often complex implementation is hidden behind the interface
```

###### 0406 Decorators; Class and Static Methods
```
* A class method takes the class (not instance) as argument and works with the class object
* A static method requires no argument and does not work with the class or instance (but it still belongs in the class code)
* A decorator is a processor that modifies a function
* @classmethod and @staticmethod modify the default binding that instance methods provide
```

###### 0407 Abstract Base Classes
```
* An abstract class is a kind of "model" for other classes to be defined. It is not designed to contruct instances, but can be subclassed by regular classes. 
* Abstract classes can define an interface, or methods that must be implemented by its subclasses
* The python abc module enables the creation of abstract base classes
* For information, see the abc module and related docs
```

###### 0408 Inheritance Examples
```
* When working in a child class we can choose to implement parent class methods in different ways
    * Inherit: simply use the parent class' defined method
    * Override/overload: provide child's own version of a method
    * Extend: do work in addition to that in parent's method
    * Provide: implement abstract method that parent requires
```


