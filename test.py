import streamlit as st
import random
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from graphviz import Digraph
from gtts import gTTS
import pygame
import tempfile
import matplotlib.patches as patches
from matplotlib.patches import ConnectionPatch
import matplotlib.lines as lines



# List to store questions and answers
#basic questions list
questions = [
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
        'answer': 3,
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


def reset_basic_section():
    st.session_state.finish_button_clicked = False
    st.session_state.clicked_buttons = []
    st.session_state.total_marks = 0
    st.session_state.total_attempts = 0
    st.session_state.random_questions = None

def reset_intermediate_section():
    st.session_state.finish_button_clicked_intermediate = False
    st.session_state.clicked_buttons_intermediate = []
    st.session_state.total_marks_intermediate = 0
    st.session_state.total_attempts_intermediate = 0
    st.session_state.random_questions_intermediate = None


def reset_advanced_section():
    st.session_state.finish_button_clicked_advanced = False
    st.session_state.clicked_buttons_advanced = []
    st.session_state.total_marks_advanced = 0
    st.session_state.total_attempts_advanced = 0
    st.session_state.random_questions_advanced = None

def main():
    st.sidebar.header('Home')
    selected_section = st.sidebar.radio("", ['Basic', 'Intermediate', 'Advanced'])

    if selected_section == "Basic":
        basic_section()

    elif selected_section == 'Intermediate':
        intermediate_section()

    elif selected_section == 'Advanced':
        advanced_section()

# Function to convert text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
        tts.save(temp_wav.name)
    return temp_wav.name

# Function to play background music
def play_background_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

# Function to stop background music
def stop_background_music():
    pygame.mixer.music.stop()


#first python figure generation function
def generate_wordcloud(text, mask_image_path):
    # Load the mask image
    python_mask = np.array(Image.open(mask_image_path))

    # Create WordCloud with custom mask
    wc = WordCloud(stopwords=STOPWORDS, mask=python_mask, background_color="white",
                   contour_color="black", contour_width=3, min_font_size=3, max_words=100)

    # Generate the Word Cloud
    wc.generate(text)

    # Recolor the Word Cloud using the colors from the mask image
    colormap = ImageColorGenerator(python_mask)
    wc.recolor(color_func=colormap)
    
    return wc


#to  display data types in python
def create_tree_diagram():
    dot = Digraph(comment='Tree Diagram')
   
    # Set graph attributes
    dot.attr(bgcolor='#f0f0f0', fontcolor='black')

    # Add nodes and edges for the tree structure
    dot.node('A', 'Data Types', shape='ellipse', style='filled', color='#306998', fontname='Pacifico', penwidth='2', fontcolor='white')
    dot.node('B', 'Numeric', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontcolor='black')
    dot.node('C', 'Text', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontcolor='black')
    dot.node('D', 'Sequence', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontcolor='black')
    dot.node('E', 'Mapping', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontcolor='black')
    dot.node('F', 'Set', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontcolor='black')
    dot.node('G', 'Boolean', shape='ellipse', style='filled', color='#FFD43B', fontname='Pacifico', fontcolor='black')

    dot.node('H', 'int', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')
    dot.node('I', 'float', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')
    dot.node('J', 'complex', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')
    dot.node('L', 'list', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')
    dot.node('M', 'tuple', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')
    dot.node('N', 'range', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')
    dot.node('O', 'dict', shape='box', style='filled', color='#306998', fontname='Pacifico', fontcolor='white')

    dot.edges(['AB', 'AC', 'AD', 'AE', 'AF', 'AG'])
    dot.edges(['BH', 'BI', 'BJ'])
    dot.edges(['DL', 'DM', 'DN'])
    dot.edges(['EO'])

    # Manually set the font size for the entire graph in the DOT source code
    dot_source = dot.source.replace('fontname="Pacifico"', 'fontname="Pacifico" fontsize="20"')

    return dot_source


def basic_section():
    random_questions = st.session_state.get('random_questions')
    if not random_questions:
        random_questions = random.sample(questions, 10)
        st.session_state.random_questions = random_questions
    st.title("Personalized E-Learning")
    total_marks = getattr(st.session_state, 'total_marks', 0)
    total_questions = len(random_questions)  # Use the randomly selected questions
    max_marks = sum(question_data['mark'] for question_data in random_questions)

    clicked_buttons = st.session_state.get('clicked_buttons', [False] * total_questions)

    finish_button_clicked = st.session_state.get('finish_button_clicked', False)

    if not finish_button_clicked:
        for i, question_data in enumerate(random_questions):
            question = question_data['question']
            options = question_data['options']
            marks = question_data['mark']
           
            st.write(f"Question {i+1}: {question}")
            if 'code' in question_data:
                st.code(question_data['code'], language='python')

            user_answer = st.radio(f"Select an answer for Question {i+1}:", options)

            button_state_key = f"button_{i}_state"
            if i >= len(clicked_buttons):
                clicked_buttons.append(False)  # Ensure clicked_buttons has the correct length

            check_answer_button_state = clicked_buttons[i]
            check_answer_button = st.button(f"Check Answer for Question {i+1}", key=button_state_key,
                                            disabled=check_answer_button_state)

            if check_answer_button:
                clicked_buttons[i] = True

                correct_answer_index = question_data['answer']
                correct_answer = options[correct_answer_index - 1]

                if user_answer == correct_answer:
                    st.success("Correct!")
                    total_marks += marks
                    st.session_state.total_marks = total_marks

                else:
                    st.error(f"Wrong. The correct answer is: {correct_answer}")

        st.session_state.clicked_buttons = clicked_buttons

        percentage = (total_marks / max_marks) * 100 if total_questions > 0 else 0

        st.write(f"Total Marks Obtained: {total_marks}")
        st.write(f"Percentage: {percentage}%")

        # Add "Finish" button
        finish_button_clicked = st.button("Finish")
        if finish_button_clicked:
            st.session_state.finish_button_clicked = True

    else:
        # Display only the total score for basic level
        st.write(f"Total Marks Obtained - Basic Level : {total_marks}")
        if total_marks >= 7:
            st.session_state.basic_level_passed = True
            st.write('Congratulations! You have passed Level 1: Basics of Python')
            st.write('Please take the test for the Intermediate Level')

        else:
            st.write('Thank You for taking the test. But unfortunately you have not cleared Level 1 : Basics of Python')
            st.write("Don't worry, we are here to help you....... ")
            st.write("Further Study Options:")

            study_option = st.radio("Choose a study option:", ["Text Material", "Audio Material"])

            if study_option == "Text Material":
                st.subheader("Welcome to the World of Python ")
                text = open(r'D:\Internship Luminar\Main Projects\Personalized E-Learning\Personalized_E-Learning\keywrds.txt', 'r').read()
                wc = generate_wordcloud(text, "Image.png")
                st.image(wc.to_array(),width=450)
                text='Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.It is used for web development (server-side),software development,mathematics,system scripting. Python is a casesensitive programming language. This means that it considers uppercase and lowercase letters differently. As a result, in Python, we cannot use two terms with the same characters but different cases interchangeably. it is both compiled and interpreted language.'


                styled_text = f'<span style="font-family: Pacifico; color: #306998; font-size: 20px;">{text}</span>'
                st.markdown(styled_text, unsafe_allow_html=True)
                st.subheader("Tree Diagram of Data Types in Python")
                tree_diagram_source = create_tree_diagram()
                # Display the modified Graphviz DOT source code using the Source class
                st.graphviz_chart(tree_diagram_source, use_container_width=True)

                st.write("There are different types of data types in Python. Some built-in Python data types are : ")
                st.write("Numeric data types")
                st.write("String data types")
                st.write("Sequence types")
                st.write("Mapping data type")
                st.write("Set data types")
                st.write("Boolean type")
                st.write("Numeric: numeric data type is used to hold numeric values like; int,float and complex.int holds signed integers of non-limited length.float holds floating precision numbers and it's accurate up to 15 decimal places.Complex holds complex numbers.")
                st.write("String: The string is a sequence of characters")
                st.write("Sequence:  sequence refers to a collection of ordered elements. The main built-in sequence types in Python are: list, tuple and range.List is an ordered sequence of some data written using square brackets and commas.Tuple is another data type which is a sequence of data similar to a list. Data in a tuple is written using parenthesis and commas.Range is used to represent an immutable sequence of numbers.")
                st.write("Mapping: A mapping is a collection of key-value pairs, where each key is unique and associated with a corresponding value. The dict type is used to represent mappings in Python. The dictionary (dict) is a built-in data type that represents a collection of key-value pairs. It is a mutable, unordered, and dynamic data structure.")
                st.write("Set : Set is a built-in data type that represents an unordered collection of unique elements.")
                st.write("Boolean : boolean type represents Boolean values, which are either True or False.")

                # Add "Ready to take test again" button
                ready_button_clicked = st.button("Ready to take test again")
                if ready_button_clicked:
                    reset_basic_section()
                    st.experimental_rerun()  # Restart the test

            elif study_option == "Audio Material":
                st.write("Audio material goes here.")
                st.title("Basics of Python")

                # Initialize session state
                current_sentence = st.session_state.get("current_sentence", 0)
                paused = st.session_state.get("paused", False)

                # Load text
                text = '''There are different types of data types in Python.Some built-in Python data types are : Numeric data types, String data types, Sequence types, Mapping data type, Set data types, Boolean type.Numeric: numeric data type is used to hold numeric values like; int,float and complex.int holds signed integers of non-limited length.float holds floating precision numbers and it's accurate up to 15 decimal places.Complex holds complex numbers.String : The string is a sequence of characters.Sequence:  sequence refers to a collection of ordered elements.The main built-in sequence types in Python are: list, tuple and range.List is an ordered sequence of some data written using square brackets and commas.Tuple is another data type which is a sequence of data similar to a list.Data in a tuple is written using parenthesis and commas.Range is used to represent an immutable sequence of numbers.Mapping : A mapping is a collection of key-value pairs, where each key is unique and associated with a corresponding value.The dict type is used to represent mappings in Python.The dictionary (dict) is a built-in data type that represents a collection of key-value pairs.It is a mutable, unordered, and dynamic data structure.Set : Set is a built-in data type that represents an unordered collection of unique elements.Boolean : boolean type represents Boolean values, which are either True or False.'''

                sentences = text.split('.')

                # Load background music
                background_music_file = r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Personalized_E-Learning\Music.wav"

                # Play background music
                play_background_music(background_music_file)

                # Display current sentence and control buttons
                st.text(sentences[current_sentence])

                # Pause, Continue, Replay buttons
                col1, col2, col3 = st.columns(3)

                # Pause button
                if col1.button("Pause"):
                    paused = True

                # Continue button
                if col2.button("Continue"):
                    paused = False

                # Replay button
                if col3.button("Replay"):
                    current_sentence = 0  # Reset to the beginning
                    paused = False

                # Check if paused
                if not paused:
                    # Play text-to-speech
                    audio_file_path = text_to_speech(sentences[current_sentence])
                    st.audio(audio_file_path, format='audio/wav')

                    # Increment current sentence
                    current_sentence += 1

                    # # Check if it's the last sentence
                    # if current_sentence == len(sentences):
                    #     stop_background_music()

                # Save session state
                st.session_state.current_sentence = current_sentence
                st.session_state.paused = paused
            

                # Add "Ready to take test again" button
                ready_button_clicked = st.button("Ready to take test again")
                if ready_button_clicked:
                    stop_background_music()  # Stop the background music
                    reset_basic_section()
                    st.experimental_rerun()  # Restart the test

# Function to generate the plot for if-else
def generate_plot():
    fig, ax = plt.subplots()

    # Small ellipse shape
    ellipse1 = patches.Ellipse((0.3, 0.9), 0.1, 0.05, edgecolor='black', facecolor='darkblue')
    ax.add_patch(ellipse1)
    ax.text(0.3, 0.9, "...", ha='center', va='center', color='white', weight='bold')  # Adding text to the ellipse

    # Arrow from ellipse to diamond
    arrow1 = patches.ConnectionPatch((0.3, 0.875), (0.3, 0.800), 'data', 'data', arrowstyle='->', linewidth=1, color='black', mutation_scale=15)
    ax.add_patch(arrow1)

    # Smaller diamond shape
    diamond = patches.RegularPolygon((0.3, 0.7), numVertices=4, radius=0.1, edgecolor='black', facecolor='blue')
    ax.add_patch(diamond)
    ax.text(0.3, 0.7, "Condition", ha='center', va='center', color='white', weight='bold')  # Adding text to the diamond

    # Arrow from diamond to rectangle
    arrow2 = patches.ConnectionPatch((0.3, 0.6), (0.3, 0.4), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow2)
    ax.text(0.2, 0.5, "When the if\nCondition is\nFalse", ha='center', va='center', color='black')  # Adding text to the left of arrow2

    # Line from diamond edge to the right
    line_from_diamond = lines.Line2D([0.4, 0.65], [0.7, 0.7], linewidth=1, color='black')
    ax.add_line(line_from_diamond)

    # Arrow from the line to the new rectangle in downward direction
    arrow_downward = patches.ConnectionPatch((0.65, 0.7), (0.65, 0.5), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow_downward)
    ax.text(0.75, 0.6, "When the if\nCondition is\nTrue", ha='center', va='center', color='black')  # Adding text to the right of arrow_downward

    # Rectangle shape with increased width
    rectangle1 = patches.Rectangle((0.2, 0.3), 0.2, 0.1, edgecolor='black', facecolor='blue')
    ax.add_patch(rectangle1)
    ax.text(0.3, 0.35, "else Block", ha='center', va='center', color='white', weight='bold')  # Adding text to the rectangle

    # Arrow from rectangle1 to ellipse
    arrow3 = patches.ConnectionPatch((0.3, 0.3), (0.3, 0.175), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow3)

    # Small ellipse shape (same size as the first one)
    ellipse2 = patches.Ellipse((0.3, 0.15), 0.1, 0.05, edgecolor='black', facecolor='darkblue')
    ax.add_patch(ellipse2)
    ax.text(0.3, 0.15, "...", ha='center', va='center', color='white', weight='bold')  # Adding text to the second ellipse

    # Rectangle to the right, slightly above
    rectangle2 = patches.Rectangle((0.55, 0.4), 0.2, 0.1, edgecolor='black', facecolor='blue')
    ax.add_patch(rectangle2)
    ax.text(0.65, 0.45, "if Block", ha='center', va='center', color='white', weight='bold')  # Adding text to the second rectangle

    # Line from rectangle2 to downward
    line_downward = lines.Line2D([0.65, 0.65], [0.4, 0.23], linewidth=1, color='black')
    ax.add_line(line_downward)

    # Arrow from line_downward to the left
    arrow_left = patches.ConnectionPatch((0.65, 0.23), (0.3, 0.23), 'data', 'data', arrowstyle='->', linewidth=1, color='black')
    ax.add_patch(arrow_left)

    plt.axis('off')

    return fig

# Function to generate the plot for for-loop
def draw_flowchart():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Ellipse
    ellipse = patches.Ellipse((0.5, 0.85), 0.28, 0.2, fill=True, edgecolor='black', facecolor='green')
    ax.add_patch(ellipse)
    ax.text(0.5, 0.85, 'Start', ha='center', va='center', color='white', weight='bold')  # Add text to the center of the ellipse

    # Diamond shape with corrected orientation, filled with yellow
    diamond = patches.RegularPolygon((0.5, 0.525), numVertices=4, radius=0.13, orientation=0, fill=True, edgecolor='black', facecolor='yellow')
    ax.add_patch(diamond)
    ax.text(0.5, 0.525, 'Condition', ha='center', va='center', color='black', weight='bold')  # Add text to the center of the diamond

    # Larger Parallelogram, filled with blue
    parallelogram = patches.Polygon([(0.35, 0.3), (0.6, 0.3), (0.7, 0.18), (0.45, 0.18)],
                                    closed=True, fill=True, edgecolor='black', facecolor='blue')
    ax.add_patch(parallelogram)
    ax.text(0.525, 0.24, 'Statements', ha='center', va='center', color='white', weight='bold')  # Add text to the center of the parallelogram

    # Rectangle to the right and just above the parallelogram, filled with violet
    rectangle = patches.Rectangle((0.75, 0.33), 0.2, 0.12, fill=True, edgecolor='black', facecolor='violet')
    ax.add_patch(rectangle)
    ax.text(0.85, 0.39, 'Update', ha='center', va='center', color='black', weight='bold')  # Add text to the center of the rectangle

    # Connection patch from ellipse to diamond
    arrow1 = patches.ConnectionPatch((0.5, 0.77), (0.5, 0.63), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow1)

    # Connection patch from diamond to parallelogram
    arrow2 = patches.ConnectionPatch((0.5, 0.418), (0.5, 0.28), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow2)

    # Add "True" text to the right of arrow2
    ax.text(0.525, 0.35, 'True', ha='left', va='center', color='black', weight='bold')

    # Arrow from right to left starting from the right side of the diamond
    arrow3 = patches.ConnectionPatch((0.865, 0.525), (0.615, 0.525), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow3)

    # Connection patch upwards from the right side of the rectangle
    arrow_up = patches.ConnectionPatch((0.85, 0.23), (0.85, 0.35), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow_up)

    # Line upwards from the right side of the rectangle
    ax.plot([0.85, 0.85], [0.45, 0.525], color='black', linewidth=1)  # Adjust linewidth as needed
    ax.plot([0.645, 0.85], [0.25, 0.25], color='black', linewidth=1)
    ax.plot([0.15, 0.37], [0.525, 0.525], color='black', linewidth=1) 

    # Ellipse to the left of parallelogram below it
    ellipse_left_parallelogram = patches.Ellipse((0.15, 0.25), 0.28, 0.2, fill=True, edgecolor='black', facecolor='red')
    ax.add_patch(ellipse_left_parallelogram)
    # ax.plot([0.15, 0.15], [0.35, 0.525], color='black', linewidth=1) 
    arrow_end = patches.ConnectionPatch((0.15, 0.54), (0.15, 0.33), "data", "data", arrowstyle="->", shrinkA=5, shrinkB=5, mutation_scale=15, color='black')
    ax.add_patch(arrow_end)

    ax.text(0.15, 0.25, 'End', ha='center', va='center', color='white', weight='bold')  # Add text to the center of the ellipse

    # Text "False" on the left side of the line from the diamond
    ax.text(0.3, 0.55, 'False', ha='right', va='center', color='black', weight='bold')

    # Set axis limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove axes for clarity
    ax.axis('off')

    # Display the plot using Streamlit
    st.pyplot(fig)

# Function to generate the plot for while-loop
def draw_flowchart1():
    # Create figure and axes
    fig, ax = plt.subplots()

    # Create ellipse and fill with green
    ellipse = patches.Ellipse((0.3, 0.88), 0.4, 0.2, edgecolor='black', facecolor='green')
    ax.add_patch(ellipse)

    # Create arrow pointing downward
    arrow = ConnectionPatch((0.3, 0.78), (0.3, 0.67), 'data', 'data', arrowstyle='->', color='black', linewidth=2)
    ax.add_patch(arrow)

    # Create diamond shape at the arrowhead, fill with yellow, and set border color to black
    diamond = patches.RegularPolygon((0.3, 0.5), numVertices=4, radius=0.17, orientation=np.deg2rad(90), facecolor='yellow', fill=True, edgecolor='black')
    ax.add_patch(diamond)

    # Create arrow pointing downward from the bottom of the diamond
    arrow_below_diamond = ConnectionPatch((0.3, 0.33), (0.3, 0.24), 'data', 'data', arrowstyle='->', color='black', linewidth=2)
    ax.add_patch(arrow_below_diamond)

    # Create ellipse at the bottom of the second arrow and fill with red
    ellipse_below_arrow = patches.Ellipse((0.3, 0.14), 0.4, 0.2, edgecolor='black', facecolor='red')
    ax.add_patch(ellipse_below_arrow)

    # Create parallelogram to the right and above the diamond and fill with blue
    parallelogram = patches.Polygon(np.array([[0.6, 0.6], [0.9, 0.6], [1.0, 0.4], [0.7, 0.4]]), edgecolor='black', facecolor='blue')
    ax.add_patch(parallelogram)

    # Add a line starting from the center of the first arrow to the right
    line_x = [0.3, 0.75]  # X-coordinates for the line
    line_y = [0.75, 0.75]  # Y-coordinates for the line
    ax.plot(line_x, line_y, color='black', linewidth=2)

    # Draw a line from the parallelogram to upwards
    line_parallelogram_x = [0.75, 0.75]  # X-coordinates for the line
    line_parallelogram_y = [0.605, 0.75]   # Y-coordinates for the line
    ax.plot(line_parallelogram_x, line_parallelogram_y, color='black', linewidth=2)

    # Draw an arrow from the right edge of the diamond to the left side of the parallelogram
    arrow_diamond_to_parallelogram = ConnectionPatch((0.3 + 0.17, 0.5), (0.65, 0.5), 'data', 'data', arrowstyle='->', color='black', linewidth=2)
    ax.add_patch(arrow_diamond_to_parallelogram)

    # Add text to the patches
    ax.text(0.3, 0.88, 'Start', ha='center', va='center', color='black', fontsize=10, weight='bold')
    ax.text(0.3, 0.5, 'Condition', ha='center', va='center', color='black', fontsize=10, weight='bold')
    ax.text(0.3, 0.14, 'End', ha='center', va='center', color='black', fontsize=10, weight='bold')
    ax.text(0.8, 0.5, 'Statement', ha='center', va='center', color='black', fontsize=10, weight='bold')

    # Add text 'True' just above the line joining diamond and parallelogram
    ax.text(0.55, 0.53, 'True', ha='center', va='center', color='black', fontsize=10)

    # Add text 'False' to the right of the second arrow
    ax.text(0.32, 0.3, 'False', ha='left', va='center', color='black', fontsize=10)

    # Turn off the axis box
    ax.set_axis_off()

    # Set aspect ratio to 'equal' for a more accurate representation
    ax.set_aspect('equal', adjustable='box')

    # Display the plot
    st.pyplot(fig)



def intermediate_section():
    # Check if the user has passed the basic level
    basic_level_passed = st.session_state.get('basic_level_passed', False)

    if not basic_level_passed:
        st.warning("You need to pass the Basic level first.")
        return

    random_questions = st.session_state.get('random_questions_intermediate')
    if not random_questions:
        random_questions = random.sample(questions_intermediate, 10)
        st.session_state.random_questions_intermediate = random_questions
    
    st.title("Personalized E-Learning")
    total_marks = getattr(st.session_state, 'total_marks_intermediate', 0)
    total_questions = len(random_questions)
    max_marks = sum(question_data['mark'] for question_data in random_questions)

    clicked_buttons = st.session_state.get('clicked_buttons_intermediate', [False] * total_questions)

    finish_button_clicked = st.session_state.get('finish_button_clicked_intermediate', False)
    if not finish_button_clicked:
        for i, question_data in enumerate(random_questions):
            question = question_data['question']
            options = question_data['options']
            marks = question_data['mark']

            st.write(f"Question {i + 1}: {question}")
            if 'code' in question_data:
                st.code(question_data['code'], language='python')

            user_answer = st.radio(f"Select an answer for Question {i + 1}:", options)

            # button_state_key = f"button_{i}_state_intermediate"
            button_state_key = f"button_{i}_state_intermediate"
            if i >= len(clicked_buttons):
                clicked_buttons.append(False)  # Ensure clicked_buttons has the correct length
            check_answer_button_state = clicked_buttons[i]
            check_answer_button = st.button(f"Check Answer for Question {i + 1}", key=button_state_key,
                                            disabled=check_answer_button_state)

            if check_answer_button:
                clicked_buttons[i] = True

                correct_answer_index = question_data['answer']
                correct_answer = options[correct_answer_index - 1]

                if user_answer == correct_answer:
                    st.success("Correct!")
                    total_marks += marks
                    st.session_state.total_marks_intermediate = total_marks

                else:
                    st.error(f"Wrong. The correct answer is: {correct_answer}")

        st.session_state.clicked_buttons_intermediate = clicked_buttons

        percentage = (total_marks / max_marks) * 100 if total_questions > 0 else 0

        st.write(f"Total Marks Obtained: {total_marks}")
        st.write(f"Percentage: {percentage}%")

        # Add "Finish" button
        finish_button_clicked = st.button("Finish Intermediate Section")
        if finish_button_clicked:
            st.session_state.finish_button_clicked_intermediate = True
            
    else:
        # Display only the total score for basic level
        st.write(f"Total Marks Obtained - Intermediate Level : {total_marks}")
        if total_marks >= 7:  # Adjust the passing criteria as needed
            st.session_state.intermediate_level_passed = True
            st.write("Congratulations! You have completed the Intermediate level.")
            st.write('Please take the test for the Advanced Level')

        else:
            st.write("Thank You for taking the test. But unfortunately you have not cleared the Intermediate level")
            st.write("Further Study Options:")
            study_option = st.radio("Choose a study option:", ["Text Material", "Audio Material"])

            if study_option == "Text Material":
                st.write("Intermediate Text material goes here.")

                st.title('If-Else')
                # Display the plot for if-else
                st.pyplot(generate_plot())

                st.write("if-else : In Python, the if-else statement is used for conditional execution of code. It allows you to specify two blocks of code: one to be executed if a certain condition is true (if block), and another to be executed if the condition is false (else block).")
                
                st.title("for-loop")
                # Draw the flowchart for for-loop
                draw_flowchart()

                st.write("'for' loop : In Python, a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a string, or other iterable objects). for loops are a fundamental part of Python and are widely used for iterating through data structures, processing elements, and performing repetitive tasks.")

                st.title("while-loop")
                # Draw the flowchart for while-loop
                draw_flowchart1()

                st.write("'while' loop : In Python, a while loop is used to repeatedly execute a block of code as long as a given condition is true. Be cautious when using while loops to avoid unintentional infinite loops. It's crucial to ensure that the condition eventually becomes False to allow the loop to exit. Otherwise, the program will continue running indefinitely.")




                # Add "Ready to take test again" button
                ready_button_clicked = st.button("Ready to take test again")
                if ready_button_clicked:
                    reset_intermediate_section()
                    st.experimental_rerun()  # Restart the test

            elif study_option == "Audio Material":
                st.write("Intermediate Audio material goes here.")
                st.title("Intermediates of Python")

                # Initialize session state
                current_sentence = st.session_state.get("current_sentence", 0)
                paused = st.session_state.get("paused", False)

                # Load text
                text = '''if-else : In Python, the if-else statement is used for conditional execution of code.It allows you to specify two blocks of code: one to be executed if a certain condition is true (if block), and another to be executed if the condition is false (else block).“for” loop : In Python, a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a string, or other iterable objects).for loops are a fundamental part of Python and are widely used for iterating through data structures, processing elements, and performing repetitive tasks.“while" loop : In Python, a while loop is used to repeatedly execute a block of code as long as a given condition is true.Be cautious when using while loops to avoid unintentional infinite loops.It's crucial to ensure that the condition eventually becomes False to allow the loop to exit.Otherwise, the program will continue running indefinitely.'''

                sentences = text.split('.')

                # Load background music
                background_music_file = r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\AI Tutor\Music.wav"

                # Play background music
                play_background_music(background_music_file)

                # Display current sentence and control buttons
                st.text(sentences[current_sentence])

                # Pause, Continue, Replay buttons
                col1, col2, col3 = st.columns(3)

                # Pause button
                if col1.button("Pause"):
                    paused = True

                # Continue button
                if col2.button("Continue"):
                    paused = False

                # Replay button
                if col3.button("Replay"):
                    current_sentence = 0  # Reset to the beginning
                    paused = False

                # Check if paused
                if not paused:
                    # Play text-to-speech
                    audio_file_path = text_to_speech(sentences[current_sentence])
                    st.audio(audio_file_path, format='audio/wav')

                    # Increment current sentence
                    current_sentence += 1

                    # # Check if it's the last sentence
                    # if current_sentence == len(sentences):
                    #     stop_background_music()

                # Save session state
                st.session_state.current_sentence = current_sentence
                st.session_state.paused = paused

                # Add "Ready to take test again" button
                ready_button_clicked = st.button("Ready to take test again")
                if ready_button_clicked:
                    stop_background_music()  # Stop the background music
                    reset_intermediate_section()
                    st.experimental_rerun()  # Restart the test

materials = [
    {"category": "Documentation", "name": "Python Documentation", "link": "https://docs.python.org/3/"},
    {"category": "Video Tutorials", "name": "sentdex - Python Programming for Beginners", "link": "https://www.youtube.com/playlist?list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M"},
    {"category": "Video Tutorials", "name": "Academind - Python Tutorial for Beginners", "link": "https://www.youtube.com/watch?v=YYXdXT2l-Gg"},
    {"category": "Books", "name": "\"Dive into Python 3\" by Mark Pilgrim", "link": "https://diveinto.org/python3/"},
    {"category": "Books", "name": "\"Think Python\" by Allen B. Downey", "link": "http://greenteapress.com/thinkpython2/html/index.html"},
    {"category": "Educational Platforms", "name": "HackerRank - Python Practice", "link": "https://www.hackerrank.com/domains/tutorials/10-days-of-python"},
    {"category": "Educational Platforms", "name": "GitHub - Python Programming", "link": "https://github.com/geekcomputers/Python"},
    {"category": "Educational Platforms", "name": "Kaggle Courses - Python", "link": "https://www.kaggle.com/learn/python"}
    ]


# Function to create the plot for oops
def create_oo_plot():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(7, 7))

    # Draw a larger circle in the center with shadow
    circle_center = plt.Circle((0, 0), 0.3, edgecolor='black', facecolor='gray', lw=2, alpha=0.5)
    ax.add_patch(circle_center)

    # Draw lines radiating from the circumference with text boxes at the end and shadows
    num_lines = 6
    theta_values = np.linspace(0, 2 * np.pi, num_lines, endpoint=False)
    line_length = 0.5  # Adjusted line length

    box_labels = ['Class', 'Object', 'Encapsulation', 'Polymorphism', 'Inheritance', 'Abstraction']

    for i, theta in enumerate(theta_values):
        x = 0.3 * np.cos(theta)
        y = 0.3 * np.sin(theta)

        # Coordinates for the end of the line
        end_x = x + line_length * np.cos(theta)
        end_y = y + line_length * np.sin(theta)

        # Plot the shadow of the line
        ax.plot([x, end_x], [y, end_y], color='gray', lw=2, alpha=0.5)

        # Plot the line
        ax.plot([x, end_x], [y, end_y], color='black', lw=2)

        # Add a text box at the end of the line with a label and increased box size
        label = f'{box_labels[i]}'

        # Add a shadow for the text box
        ax.text(end_x + 0.07, end_y - 0.07, label, ha='center', va='center',
                bbox=dict(facecolor='gray', edgecolor='none', boxstyle='round,pad=2'), alpha=0.5)

        # Add the text box
        ax.text(end_x, end_y, label, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=2'))

    # Add the center text without a box
    ax.text(0, 0, 'Object\nOriented\nProgramming', ha='center', va='center', fontsize=14)

    # Set aspect ratio to be equal
    ax.set_aspect('equal', adjustable='box')

    # Remove axes for a cleaner look
    ax.axis('off')

    return fig


# Function to generate the plot for python applications
def draw_flower():
    num_petals = 6
    central_radius = 2.5
    surrounding_radius = 1.0
    distance = 5.0

    angle = np.linspace(0, 2 * np.pi, 100)

    central_x = central_radius * np.cos(angle)
    central_y = central_radius * np.sin(angle)
    plt.plot(central_x, central_y, color='purple')

    text_x = 0
    text_y = 0
    plt.text(text_x, text_y, "PYTHON", color='black', ha='center', va='center', fontsize=12, fontweight='bold')

    texts = ["Data Science", "Web\nDevelopment", "Game\nDevelopment", "Desktop GUIs", "Web Scraping", "CAD"]
    colors = plt.cm.viridis(np.linspace(0, 1, num_petals))

    for i in range(num_petals):
        x = (surrounding_radius + distance) * np.cos(i * (2 * np.pi / num_petals))
        y = (surrounding_radius + distance) * np.sin(i * (2 * np.pi / num_petals))
        plt.plot(x + central_x, y + central_y, color=colors[i], linestyle='--')

        text_x = x
        text_y = y
        text_color = colors[i]
        plt.text(text_x, text_y, texts[i], color=text_color, ha='center', va='center', fontsize=8)

    plt.axis('equal')
    plt.axis('off')

    # Return the Matplotlib figure
    return plt.gcf()


def advanced_section():
    # Check if the user has passed the intermediate level
    intermediate_level_passed = st.session_state.get('intermediate_level_passed', False)

    if not intermediate_level_passed:
        st.warning("You need to pass the Intermediate level first.")
        return

    # Rest of the advanced section
    random_questions = st.session_state.get('random_questions_advanced')
    if not random_questions:
        random_questions = random.sample(advanced_questions, 10)
        st.session_state.random_questions_advanced = random_questions
    
    st.title("Personalized E-Learning")
    total_marks = getattr(st.session_state, 'total_marks_advanced', 0)
    total_questions = len(random_questions)
    max_marks = sum(question_data['mark'] for question_data in random_questions)

    clicked_buttons = st.session_state.get('clicked_buttons_advanced', [False] * total_questions)

    finish_button_clicked = st.session_state.get('finish_button_clicked_advanced', False)
    if not finish_button_clicked:
        for i, question_data in enumerate(random_questions):
            question = question_data['question']
            options = question_data['options']
            marks = question_data['mark']

            st.write(f"Question {i + 1}: {question}")
            if 'code' in question_data:
                st.code(question_data['code'], language='python')

            user_answer = st.radio(f"Select an answer for Question {i + 1}:", options)

            # button_state_key = f"button_{i}_state_advanced"
            button_state_key = f"button_{i}_state_advanced"
            if i >= len(clicked_buttons):
                clicked_buttons.append(False)  # Ensure clicked_buttons has the correct length
            check_answer_button_state = clicked_buttons[i]
            check_answer_button = st.button(f"Check Answer for Question {i + 1}", key=button_state_key,
                                            disabled=check_answer_button_state)

            if check_answer_button:
                clicked_buttons[i] = True

                correct_answer_index = question_data['answer']
                correct_answer = options[correct_answer_index - 1]

                if user_answer == correct_answer:
                    st.success("Correct!")
                    total_marks += marks
                    st.session_state.total_marks_advanced = total_marks

                else:
                    st.error(f"Wrong. The correct answer is: {correct_answer}")

        st.session_state.clicked_buttons_advanced = clicked_buttons

        percentage = (total_marks / max_marks) * 100 if total_questions > 0 else 0

        st.write(f"Total Marks Obtained: {total_marks}")
        st.write(f"Percentage: {percentage}%")

        # Add "Finish" button
        finish_button_clicked = st.button("Finish Advanced Section")
        if finish_button_clicked:
            st.session_state.finish_button_clicked_advanced = True
            
    else:
        # Display only the total score for basic level
        st.write(f"Total Marks Obtained - Advanced Level : {total_marks}")
        if total_marks >= 5:  # Adjust the passing criteria as needed
            st.session_state.advanced_level_passed = True
            st.write("Congratulations! You have completed all the levels .")

            st.subheader("Reference Materials")

            current_category = None
            for material in materials:
                if material.get("category") != current_category:
                    if current_category is not None:
                        st.write("")  # Add an empty line to separate categories
                    st.subheader(material["category"])
                    current_category = material["category"]

                st.write(f"- [{material['name']}]({material['link']})")


        else:
            st.write("Thank You for taking the test. But unfortunately you have not cleared the Advanced level")
            st.write("Don't worry, we are here to help you....... ")
            st.write("Further Study Options:")
            study_option = st.radio("Choose a study option:", ["Text Material", "Audio Material"])

            if study_option == "Text Material":
                st.write("Advanced Text material goes here.")

                st.title('Python Applications')
                st.subheader("Python Applications")
                # Get the Matplotlib figure from the draw_flower function
                fig = draw_flower()
    
                # Display the plot using Streamlit
                st.pyplot(fig)

                st.write("'Python applications' refers to software programs or systems that are developed using the Python programming language.Python applications can be found in a wide range of domains, including : ")
                st.write("    • Web Development: Python is widely used for building web applications, and frameworks like Django and Flask make it easier to develop robust and scalable web solutions.")
                st.write("    • Data Science: Python is a popular choice for data analysis, machine learning, and artificial intelligence. Libraries like NumPy, Pandas, TensorFlow, and PyTorch support these domains.")
                st.write("    • CAD : Python is commonly applied in CAD for automating repetitive design tasks, creating parametric designs, and developing custom tools and plugins that enhance the functionality of CAD software. Its versatility allows for seamless integration, enabling data analysis, visualization, and efficient collaboration within the design and engineering workflow.")
                st.write("    • Web scraping: Python is widely utilized in web scraping to extract data from websites by leveraging libraries like BeautifulSoup and Scrapy, allowing developers to automate the retrieval of information for analysis or other purposes. Its simplicity and rich ecosystem make Python a popular choice for building web scraping scripts that navigate through web pages, parse HTML, and collect structured data.")
                st.write("    • Desktop GUIs: Python can be used to create desktop applications with graphical user interfaces (GUIs) using tools like Tkinter, PyQt, or Kivy.")
                st.write("    • Game Development: Python is used for developing simple to moderate complexity games, often leveraging libraries like Pygame.")


                st.title('Object-Oriented Programming Concepts')
                # Create and display the plot for oops
                
                oo_plot = create_oo_plot()

                # Display the plot
                st.pyplot(oo_plot)


                st.write("OOPs stands for Object-Oriented Programming, which is a programming paradigm that uses objects - instances of classes - for designing and organizing code. It is based on several principles that help in creating modular, reusable, and maintainable software. The core concepts of OOP include:")
                st.write("Class: A class is a blueprint or a template for creating objects. It defines a data structure and behavior that the objects will have.")
                st.write("Object: An object is an instance of a class. It encapsulates data (attributes) and the methods (functions) that operate on the data.")
                st.write("Encapsulation: Encapsulation is the bundling of data and the methods that operate on that data into a single unit, i.e., a class. It helps in hiding the internal details of an object and exposing only what is necessary.")
                st.write("Inheritance: Inheritance is a mechanism that allows a new class (subclass or derived class) to inherit the properties and behaviors of an existing class (base class or parent class). It promotes code reusability and establishes a relationship between classes.")
                st.write("Polymorphism: Polymorphism allows objects of different types to be treated as objects of a common type. It enables a single interface to represent different types of objects, making the code more flexible and extensible.")
                st.write("Abstraction: Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors. It allows programmers to focus on the relevant aspects of an object and ignore unnecessary details.")
                st.write("OOPs is widely used in software development because it provides a modular structure that promotes code organization, reusability, and ease of maintenance. Popular programming languages that support OOP include Java, C++, Python, and C#.")


                # Add "Ready to take test again" button
                ready_button_clicked = st.button("Ready to take test again")
                if ready_button_clicked:
                    reset_advanced_section()
                    st.experimental_rerun()  # Restart the test

            elif study_option == "Audio Material":
                st.write("Advanced Audio material goes here.")
                st.title("Advanced of Python")

                # Initialize session state
                current_sentence = st.session_state.get("current_sentence", 0)
                paused = st.session_state.get("paused", False)

                # Load text
                text = '''OOPs stands for Object-Oriented Programming, which is a programming paradigm that uses objects - instances of classes - for designing and organizing code.It is based on several principles that help in creating modular, reusable, and maintainable software.The core concepts of OOP include:Class: A class is a blueprint or a template for creating objects.It defines a data structure and behavior that the objects will have.Object: An object is an instance of a class.It encapsulates data (attributes) and the methods (functions) that operate on the data.Encapsulation: Encapsulation is the bundling of data and the methods that operate on that data into a single unit, i.e., a class.It helps in hiding the internal details of an object and exposing only what is necessary.Inheritance: Inheritance is a mechanism that allows a new class (subclass or derived class) to inherit the properties and behaviors of an existing class (base class or parent class).It promotes code reusability and establishes a relationship between classes.Polymorphism: Polymorphism allows objects of different types to be treated as objects of a common type.It enables a single interface to represent different types of objects, making the code more flexible and extensible.Abstraction: Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors.It allows programmers to focus on the relevant aspects of an object and ignore unnecessary details.OOPs is widely used in software development because it provides a modular structure that promotes code organization, reusability, and ease of maintenance. Popular programming languages that support OOP include Java, C++, Python, and C#.'''

                sentences = text.split('.')

                # Load background music
                background_music_file = r"C:\Users\shilp\OneDrive\Documents\Luminar\Internship\AI Tutor\Music.wav"

                # Play background music
                play_background_music(background_music_file)

                # Display current sentence and control buttons
                st.text(sentences[current_sentence])

                # Pause, Continue, Replay buttons
                col1, col2, col3 = st.columns(3)

                # Pause button
                if col1.button("Pause"):
                    paused = True

                # Continue button
                if col2.button("Continue"):
                    paused = False

                # Replay button
                if col3.button("Replay"):
                    current_sentence = 0  # Reset to the beginning
                    paused = False

                # Check if paused
                if not paused:
                    # Play text-to-speech
                    audio_file_path = text_to_speech(sentences[current_sentence])
                    st.audio(audio_file_path, format='audio/wav')

                    # Increment current sentence
                    current_sentence += 1

                    # # Check if it's the last sentence
                    # if current_sentence == len(sentences):
                    #     stop_background_music()

                # Save session state
                st.session_state.current_sentence = current_sentence
                st.session_state.paused = paused

                # Add "Ready to take test again" button
                ready_button_clicked = st.button("Ready to take test again")
                if ready_button_clicked:
                    stop_background_music()  # Stop the background music
                    reset_advanced_section()
                    st.experimental_rerun()  # Restart the test


if __name__ == "__main__":
    main()