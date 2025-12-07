class Engine:
    def __init__ (self, horse_power):
        self.horse_power = horse_power
class Wheel:
    def __init__ (self, size):
        self.size = size
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power} (hp) {self.wheels[0].size} in" 

car1 = Car(make = "Ford", model="Mustang", horse_power=580, wheel_size=18)

#Nested Class = A class defined within another class OUter -> inner
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def get_details(self):
            return f"{self.name} {self.position}"
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position )
        self.employees.append(new_employee)
    def list_employee(self):
        return [employee.get_details() for employee in self.employees]
company = Company("Krusty Krab")
company.add_employee("Eugene", "Manager")
class Mail:
    def __init__(self,name, email, password):
        self.name = name
        self._email = email
        self._password = password
    def show(self):
        
        print(f"Your name is: {self.name}, are you log in {self._email}?")
user1 = Mail("Bob", "boblovwyou@gmail.com", "bob@thatsright")


class Vector:
    """Represent a vextor in a multidimensional space"""
    def __init__(self, d):
        self._coords = [0] * d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]
    def __setitem__(self, j, val):
        self._coords[j] = val
    def __add__(self, other):  # add self.list with other.list
        if len(self) != len(other):        # relies on len method
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result
    def __eq__(self, other):
        return self._coords == other._coords  # rely on existing __eq__ definition
    def __ne__(self, other):
        return not self == other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list presentation


class SequenceIterator:
    """An iterator for any of Python's sequence types"""
    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on first call to next
    def __next__(self): # call next, k += 1
        """Return the next element, or else eaise Stop Iteration error"""
        self._k += 1   # advance to next index
        if self._k < len(self._seq): 
            return (self._seq[self._k]) # return data element at k element
        else:
            raise StopIteration() # there are no more iteration
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self # Return itself as an iterator        
        
class CreditCard:
    """Consumer credit card"""
    def __init__(self, customer, bank, acnt, limit):
        "Create a new credit card instance"
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    def get_bank(self):
        """Return the bank name"""
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def charge(self, price):
        "Charge the given price to the card, assming sufficient credit limit"""
        # Return True if charge was processed, False if charge was denied
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        if self._balance - amount < 0:
            return "Insufficient limit"
        else:
            self._balance -= amount
            print('Bank successfully')
# Inheritance
class PredatoryCreditCard(CreditCard):
    OVERLIMITFEE = 5
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit) # call super constructor
        # extend the dat
        self._apr = apr
    def charge(self, price):
        success = super().charge(price)  # call inherited method
        if not success:  
            self._balance += 5 # assess penalty  
        return success
    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance  *= monthly_factor
# CREATE A STRUCTURE OF NUMERIC PROGRESSION
class Progression:
    '''Iterator producing a generic progression'''
    def __init__(self, start = 0):
        self._current = start
    def _advance(self): # private
        self._current += 1
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        return self
    def print_progression(self, n):
        return (' '.join(str(next(self)) for j in range (n))) # call self.next until it ends  loop
class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""
    def __init__(self, increment = 1, start=0):   # default data
        super().__init__(start)
        self._increment = increment
    def _advance(self):    # SELF CAN INHERITATED FROM PARENT
        self._current += self._increment # 1. 2. 3. 4, .....
class GeometricProgression(Progression):
    def __init__(self, base = 2, start=0): # Default value if none value is inpt in these sections
        super().__init__(start)
        self._base = base
    def _advance(self):
        self._current *= self._base
class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        self._prev = second - first
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

from abc import ABCMeta, abstractmethod      # constant method
class Sequence(metaclass = ABCMeta):
    @abstractmethod     # We can custom a constant method that run without coding it again, like header in page
    def __len__(self):
        "Return the length of the sequence"
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""
    def __contains__(self, val):
        """Return True if val found in the sequence, False otherwise"""
        for j in range (len(self)):
            if self[j] == val:
                return True
        return False
    def index(self, val):
        """Return leftmost index at which val is found(or raise ValueError)"""
        k = 0
        for j in range (len(self)):
            if self[j] == val:
                k += 1
            return k
# Polymorphism
# Example:
class Calculator:
    def multiply(self, a = 1, b = 1, *args):
        result = a * b
        for num in args:
            result *= num
        return result    
# default arg -> Calculator().multiply(4)
# multiple arg -> Calculator().multiply(2, 3) or (2, 3 ,4)
# Iterator
s = 'GFG'
it = iter(s)  # -> next(it) = G, next(it) = F, next(it) = G
# Custom iterator
class EvenNumber:
    def __iter__(self):
        self.n = 2
        return self
    def __next__(self):
        x = self.n
        self.n += 2
        return x 
# iter(EvenNumeber()) -> 2 4 6 8 10
# StopIteration Exception
li = [100, 200, 300]
it = iter(li)
accept = False
while accept:
    try: 
        print(next(it))
    except StopIteration:
        print('End of iteration')
        break
if __name__ == "__main__":
    cd = CreditCard('Andrew', 'Oxford Bank', '@drew2401', 10000)
    print(ArithmeticProgression(10).print_progression(5))
    print(ArithmeticProgression(5, 2).print_progression(5))
    print(GeometricProgression(2, 1).print_progression(5))    
    print(FibonacciProgression(0, 1).print_progression(10))

    from abc import ABC, abstractmethod
    def decorator(func):
        def wrapper():
            print("Before calling the function")
            func()
            print('After calling the function')
        return wrapper

    @decorator
    def greet():
        print('Hello World')


    '''
        def decorator_name(func):
            def wrapper(*args, **kwargs):
                print("Before Execution: ")
                result = func(*args, **kwargs)
                print("After Execution: ")
                return result
            return wrapper
        @decorator_name
        def add(a, b):
            return a + b
    '''
    #class_method: define a method that operates on class itself
    #@classmethod
    class Employee:
        raise_amount = 1.05 #class_method
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
        @classmethod
        def set_raise_amount(cls, amount):
            cls.raise_amount = amount
    # Using the class method
    Employee.set_raise_amount(1.1) # -> raise_amount = 1.1

    #@property: define a method as a property -> access like an attribute
    #useful for encapsulating implemention of a method 
    class Circle:
        def __init__(self, radius):
            self.radius = radius
        @property
        def radius(self):
            return self.radius
        @radius.setter
        def radius(self, value):
            if value > 0:
                self.radius = value
            else:
                raise ValueError("Radius cannot be negative")
        @property
        def area(self):
            return 3.14159 * (self.radius ** 2)
    # Chaining multiple decorators
    def decor1(func):
        def inner():
            x = func()
            return x * x
        return inner
    def decor(func):
        def inner():
            x = func()
            return 2 * x
        return inner
    @decor1
    @decor
    def num2():
        return 10 # -> 10 * 10 * 2
    # @abstractmethod -> a method that require subclass to be implemented
    class Animal:
        def sound(self):
            pass
    class Dog(Animal):
        def sound(self):
            return 'woof'  # when call Dog -> returns woof
    class Cat(Animal):
        def sound(self):
            return 'meow'
    # Polymorphism (OOP) -> allow same method do many tasks -> uppercase examples
    # Abstraction -> Hide internal logic and only shows necessary details, reduce chances of misuse or accidental changes
    # -> Similar to abstract method but used for properties -> these properties are declared with @property decorator
    class Animal(ABC):
        @property
        @abstractmethod
        def species(self):
            pass
    class Dog(Animal):
        @property
        def species(self):
            return "Corgi"
    # Encapsulation: Hiding internal details of class and only expose, change if necessary -> private, public, protected


    #Generators:
    def mygenerator(n):
        for x in range (n):
            yield x * 3
    # yield can be considered like an linked list, in the first call, it none, next return next value till StopIteration
    values = mygenerator(10)
    # print(next(values))  # ->> 0
    # print(next(values))  # ->> 1 * 3 (next value of x)

    ######################################
    """PROXY DESIGN PATTERN"""
    from abc import ABCMeta, abstractstaticmethod
    class IPerson(metaclass = ABCMeta):
        @abstractstaticmethod
        def person_method():
            ''' Interface Method '''
            pass
    class Person(IPerson):
        def person_method(self):
            print ('I am a person!')
    class ProxyPerson(IPerson):
        def __init__(self):
            self.person = Person()
        def person_method(self):
            print('I am the proxy functionality!')
            self.person.person_method() # -> 2 protected accessed key


    
        

