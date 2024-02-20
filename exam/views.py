from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import random
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse,JsonResponse
from random import sample

basic_questions = [
    {#1
        'question': 'Who developed Python Programming Language?',
        'options': ['Wick van Rossum', 'Rasmus Lerdorf', 'Guido van Rossum', 'Niene Stom'],
        'answer': 3,  # Index of the correct option
        'mark': 1
    },
    {#2
        'question': 'Which type of Programming does Python support?',
        'options': ['object-oriented programming', 'structured programming', 'functional programming', 'all of the mentioned'],
        'answer': 4,
        'mark': 1
    },
    {#3
        'question': 'Is Python case sensitive when dealing with identifiers?',
        'options': ['No','Yes','machine dependent','none of the mentioned'],
        'answer': 2,
        'mark': 1
    },
    {#4
        'question': 'Which of the following is the correct extension of the Python file?',
        'options': ['.python','.pl','.py','.p'],
        'answer': 3,
        'mark': 1
    },
    {#5
        'question': 'Is Python code compiled or interpreted?',
        'options': ['Python code is both compiled and interpreted',' Python code is neither compiled nor interpreted','Python code is only compiled','Python code is only interpreted'],
        'answer': 1,
        'mark': 1
    },
    {#6
        'question': 'All keywords in Python are in _________',
        'options': ['Capitalized','lower case','UPPER CASE','None of the mentioned'],
        'answer': 4,
        'mark': 1
    },
    {#7
        'question': 'What will be the value of the following Python expression?',
        'code': '''
4 + 3 % 5
''',
        'options': ['7','20','4','1'],
        'answer': 1,
        'mark': 1
    },
    {#8
        'question': 'Which of the following is used to define a block of code in Python language?',
        'options': ['Indentation','Key','Backets','All of the mentioned'],
        'answer': 1,
        'mark': 1
    },
    {#9
        'question': 'Which keyword is used for function in Python language?',
        'options': ['Function','def','Fun','Define'],
        'answer': 2,
        'mark': 1
    },
    {#10
        'question': 'Which of the following character is used to give single-line comments in Python?',
        'options': ['&#47;', '&#35;', '&#33;', '&#42;'],
        'answer': 2,
        'mark': 1 
    },
    {#11
        'question': 'What will be the output of the following Python code?',
        'code': '''
        i = 1
        while True:
            if i % 3 == 0:
                break
            print(i)
            
            i += 1
            ''',
        'options': ['1 2 3','error','1 2','none of the mentioned'],
        'answer': 2,
        'mark': 1 
    }, 
    {#12
        'question': 'Which of the following functions can help us to find the version of python that we are currently working on?',
        'options': ['sys.version(1)','sys.version(0)','sys.version()','sys.version'],
        'answer': 4,
        'mark': 1
    },
    {#13
        'question': 'Python supports the creation of anonymous functions at runtime, using a construct called __________',
        'options': ['Api','anonymous','lambda','none of the mentioned'],
        'answer': 3,
        'mark': 1
    },
    {#14
        'question': 'What is the order of precedence in python?',
        'options': ['Exponential, Parentheses, Multiplication, Division, Addition, Subtraction','Exponential, Parentheses, Division, Multiplication, Addition, Subtraction','Parentheses, Exponential, Multiplication, Division, Subtraction, Addition','Parentheses, Exponential, Multiplication, Division, Addition, Subtraction'],
        'answer': 4,
        'mark': 1
    },
    {#15
        'question': 'What will be the output of the following Python code snippet if x=1?',
        'code': '''
x<<2
''',
        'options': ['4','2','1','8'],
        'answer': 1,
        'mark': 1
    },
    {#16
        'question': 'What does pip stand for python?',
        'options': ['Pip Installs Python','Pip Installs Packages','Preferred Installer Program','All of the mentioned'],
        'answer': 2,
        'mark': 1
    },
    {#17
        'question': 'Which of the following is true for variable names in Python?',
        'options': ['underscore and ampersand are the only two special characters allowed','unlimited length','all private members must have leading and trailing underscores','none of the mentioned'],
        'answer': 2,
        'mark': 1
    },
    {#18
        'question': 'What are the values of the following Python expressions?',
        'code': '''
2*(3*2)
 (2**3)**2
 2*3*2

''',
        'options': ['512,64,512','512,512,512','64,512,64','64, 64, 64'],
        'answer': 1,
        'mark': 1
    },
    {#19
        'question': 'Which of the following is the truncation division operator in Python?',
        'options': ['|','//','/','%'],
        'answer': 2,
        'mark': 1
    },
    {#20
        'question': 'What will be the output of the following Python code?',
        'code': '''
l=[1, 0, 2, 0, 'hello', '', []]
list(filter(bool, l))
''',
        'options': ['[1, 0, 2, "hello", "", []]','Error','[1, 2, "hello"]','[1, 0, 2, 0, "hello", "", []]'],
        'answer': 3,
        'mark': 1
    },
    {#21
        'question':  'Which of the following functions is a built-in function in python?',
        'options': ['factorial()','print()','seed()','sqrt()'],
        'answer': 2,
        'mark': 1
    },
    {#22
        'question': 'Which of the following is the use of id() function in python?',
        'options': ['Every object doesnt have a unique id','Id returns the identity of the object','All of the mentioned','None of the mentioned'],
        'answer': 2,
        'mark': 1
    },
    {#23
        'question': 'The following python program can work with ____ parameters.',
        'code': '''
def f(x):
    def f1(*args, **kwargs):
           print("Sanfoundry")
           return x(*args, **kwargs)
    return f1

''',
        'options': ['any number of','0','1','2'],
        'answer': 1,
        'mark': 1
    },
    {#24
        'question': 'What will be the output of the following Python function?',
        'code': '''
min(max(False,-3,-4), 2,7)
''',
        'options': ['-4','-3','2','False'],
        'answer': 4,
        'mark': 1
    },
    {#25
       'question': 'Which of the following is not a keyword in Python language?',
       'options' :['pass','eval','assert','nonlocal'],
       'answer':2,
       'mark': 1

   },
   {#26
       'question': 'Which of the following is not a core data type in Python programming?',
       'options' :['Tuples','Lists','Class','Dictionary'],
       'answer':3,
       'mark': 1

   },
   {#27
       'question':'Which of these is the definition for packages in Python?',
       'options' :['A set of main modules','A folder of python modules','A number of files containing Python definitions and statements','A set of programs making use of Python modules'],
       'answer':2,
       'mark': 1
       
   },
   {#28
       'question':'What will be the output of the following Python function?',
       'code': '''
 len(["hello",2, 4, 6])
''',
       'options' :['Error','6','4','3'],
       'answer':3,
       'mark': 1
   }, 
   {#29
       'question':'What is the order of namespaces in which Python looks for an identifier?',
       'options' :['Python first searches the built-in namespace, then the global namespace and finally the local namespace','Python first searches the built-in namespace, then the local namespace and finally the global namespace','Python first searches the local namespace, then the global namespace and finally the built-in namespace','Python first searches the global namespace, then the local namespace and finally the built-in namespace'],
       'answer': 3,
       'mark': 1
   },
   {#30
        'question':'What will be the output of the following Python code snippet?',
        'code': '''
for i in [1, 2, 3, 4][::-1]:
    print(i, end=' ')'
''',
        'options' :['4 3 2 1','error','1 2 3 4','none of the mentioned'],
        'answer':1,
        'mark': 1
   },
    # Add more questions...
]

# Intermediate-level questions...
questions_intermediate = [
    {  # 1
        'question': 'What is the purpose of the init method in a Python class?',
        'options': ["To initialize the object's attributes"," To create a new instance of the class","To define a constructor for the class"," To initialize the class variables"],
        'answer': 1,
        'mark': 1
    },
    {  # 2
        'question': 'In Python, what does the *args syntax in a function definition represent?',
        'options':['A required argument','A variable number of positional arguments','A keyword argument','A default argument'],
        'answer': 2,
        'mark': 1
    },
    {  # 3
        'question': 'What is the key difference between a list and a tuple in Python?',
        'options': ['Lists are mutable, while tuples are immutable','Tuples are mutable, while lists are immutable','Both lists and tuples are immutable','Both lists and tuples are mutable'],
        'answer': 1,
        'mark': 1
    },
    {  # 4
        'question': 'How can you open a file in Python and ensure it is closed properly after usage?',
        'options': ['Using the file.open() method','Using the with open() statement','Using the file.close() method','Using the open.file() function'],
        'answer': 2,
        'mark': 1
    },
    {  # 5
        'question': 'What is the key difference between the append() and extend() methods of a list in Python?',
        'options': ['append() adds a single element, while extend() adds multiple elements','extend() adds a single element, while append() adds multiple elements','Both methods add elements to the end of the list, but extend() can only add one element at a time','There is no difference; the terms are interchangeable'],
        'answer': 1,
        'mark': 1
    },
    {  # 6
        'question': 'What does the following list comprehension do?',
        'code': '''
 Squarerd_numbers= [x**2 for x in range(10) if x%2==0] 
''',
        'options': ['Creates a list of squares for even numbers from 0 to 9','Creates a list of squares for all numbers from 0 to 9','Creates a list of even numbers from 0 to','Creates a list of squares for odd numbers from 0 to 9'],
        'answer': 1,
        'mark': 1
    },
    {  # 7
        'question': 'What is the output of the following code snippet?',
        'code': '''
 def foo (a, b=[ ]):
      b.append(a)
       return b
print(foo(1))
print(foo(2))

''',
        'options': ['[1] and [2]',' [1, 2] and [2]','[1] and [1,2]','[1, 2] and [1, 2]'],
        'answer': 4,
        'mark': 1
    },
    {  # 8
        'question': 'What is the purpose of the zip function in Python?',
        'options': ['To compress files','To combine two or more iterables element-wise','To extract files','To create a list of tuples'],
        'answer': 2,
        'mark': 1
    },
    {  # 9
        'question': 'What is the maximum length of a Python identifier?',
        'options': ['32','16','128','No fixed length is specified'],
        'answer': 4,
        'mark': 1
    },
    {  # 10
        'question': 'Which of the following is the proper syntax to check if a particular element is present in a list?',
        'options': ['if ele in list','if not ele not in list','Both a and b','None of the above'],
        'answer': 3,
        'mark': 1
    },
    {  # 11
        'question': 'Which of the following is not a valid set operation in python?',
        'options': ['Union','Intersection','Difference','None of the above'],
        'answer': 4,
        'mark': 1
    },
    {  # 12
        'question': 'As what datatype are the *kwargs stored, when passed into a function?',
        'options': ['Lists','Tuples','Dictionary','None of the above'],
        'answer': 3,
        'mark': 1
    },
    {  # 13
        'question': 'What keyword is used in Python to raise exceptions?',
        'options': ['raise','try','goto','except'],
        'answer': 1,
        'mark': 1
    },
    {  # 14
        'question': 'Which of the following are valid string manipulation functions in Python?',
        'options': ['count()','upper()','strip()','All of the above'],
        'answer': 4,
        'mark': 1
    },
    {  # 15
        'question': 'Which of the following concepts is not a part of Python?',
        'options': ['Pointers','Loops','Dynamic Typing','All of the above'],
        'answer': 1,
        'mark': 1
    },
    {  # 16
        'question': 'Which of the following statements are used in Exception Handling in Python?',
        'options': ['try','except','finally','All of the above'],
        'answer': 4,
        'mark': 1
    },
    {  # 17
        'question': 'How is a code block indicated in Python?',
        'options': ['Brackets','Indentation','Key','None of the above'],
        'answer': 2,
        'mark': 1
    },
    {  # 18
        'question': 'Which of the following types of loops are not supported in Python',
        'options': ['for','while','do-while','None of the above'],
        'answer': 3,
        'mark': 1
    },
    {  # 19
        'question': 'Which of the following functions converts date to corresponding time in Python?',
        'options': ['strptime()','strftime()','Both A and B','None of the above'],
        'answer': 1,
        'mark': 1
    },
    {  # 20
        'question': 'What will be the output of the following code snippet?',
        'code': '''
 set1 = {1, 3, 5}
set2 = {2, 4, 6}
print (len(set1 + set2))


''',
        'options': ['3','6','0','Error'],
        'answer': 4,
        'mark': 1
    },
    {  # 21
        'question': ' What is the purpose of the range() function in Python?',
        'options': ['Generate a list of numbers','Create a range object','Iterate over a sequence of numbers','All of the above'],
        'answer': 4,
        'mark': 1
    },
     {  # 22
        'question': 'What will be the result of the following expression in Python “2 ** 3 + 5 ** 2”?',
        'options': ['65536','33','169','None of these'],
        'answer': 2,
        'mark': 1
    },
     {  # 23
        'question': 'Which of the following operators is the correct option for power(ab)?',
        'options': ['a ^ b', 'a**b', 'a ^ ^ b', 'a^*b'],
        'answer': 2,
        'mark': 1
    },
     {  # 24
        'question': 'Which one of the following has the same precedence level?',
        'options': ['Division, Power, Multiplication, Addition and Subtraction','Division and Multiplication', 'Subtraction and Division','Power and Division'],
        'answer': 2,
        'mark': 1
    },
     {  # 25
        'question': ' "all([2,4,0,6])"  What will be the output of this function',
        'options': ['False','True','0','Invalid code'],
        'answer': 1,
        'mark': 1
    },
     {  # 26
        'question': 'What is the output of the following code?',
                'code': '''
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(max(my_dict))

''',
        'options': ['a','b','c','3'],
        'answer': 3,
        'mark': 1
    },
     {  # 27
        'question': 'What will be the datatype of the var in the below code snippet?',
        'code': '''
var = 10
print(type(var))
var = "Hello"
print(type(var))


''',
        'options': ['str and int','int and int','str and str','int and str'],
        'answer': 4,
        'mark': 1
    },
     {  # 28
        'question': 'What will be the output of the following code snippet?',
        'code': '''
word = "Python Programming"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
 if i % 2 == 0:
   converted_word += word2[i]
 else:
   converted_word += word1[i]
print(converted_word)


''',
        'options': ['pYtHoN PrOgRaMmInG','Python Programming','python programming','PYTHON PROGRAMMING'],
        'answer': 1,
        'mark': 1
    },
    # Add more questions...
]

#Advanced level questions
advanced_questions = [
    {#1
        'question': 'What is the purpose of the “_init_” method in Python classes?',
        'options': ['Initialization of class attributes', 'Creation of class instances', 'Destruction of class instances', 'Initialization of module-level variables'],
        'answer': 1,  # Index of the correct option
        'mark': 1
    },
    {#2
        'question': 'In Python, what is the primary use of metaclasses?',
        'options': ['Code organization', 'Code profiling', 'Class customization', 'Exception handling'],
        'answer': 3,
        'mark': 1
    },
    {#3
        'question': 'How does the Global Interpreter Lock (GIL) impact the performance of multi-threaded programs in Python?',
        'options': ['Improves performance','Has no impact','Degrades performance','Depends on the number of threads'],
        'answer': 3,
        'mark': 1
    },
    {#4
        'question': 'What is the purpose of the “functools” module in Python?',
        'options': ['Functional programming utilities','File I/O operations','Data serialization','Database connectivity'],
        'answer': 1,
        'mark': 1
    },
    {#5
        'question': 'How does a generator differ from a regular function in Python?',
        'options': ['Generators can only yield integers','Generators use the “yield” keyword','Generators cannot accept parameters','Generators are not iterable'],
        'answer': 2,
        'mark': 1
    },
    {#6
        'question': 'What is the primary use of the “_slots_” attribute in a Python class?',
        'options': ['Restricting the creation of new attributes','Defining class methods','Enabling multiple inheritance','Specifying default attribute values'],
        'answer': 1,
        'mark': 1
    },
    {#7
        'question': 'What is the purpose of the “asyncio” module in Python?',
        'options': ['Asynchronous programming','Synchronous programming','File manipulation','Network socket programming'],
        'answer': 1,
        'mark': 1
    },
    {#8
        'question': 'How does the “_getattribute” method differ from the “__getattr_” method in Python?',
        'options': ['“_getattribute” is called for undefined attributes','“__getattr” is called for all attribute access','They are used interchangeably','“__getattribute_” is called for all attribute access'],
        'answer': 4,
        'mark': 1
    },
    {#9
        'question': 'What does the “with” statement in Python primarily facilitate?',
        'options': ['Exception handling','Memory management','Context management','Dynamic typing'],
        'answer': 3,
        'mark': 1
    },
    {#10
        'question': 'What is the purpose of the “_future_” module in Python?',
        'options': ['Importing features from future Python versions', 'Enabling experimental features', 'Specifying module dependencies', 'Defining future class attributes'],
        'answer': 1,
        'mark': 1 
    },
    {#11
        'question': 'What is the purpose of the “_del_” method in Python?',
        'options': ['Initialization of class instances','Destruction of class instances','Garbage collection management','Delegation of attributes'],
        'answer': 2,
        'mark': 1 
    }, 
    {#12
        'question': 'In Python, what is the primary use of the “@staticmethod” decorator?',
        'options': ['Defining class methods','Creating instance methods','Handling exceptions','Enforcing method privacy'],
        'answer': 1,
        'mark': 1
    },
    {#13
        'question': 'What is the purpose of the “functools.partial” function in Python?',
        'options': ['Creating partial functions','Function composition','Function memoization','Function currying'],
        'answer': 1,
        'mark': 1
    },
    {#14
        'question': 'How does a deep copy differ from a shallow copy in Python?',
        'options': ['Deep copy copies only references','Shallow copy copies nested objects recursively','Deep copy creates independent copies of nested objects','Shallow copy is faster than deep copy'],
        'answer': 3,
        'mark': 1
    },
    {#15
        'question': ' What is the purpose of the “sys.argv” list in Python?',
        'options': ['Accessing environment variables','Command-line argument parsing','Retrieving module attributes','Specifying default function arguments'],
        'answer': 2,
        'mark': 1
    },
    {#16
        'question': 'What is the purpose of the “_new_” method in Python?',
        'options': ['Initialization of class attributes','Creation of class instances','Destruction of class instances','Initialization of module-level variables'],
        'answer': 2,
        'mark': 1
    },
    {#17
        'question': 'Which of the following statements about abstract classes in Python is true?',
        'options': ['Abstract classes cannot have any concrete methods','Abstract classes can be instantiated directly','Abstract classes must be subclassed to be instantiated','Abstract classes can be instantiated and used without any subclassing'],
        'answer': 3,
        'mark': 1
    },
    {#18
        'question': 'How is method resolution order (MRO) determined in Python for classes with multiple inheritance?',
        'options': ['Random order','Depth-first, left-to-right','Breadth-first, right-to-left','Depth-first, right-to-left'],
        'answer': 2,
        'mark': 1
    },
    {#19
        'question': 'What is the purpose of the “_call_” method in Python?',
        'options': ['Initialization of class instances','Execution when an object is called as a function','Garbage collection management','Delegation of attributes'],
        'answer': 2,
        'mark': 1
    },
    {#20
        'question': 'How does the “super()” function work in Python?',
        'options': ['Calls the superclass constructor','Calls a method in the superclass','Creates a new instance of the superclass','Initializes attributes in the superclass'],
        'answer': 2,
        'mark': 1
    },
    {#21
        'question':  'What is the purpose of the “@property” decorator in Python?',
        'options': ['Decorates methods as properties','Defines read-only properties for class attributes','Defines write-only properties for class attributes','Enforces encapsulation'],
        'answer': 2,
        'mark': 1
    },
    {#22
        'question': 'How can you force a thread to wait for the completion of another thread in Python?',
        'options': ['Using the “sleep()” function','Using the “join()” method','Using the “wait()” method','Using the “block()” function'],
        'answer': 2,
        'mark': 1
    },
    {#23
        'question': 'What is the purpose of the “_dict_” attribute in Python?',
        'options': ['Holds the instance variables of a class','Holds the attributes of a module','Holds the methods of a class','Holds the class variables of a class'],
        'answer': 1,
        'mark': 1
    },
    {#24
        'question': 'How can you implement a Singleton pattern in Python?',
        'options': ['Using a metaclass','Using the “_new” method','Using the “__init_” method','Using the “@singleton” decorator'],
        'answer': 2,
        'mark': 1
    },
    {#25
       'question': 'What is the purpose of the “_annotations_” attribute in Python?',
       'options' :['Stores the documentation strings of a module','Stores the annotations of function parameters','Stores the metadata of a class','Stores the type hints of function arguments'],
       'answer':2,
       'mark': 1

   },
   {#26
       'question': 'In Python, what does the term "duck typing" refer to?',
       'options' :['Typing variables using the “duck” keyword','Matching objects based on their behavior, not their type','Typing variables using the “typing” module','Using dynamic typing for all variables'],
       'answer':2,
       'mark': 1

   },
   {#27
       'question':'What is the purpose of the “_enter” and “__exit_” methods in a Python class?',
       'options' :['Context management with the “with” statement','Initialization and destruction of class instances','Handling exceptions within the class','Defining class-level properties'],
       'answer':1,
       'mark': 1
       
   },
   {#28
       'question':'How does the “collections.Counter” class work in Python?',
       'options' :['Counts the occurrences of elements in a list','Creates a counter for loop iterations','Counts the number of methods in a class','Maintains a count of active threads'],
       'answer':1,
       'mark': 1
   }, 
   {#29
       'question':'What is the purpose of the “threading.Lock” class in Python?',
       'options' :['Ensures thread safety in multithreaded programs','Implements a mutual exclusion mechanism','Controls access to a shared resource','Facilitates inter-process communication'],
       'answer': 3,
       'mark': 1
   },
   {#30
        'question':'How does the “contextlib” module in Python simplify the creation of context managers?',
        'options' :['By providing decorators for context managers','By automatically generating context managers for classes','By implementing context managers as functions using generators','By using metaclasses for context manager creation'],
        'answer':3,
        'mark': 1
   },
    # Add more questions...
]





def basic_section(request):
    
    random_questions = request.session.get('random_questions')
    if not random_questions:
        random_questions = random.sample(basic_questions, 10)
        request.session['random_questions'] = random_questions
    # else:
    #     random.shuffle(random_questions)
            

    if request.method == 'POST':
        total_marks = 0
        clicked_buttons = request.session.get('clicked_buttons', [False] * len(random_questions))
        finish_button_clicked = request.session.get('finish_button_clicked', False)
        
        if not finish_button_clicked:
            for i, question_data in enumerate(random_questions):
                user_answer = request.POST.get(f"question_{i + 1}", "")
                clicked_button = request.POST.get("check_answers", "")

                if clicked_button:
                    clicked_buttons[i] = True

                    correct_answer_index = question_data['answer'] 
                    correct_answer = question_data['options'][correct_answer_index-1 ]

                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            
            
        if total_marks :
            test_result = TestResult.objects.filter(user=request.user,section="Basic").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                test = TestResult.objects.create(user=request.user, score=total_marks,section="Basic")
            print(test_result)
            return render(request, 'basic.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
                
            })
            
        else:
            return render(request, 'basic.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
                
            })
    
    return render(request, 'basic.html', {'random_questions': random_questions})



def intermediate_section(request):
    scores=TestResult.objects.filter(user=request.user)
    print(scores)
    random_questions = request.session.get('random_questions_intermediate')
    if not random_questions:
        random_questions = random.sample(questions_intermediate, 10)
        request.session['random_questions_intermediate'] = random_questions
    # else:
    #     random.shuffle(random_questions)

    if request.method == 'POST':
        total_marks = 0
        clicked_buttons = request.session.get('clicked_buttons', [False] * len(random_questions))
        finish_button_clicked = request.session.get('finish_button_clicked', False)

        if not finish_button_clicked:
            for i, question_data in enumerate(random_questions):
                user_answer = request.POST.get(f"question_{i + 1}", "")
                clicked_button = request.POST.get("check_answers", "")

                if clicked_button:
                    clicked_buttons[i] = True

                    correct_answer_index = question_data['answer']  
                    correct_answer = question_data['options'][correct_answer_index - 1]

                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks

            request.session['clicked_buttons'] = clicked_buttons

            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
        if total_marks :
            test_result = TestResult.objects.filter(user=request.user,section="Intermediate").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks,section="Intermediate")
            return render(request, 'intermediate.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'intermediate.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
    
    return render(request, 'intermediate.html', {'random_questions': random_questions,'score':scores})



@login_required
def advanced_section(request):
    scores=TestResult.objects.filter(user=request.user)
    random_questions = request.session.get('random_questions_advanced')
    if not random_questions:
        random_questions = random.sample(advanced_questions, 10)
        request.session['random_questions_advanced'] = random_questions
    # else:
    #     random.shuffle(random_questions)
    
    if request.method == 'POST':
        total_marks = 0
        clicked_buttons = request.session.get('clicked_buttons', [False] * len(random_questions))
        finish_button_clicked = request.session.get('finish_button_clicked', False)

        if not finish_button_clicked:
            for i, question_data in enumerate(random_questions):
                user_answer = request.POST.get(f"question_{i + 1}", "")
                clicked_button = request.POST.get("check_answers", "")

                if clicked_button:
                    clicked_buttons[i] = True

                    correct_answer_index = question_data['answer'] 
                    correct_answer = question_data['options'][correct_answer_index - 1]

                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks

            request.session['clicked_buttons'] = clicked_buttons

            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
        if total_marks :
            test_result = TestResult.objects.filter(user=request.user,section="Advanced").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks,section="Advanced")
                
            return render(request, 'advanced.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'advanced.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'advanced.html', {'random_questions': random_questions,'score':scores})


class learning_page(TemplateView):
    template_name="basic_learning.html"


def intermediate_text_material(request):
    return render(request,'inter_learn.html')

def advanced_text_material(request):
    return render(request,"advanced_learning.html")

def basic_video_material(request):
    return render(request, 'video_basic.html')  

# def pythonintro(request):
#     return render(request, "pythonintro.html")
class pythonintro(TemplateView):
    template_name = 'pythonintro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TestResult.objects.filter(user=self.request.user)
        return context
  

