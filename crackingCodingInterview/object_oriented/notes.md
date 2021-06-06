# Object Oriented Design Questions

1. Handle Ambiguity
   These questions are designed to be vague so that the interviewee asks questions.
   Go through the Who, What, When, Where, Why, How questions to make sure you understand the
   full context of the use case

2. Define Core Objects
   Identify the core objects of the system. They are usually nouns.
   If you are designing a library the core objects will be book, librarian, shelf, checkout card, member, etc

3. Analyze Relationships
   Once you know the object, you have to determine the relationship between them.
   Are some objects members of other objects, Do any inherit from another object.
   Are the relationships many-to-many or one-to-many?

4. Investigate Actions
   At this step you should have a basic outline but you will have to review and
   reconsider objects or relationships that you've missed.

There is no "right" design pattern, just create one that works for the problem.
Two common design patterns:

- Singleton Class
  This pattern makes there is only one instance of the class and ensures
  that there is access to that instance
  Many people dislike this pattern because it interferes with unit-testing/ considered and anti-pattern

- Factory Method
  This pattern creates an interface for creating an instance of the class.
  The subclasses decide what class to instantiate.
  Can either have an abstract creator class and not implement Factory method
  Or you can have a concrete creator class that provides implementation of Factory methods which will take
  a parameter that will be used to determine which class to instantiate.
