from django.shortcuts import render

# Create your views here.

php_questions = [
    {
        'question': 'What does PHP stand for?',
        'options': ['Personal Home Page', 'Hypertext Preprocessor', 'Private Hypertext Processor', 'Pretext Hypertext Processor'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which function in PHP can be used to get the length of a string?',
        'options': ['len()', 'str_length()', 'strlen()', 'string_length()'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'How do you start a PHP script?',
        'options': ['Using the <?php tag at the beginning and ?> at the end', 'Using the <? tag at the beginning and ?> at the end', 'Using the <?php at the beginning', 'Using the <?php tag at the beginning and no ending tag'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which function in PHP is used to output data to the screen?',
        'options': ['display()', 'print()', 'echo()', 'output()'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'How do you comment a single line in PHP?',
        'options': ['// Comment', '# Comment', '<!-- Comment -->', '/* Comment */'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP superglobal variable is used to retrieve form data after submitting an HTML form?',
        'options': ['$_POST', '$_GET', '$_REQUEST', '$_GLOBAL'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the default file extension for PHP files?',
        'options': ['.php', '.ph', '.html', '.phtml'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP function is used to include a file?',
        'options': ['include()', 'require()', 'insert()', 'inc()'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the correct way to start a PHP block that will allow the output of HTML as well?',
        'options': ['<% ... %>', '<?php ... ?>', '<? ... ?>', '<!php ... !>'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Which operator is used for concatenation in PHP?',
        'options': ['+', '||', '&', '.'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'How do you define a constant in PHP?',
        'options': ['define("MY_CONSTANT", "myvalue")', 'constant("MY_CONSTANT", "myvalue")', 'set_constant("MY_CONSTANT", "myvalue")', 'const MY_CONSTANT = "myvalue"'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which function in PHP is used to check if a variable is an array?',
        'options': ['isArray()', 'checkArray()', 'is_array()', 'arrayCheck()'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which PHP directive is used to set the maximum execution time of a script?',
        'options': ['max_execution_time', 'execution_limit', 'script_timeout', 'timeout_limit'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'In PHP, what does the function `empty()` do?',
        'options': ['Checks if a variable is set', 'Checks if a variable is empty or null', 'Deletes a variable', 'Checks if a file is empty'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'How can you start a session in PHP?',
        'options': ['session_start()', 'start_session()', 'init_session()', 'begin_session()'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP function is used to remove whitespace or other predefined characters from the right side of a string?',
        'options': ['rtrim()', 'trim()', 'clear()', 'removeSpaces()'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP function is used to get the current date and time?',
        'options': ['date()', 'time()', 'datetime()', 'now()'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the PHP function `header()`?',
        'options': ['To create headers for HTML documents', 'To send raw HTTP headers', 'To include external headers in PHP files', 'To format text as headers in PHP'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'How can you convert a string to lowercase in PHP?',
        'options': ['toLower()', 'lowercase()', 'strtolower()', 'caseToLower()'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which PHP operator is used to compare two values but does not consider their data types?',
        'options': ['==', '===', '!=', '!=='],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the function `unlink()` do in PHP?',
        'options': ['Deletes a file', 'Creates a link between files', 'Returns the number of links to a file', 'Checks if a file exists'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'In PHP, how do you access the first element of an array?',
        'options': ['$array[0]', '$array{0}', '$array.first()', '$array->first'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP function is used to create an array?',
        'options': ['make_array()', 'array()', 'create_array()', 'new_array()'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the `foreach` loop in PHP?',
        'options': ['To loop through elements of an array or object', 'To perform a fixed number of iterations', 'To check if a condition is true before executing a block of code', 'To create nested loops'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'How can you access the length of an array in PHP?',
        'options': ['count($array)', 'length($array)', 'sizeOf($array)', 'getLength($array)'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP function is used to open a file for writing?',
        'options': ['open_file()', 'write_file()', 'fopen()', 'read_file()'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What does the `exit()` function do in PHP?',
        'options': ['Closes the PHP interpreter', 'Exits the current loop', 'Terminates script execution', 'Outputs a message and stops script execution'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the `include_once()` function in PHP?',
        'options': ['Includes and evaluates a specified file during script execution', 'Includes a file only once during a script execution', 'Checks if a file exists and includes it if so', 'Includes a file and runs it as a separate process'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'In PHP, how do you declare a variable?',
        'options': ['Using the $ symbol followed by the variable name', 'Using var keyword followed by the variable name', 'Using the declare keyword followed by the variable name', 'Using @ symbol followed by the variable name'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which function is used to redirect the user to a different web page in PHP?',
        'options': ['redirect()', 'header()', 'location()', 'forward()'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'How do you retrieve the size of an uploaded file in PHP?',
        'options': ['$_FILES["file"]["size"]', '$_FILES["file"]["dimensions"]', '$_FILES["file"]["length"]', '$_FILES["file"]["filesize"]'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which PHP function is used to generate a random number?',
        'options': ['rand()', 'random()', 'random_number()', 'generate_random()'],
        'answer': 0,
        'mark': 1
    }
]  



php_questions_intermediate = [
    {
        'question': 'What is the difference between == and === in PHP?',
        'options': ['== is used for value comparison, === is used for value and type comparison', '== is used for assignment, === is used for comparison', '== is used for strict comparison, === is used for loose comparison', '== is used for type conversion, === is used for strict type checking'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Explain the use of the PHP function `implode()` and provide an example.',
        'options': ['It splits a string into an array', 'It joins array elements with a string', 'It reverses the order of array elements', 'It extracts a portion of a string'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the use of PHP sessions? How are they started and destroyed?',
        'options': ['Sessions are used for encrypting data in PHP. They start with session_begin() and end with session_destroy()', 'Sessions are used for storing user data across multiple pages. They start with session_start() and end with session_end()', 'Sessions are used for maintaining stateful information across multiple requests. They start with session_start() and end with session_destroy()', 'Sessions are used for database operations in PHP. They start with session_open() and end with session_close()'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the difference between include and require in PHP.',
        'options': ['There is no difference between include and require', 'include includes a file only if it exists, require terminates the script if the file is not found', 'include includes a file and terminates the script if the file is not found, require includes a file only if it exists', 'include includes a file only if it exists, require terminates the script if the file is not found'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'What is the use of namespaces in PHP?',
        'options': ['To create alias names for functions', 'To organize and group classes, interfaces, functions, and constants', 'To define global constants', 'To define global variables'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the PHP magic methods __construct() and __destruct().',
        'options': ['__construct() is used for class instantiation and __destruct() is used for object destruction', '__construct() is used for object destruction and __destruct() is used for class instantiation', '__construct() is used for static methods and __destruct() is used for dynamic methods', '__construct() is used for object creation and __destruct() is used for object cleanup'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the difference between GET and POST methods in PHP when submitting form data?',
        'options': ['GET method is more secure than POST method', 'POST method appends data to the URL while GET doesn’t', 'GET method is suitable for sensitive data, while POST method is not', 'POST method is suitable for large data, while GET method is limited in data size'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the concept of autoloading in PHP and its relevance in coding.',
        'options': ['Autoloading is a method to automatically include PHP functions', 'Autoloading is used to include files at random', 'Autoloading helps in loading classes when they are needed without explicitly including them', 'Autoloading is a method for including CSS and JavaScript files'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'How does PHP manage sessions across multiple pages and what are the security concerns related to sessions?',
        'options': ['PHP uses cookies to manage sessions; security concerns include session fixation and session hijacking', 'PHP uses server variables to manage sessions; security concerns include XSS and CSRF attacks', 'PHP uses session IDs to manage sessions; security concerns include SQL injection and XSS attacks', 'PHP uses hidden fields to manage sessions; security concerns include cross-site scripting and cross-site request forgery'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Explain the concept of SQL injection and how PHP prevents it.',
        'options': ['SQL injection is a method to inject HTML code into SQL queries; PHP prevents it by sanitizing inputs', 'SQL injection is a technique to inject malicious SQL queries; PHP prevents it by using prepared statements or parameterized queries', 'SQL injection is a method to inject PHP code into SQL databases; PHP prevents it by using encryption techniques', 'SQL injection is a way to bypass PHP security checks; PHP prevents it by using captcha verification'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What are traits in PHP and how do they differ from classes and interfaces?',
        'options': ['Traits are abstract classes in PHP; they differ from interfaces by allowing multiple inheritances', 'Traits are similar to interfaces but can have method implementations; they differ from classes by not being instantiable', 'Traits are language constructs for sharing methods among classes; they differ from classes and interfaces by enabling horizontal code reuse', 'Traits are used for defining constants; they differ from classes by not allowing properties'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the concept of method chaining in PHP with an example.',
        'options': ['Method chaining allows calling multiple methods in a sequence; an example is $object->method1()->method2()->method3()', 'Method chaining is used for calling static methods in PHP; an example is $class::method1()::method2()::method3()', 'Method chaining is a way to call private methods in PHP; an example is $object->method1()::method2()::method3()', 'Method chaining is used to access global methods in PHP; an example is $object->method1()->method2()->method3()::method4()'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the SPL (Standard PHP Library) in PHP? Provide an example of its usage.',
        'options': ['SPL is used for handling HTML elements in PHP; an example is manipulating DOM elements', 'SPL is used for handling exceptions and errors in PHP; an example is catching and handling different types of exceptions', 'SPL is used for handling sessions and cookies in PHP; an example is managing user sessions', 'SPL is used for handling images in PHP; an example is image manipulation and resizing'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of anonymous functions (closures) in PHP and provide an example of their usage.',
        'options': ['Anonymous functions are functions without names and cannot be called directly; an example is $function() {}', 'Anonymous functions are static functions in PHP; an example is static function() {}', 'Anonymous functions are used for defining global functions; an example is global function() {}', 'Anonymous functions are functions without names that can be assigned to variables or passed as arguments; an example is $function = function() {};'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'What are PHP magic constants? Provide examples of their usage.',
        'options': ['Magic constants are reserved words in PHP for defining constants; an example is MAGIC_CONSTANT', 'Magic constants are built-in constants that change their values; an example is __VALUE__', 'Magic constants are predefined constants in PHP that change based on their usage context; examples include __LINE__, __FILE__, and __DIR__', 'Magic constants are constants that can only be accessed by magic methods in PHP; an example is MAGIC_CONSTANT()'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the use of the `PDO` extension in PHP. What are its advantages over `mysql_*` functions?',
        'options': ['PDO is used for connecting PHP with databases; its advantages include simpler syntax and better performance compared to mysql_* functions', 'PDO is used for file handling in PHP; its advantages include direct access to files and improved security over mysql_* functions', 'PDO is used for handling XML data in PHP; its advantages include faster parsing and better compatibility compared to mysql_* functions', 'PDO is used for encryption in PHP; its advantages include stronger encryption algorithms and better performance compared to mysql_* functions'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What are namespaces in PHP? Explain their significance and provide an example.',
        'options': ['Namespaces are used for creating named constants in PHP; their significance includes improved performance and better memory management', 'Namespaces are used for grouping related classes, interfaces, functions, and constants; their significance includes avoiding naming collisions and organizing code', 'Namespaces are used for defining global variables in PHP; their significance includes easier variable access and reduced code complexity', 'Namespaces are used for defining reserved keywords in PHP; their significance includes preventing keyword misuse and improving code readability'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of object serialization in PHP. What is its purpose and how is it implemented?',
        'options': ['Serialization is used for encrypting objects in PHP; it is implemented using serialize() and unserialize() functions', 'Serialization is used for converting objects into a storable format; it is implemented using the json_encode() and json_decode() functions', 'Serialization is used for compressing objects in PHP; it is implemented using gzcompress() and gzuncompress() functions', 'Serialization is used for converting objects into a format that can be stored or transmitted; it is implemented using serialize() and unserialize() functions'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'What is autoloading in PHP? How does it simplify the inclusion of class files?',
        'options': ['Autoloading is a feature for automatically executing scripts in PHP; it simplifies file inclusion by using autoload() function', 'Autoloading is a feature for automatic class file inclusion in PHP; it simplifies file inclusion by loading classes only when needed using spl_autoload_register()', 'Autoloading is a feature for automatically updating PHP configurations; it simplifies file inclusion by using autoupdate() function', 'Autoloading is a feature for handling errors in PHP; it simplifies file inclusion by using autohandle() function'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of method visibility (public, private, protected) in PHP classes.',
        'options': ['Method visibility determines the order of method execution in PHP classes; it defines the priority of method calls', 'Method visibility defines the ability to access and use methods within PHP classes; public allows access from outside the class, private restricts access, and protected allows access within the class and its subclasses', 'Method visibility defines the display of methods in PHP classes; public methods are visible, private methods are hidden, and protected methods are partially visible', 'Method visibility determines the return type of methods in PHP classes; public returns values to the calling script, private doesn’t return values, and protected partially returns values'],
        'answer': 1,
        'mark': 1
    },
     {
        'question': 'Explain the difference between `require_once` and `include_once` in PHP.',
        'options': ['There is no difference between require_once and include_once', 'require_once includes a file multiple times, include_once includes a file only once', 'require_once terminates the script if the file is not found, include_once doesn’t', 'require_once and include_once both include a file only once, but require_once is used for PHP files and include_once is used for HTML files'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What are anonymous classes in PHP? Provide an example of their usage.',
        'options': ['Anonymous classes are classes without names; they cannot be instantiated', 'Anonymous classes are classes that can only be instantiated once; they are useful for creating single instances', 'Anonymous classes are classes without predefined properties; they are defined using $class = new class {}', 'Anonymous classes are dynamically created classes without a specific name; they are defined inline using new class {}'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the `__autoload` function in PHP. How does it relate to class autoloading?',
        'options': ['__autoload is a magic function in PHP used to load classes manually; it is used for preloading classes before instantiation', '__autoload is used to automatically include classes when they are instantiated; it is a predecessor to class autoloading', '__autoload is a deprecated function in PHP; it was used for class autoloading before the introduction of spl_autoload_register()', '__autoload is used for defining global classes in PHP; it registers classes for global access'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the concept of late static binding in PHP and provide an example of its usage.',
        'options': ['Late static binding refers to static method calls that happen later in the code execution; an example is using $this->staticMethod()', 'Late static binding refers to resolving static method calls at runtime based on the context of the calling code; an example is using static::staticMethod()', 'Late static binding refers to delayed method execution; an example is using late_static_bind::staticMethod()', 'Late static binding refers to deferred method invocation; an example is using static->staticMethod()'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the `spl_autoload_register()` function in PHP? How does it work?',
        'options': ['spl_autoload_register() is used for defining autoload functions in PHP; it works by automatically loading classes when instantiated', 'spl_autoload_register() is used for registering multiple autoload functions in PHP; it works by allowing custom autoload functions to be queued', 'spl_autoload_register() is used for registering classes in PHP; it works by defining namespaces for class loading', 'spl_autoload_register() is used for registering constants in PHP; it works by defining constant autoloaders'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of dependency injection in PHP. How does it enhance code flexibility and maintainability?',
        'options': ['Dependency injection is a technique to inject database dependencies into PHP classes; it enhances code performance and scalability', 'Dependency injection is a design pattern used to resolve dependencies outside the class; it enhances code flexibility by allowing easier changes and testing', 'Dependency injection is a method to inject variables directly into functions; it enhances code maintainability by reducing global dependencies', 'Dependency injection is a way to inject HTML code into PHP classes; it enhances code readability and simplicity'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of middleware in PHP frameworks (e.g., Laravel, Symfony). How is middleware used in web applications?',
        'options': ['Middleware is used for handling errors in PHP frameworks; it intercepts requests and responses to manage errors', 'Middleware is used for implementing caching mechanisms in PHP frameworks; it caches data to improve performance', 'Middleware is used for request and response manipulation in PHP frameworks; it intercepts HTTP requests and responses to perform tasks before and after handling', 'Middleware is used for managing sessions in PHP frameworks; it intercepts user sessions to store and retrieve data'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the concept of method overloading and method overriding in PHP. Provide examples for each.',
        'options': ['Method overloading allows multiple methods with the same name but different parameters; method overriding allows redefining methods in child classes', 'Method overloading allows changing method names dynamically; method overriding allows modifying inherited methods in the same class', 'Method overloading allows calling private methods from parent classes; method overriding allows calling public methods from child classes', 'Method overloading allows defining methods outside classes; method overriding allows modifying built-in PHP functions'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Explain the concept of PSR standards in PHP. What are the advantages of adhering to these standards?',
        'options': ['PSR standards define programming language syntax in PHP; adhering to these standards improves code performance and execution speed', 'PSR standards define coding standards and recommendations in PHP; adhering to these standards enhances code readability and interoperability across frameworks', 'PSR standards define PHP extension libraries; adhering to these standards improves backward compatibility and maintains PHP versions', 'PSR standards define error handling mechanisms in PHP; adhering to these standards reduces code complexity and debugging time'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of traits conflicts in PHP. How can conflicts between traits be resolved?',
        'options': ['Traits conflicts occur when using multiple traits with the same name; conflicts can be resolved by excluding one of the traits', 'Traits conflicts happen when traits have conflicting methods; conflicts can be resolved by renaming methods in the conflicting traits', 'Traits conflicts arise when traits define conflicting properties or methods; conflicts can be resolved by explicitly using the aliasing feature or overriding methods', 'Traits conflicts occur due to namespaces clashes; conflicts can be resolved by changing namespace names'],
        'answer': 2,
        'mark': 1
    }
]


php_advanced_questions = [
    {
        'question': 'Explain the purpose and benefits of using namespaces in PHP.',
        'options': [
            'Namespaces in PHP provide a way to group logically related classes, interfaces, functions, and constants. They help in avoiding naming conflicts, organizing code, and enhancing code readability.',
            'Namespaces are primarily used for creating aliases to access long class names.',
            'Namespaces are used only for organizing classes, not functions or constants.',
            'There are no significant benefits to using namespaces in PHP.'
        ],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Discuss the differences between sessions and cookies in PHP.',
        'options': [
            'Sessions store data on the server side, while cookies store data on the client side.',
            'Sessions are more secure than cookies as session data is stored on the server.',
            'Cookies have a limited storage capacity compared to sessions.',
            'Both sessions and cookies are used interchangeably with no significant differences.'
        ],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the __construct method in PHP classes and its significance in object-oriented programming.',
        'options': [
            '__construct is used for creating multiple instances of a class.',
            '__construct is a magic method called automatically when an object is created, allowing for initialization tasks.',
            '__construct is used for defining static methods in a class.',
            'There is no such method as __construct in PHP.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Describe the usage and advantages of using traits in PHP.',
        'options': [
            'Traits are used for defining only properties in PHP classes.',
            'Traits allow for multiple inheritance in PHP classes.',
            'Traits are used only for defining abstract classes.',
            'There are no advantages to using traits in PHP.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the PDO extension in PHP and its role in database interaction.',
        'options': [
            'PDO is used for creating HTML templates in PHP.',
            'PDO stands for Personal Data Objects and is used for storing user-specific information.',
            'PDO is a database access layer providing a uniform method of access to multiple databases, enhancing security and portability.',
            'PDO is used for creating dynamic objects in PHP.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the concept of anonymous functions (closures) in PHP and provide an example of their usage.',
        'options': [
            'Anonymous functions are not supported in PHP.',
            'Anonymous functions are used only for defining class methods.',
            'Anonymous functions (closures) allow the creation of functions without a specified name. They are useful for tasks like defining callback functions or for creating one-time-use functions.',
            'Anonymous functions are used exclusively for error handling.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Discuss the differences between the == and === operators in PHP.',
        'options': [
            'The == operator performs a type-strict comparison, whereas === performs a loose comparison.',
            'Both == and === operators are used interchangeably.',
            'The == operator performs a loose comparison, whereas === performs a type-strict comparison.',
            'There is no difference between the == and === operators.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the use of the spl_autoload_register function in PHP and its significance in autoloading classes.',
        'options': [
            'spl_autoload_register is used for registering predefined autoloader functions in PHP.',
            'spl_autoload_register is used for defining class methods in PHP.',
            'spl_autoload_register is used to register multiple autoloader functions, allowing for flexible class autoloading.',
            'There is no function named spl_autoload_register in PHP.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the trait_exists function in PHP, and how is it used?',
        'options': [
            'trait_exists is used to check if a class exists in PHP.',
            'trait_exists is used to check if a trait exists in PHP.',
            'trait_exists is used to define a new trait in PHP.',
            'trait_exists is used to check if a class uses a specific trait in PHP.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the benefits of using the filter_var function in PHP for input validation.',
        'options': [
            'filter_var is used only for converting variables to a specified datatype.',
            'filter_var is used for output sanitization, not input validation.',
            'filter_var is a versatile function used for validating and sanitizing input data based on various filters, improving security by preventing common vulnerabilities.',
            'filter_var is used exclusively for validating email addresses.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the concept of anonymous classes in PHP and provide an example of their usage.',
        'options': [
            'Anonymous classes are not supported in PHP.',
            'Anonymous classes can only be used in conjunction with interfaces.',
            'Anonymous classes allow the creation of simple class instances without explicitly defining a class name. They are useful for quick, one-off instances where a full class definition is unnecessary.',
            'Anonymous classes are used exclusively for defining abstract classes.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Discuss the purpose and advantages of using the try, catch, and finally blocks in PHP exception handling.',
        'options': [
            'The try block is optional in exception handling.',
            'The catch block is used to specify the code to be executed when an exception is thrown, and the finally block is used to handle normal flow control after the try-catch blocks.',
            'The try block is used for specifying the code to be executed when an exception is thrown, and the catch block is used for normal flow control after the try-catch blocks.',
            'The finally block is optional in exception handling.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the trait_exists function in PHP, and how is it used?',
        'options': [
            'trait_exists is used to check if a class exists in PHP.',
            'trait_exists is used to check if a trait exists in PHP.',
            'trait_exists is used to define a new trait in PHP.',
            'trait_exists is used to check if a class uses a specific trait in PHP.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Describe the significance and usage of the array_column function in PHP.',
        'options': [
            'array_column is used for extracting a column from an array, useful for working with database results.',
            'array_column is used for sorting an array based on a specific column.',
            'array_column is used for merging multiple arrays into a single array.',
            'array_column is used for creating a multi-dimensional array.'
        ],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the array_map function in PHP and provide an example of its usage.',
        'options': [
            'array_map is used for creating a map of key-value pairs from an array.',
            'array_map is used for mapping a function to all elements in one or more arrays, producing a new array.',
            'array_map is used for mapping a function only to associative arrays.',
            'array_map is used exclusively for mathematical operations on arrays.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the concept of traits conflicts in PHP and how they can be resolved.',
        'options': [
            'Traits conflicts occur when two traits have methods with the same name in a class, and PHP resolves it automatically by choosing one method over the other.',
            'Traits conflicts can never occur in PHP as traits are designed to prevent naming conflicts.',
            'Traits conflicts are resolved by renaming methods in the conflicting traits.',
            'Traits conflicts are resolved by using the insteadof and as operators in the class using the conflicting traits.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Discuss the purpose and usage of the yield keyword in PHP, especially in the context of generators.',
        'options': [
            'The yield keyword is used for terminating the execution of a function in PHP.',
            'The yield keyword is used for defining constants in PHP.',
            'The yield keyword is used in the context of generators to pause the execution of a function, allowing the generator to produce a sequence of values lazily.',
            'The yield keyword is used for handling exceptions in PHP.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the array_diff function in PHP and how it is used.',
        'options': [
            'array_diff is used for finding the difference between two arrays by comparing their keys.',
            'array_diff is used for finding the common elements between two arrays.',
            'array_diff is used for finding the difference between two arrays by comparing their values.',
            'array_diff is used exclusively for sorting arrays.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Describe the significance and usage of the array_filter function in PHP.',
        'options': [
            'array_filter is used for filtering an array based on specific key-value pairs.',
            'array_filter is used for filtering an array by applying a user-defined function to each element.',
            'array_filter is used for merging multiple arrays into a single array.',
            'array_filter is used for creating a multi-dimensional array.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Discuss the purpose and advantages of using the json_encode and json_decode functions in PHP for working with JSON data.',
        'options': [
            'json_encode and json_decode functions are not used for working with JSON data in PHP.',
            'json_encode is used for converting a PHP array into a JSON string, and json_decode is used for converting a JSON string into a PHP array, facilitating the interchange of data between PHP and JavaScript.',
            'json_encode is used for decoding JSON data, and json_decode is used for encoding JSON data.',
            'json_encode and json_decode functions are used exclusively for validating JSON data.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the array_reduce function in PHP.',
        'options': [
            'array_reduce is used for flattening multi-dimensional arrays in PHP.',
            'array_reduce is used for reducing an array to a single value using a callback function.',
            'array_reduce is used for merging multiple arrays into a single array.',
            'array_reduce is used exclusively for sorting arrays.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Discuss the concept of dependency injection in PHP and how it contributes to better code design.',
        'options': [
            'Dependency injection is not applicable in PHP.',
            'Dependency injection is used only for handling database connections.',
            'Dependency injection is a design pattern in PHP where dependencies are injected into a class rather than being created within the class. It improves code maintainability, testability, and flexibility.',
            'Dependency injection is used exclusively for handling form submissions.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and advantages of using the filter_input and filter_input_array functions in PHP for input validation.',
        'options': [
            'filter_input and filter_input_array functions are not used for input validation in PHP.',
            'filter_input is used for encoding user input, and filter_input_array is used for decoding input.',
            'filter_input is used for filtering external variables and filter_input_array is used for filtering an array of external variables, providing a convenient way for input validation in PHP.',
            'filter_input and filter_input_array functions are used exclusively for handling file uploads.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Describe the purpose and usage of the assert function in PHP for debugging and testing.',
        'options': [
            'assert is used for defining custom assertions in PHP.',
            'assert is used for including external files in PHP.',
            'assert is used for executing JavaScript code within PHP.',
            'assert is used for debugging and testing by evaluating an assertion, terminating the script if the assertion is false.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the preg_match function in PHP for pattern matching with regular expressions.',
        'options': [
            'preg_match is used for validating email addresses in PHP.',
            'preg_match is used for searching and replacing text in PHP.',
            'preg_match is used for comparing two strings in PHP.',
            'preg_match is used for performing pattern matching with regular expressions in PHP, allowing for complex string manipulations.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the header function in PHP for HTTP header manipulation.',
        'options': [
            'header is used for defining constants in PHP.',
            'header is used for including external files in PHP.',
            'header is used for sending raw HTTP headers in PHP, allowing control over various aspects of HTTP responses such as redirection and caching.',
            'header is used exclusively for handling session data.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Discuss the role of the unlink function in PHP and how it is used for file manipulation.',
        'options': [
            'unlink is used for creating symbolic links in PHP.',
            'unlink is used for creating backup copies of files in PHP.',
            'unlink is used for deleting files in PHP.',
            'unlink is used exclusively for renaming files.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the file_get_contents function in PHP for reading files.',
        'options': [
            'file_get_contents is used exclusively for writing content to files in PHP.',
            'file_get_contents is used for creating directories in PHP.',
            'file_get_contents is used for reading the contents of a file into a string in PHP.',
            'file_get_contents is used for checking if a file exists in PHP.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Describe the significance and usage of the set_exception_handler function in PHP for custom exception handling.',
        'options': [
            'set_exception_handler is used for registering predefined exception handlers in PHP.',
            'set_exception_handler is used for defining class methods in PHP.',
            'set_exception_handler is used for setting a user-defined function to handle uncaught exceptions in PHP.',
            'set_exception_handler is used exclusively for handling syntax errors.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the purpose and usage of the array_reverse function in PHP.',
        'options': [
            'array_reverse is used for sorting an array in PHP.',
            'array_reverse is used for reversing the order of elements in an array in PHP.',
            'array_reverse is used for removing duplicate values from an array.',
            'array_reverse is used exclusively for filtering arrays.'
        ],
        'answer': 1,
        'mark':1
    },
]


from exam.models import TestResult
import random
from django.views.generic import TemplateView

def basicphp_section(request):
    random_questions = request.session.get('random_questionsphp')
    print(random_questions)
    if not random_questions:
        random_questions = random.sample(php_questions, 10)
        request.session['random_questionsphp'] = random_questions
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
                print(user_answer)
                if clicked_button:
                    clicked_buttons[i] = True
                    
                    correct_answer_index = question_data['answer'] 
                    print(correct_answer_index)
                    correct_answer = question_data['options'][correct_answer_index ]
                    print(correct_answer)
                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            # TestResult.objects.create(user=request.user, score=total_marks,section="BasicPHP")
        if total_marks :
            test_result = TestResult.objects.filter(user=request.user.id,section="BasicPHP").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks,section="BasicPHP")
            return render(request, 'basic_php.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'basic_php.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'basic_php.html', {'random_questions': random_questions})


# class Basiclearn(TemplateView):
#     template_name='basic_learnhtml.html'



def intermediatephp_section(request):
    random_questions = request.session.get('random_questions_intermediatephp')
    print(random_questions)
    if not random_questions:
        random_questions = random.sample(php_questions_intermediate, 10)
        request.session['random_questions_intermediatephp'] = random_questions
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
                # print(user_answer)
                if clicked_button:
                    clicked_buttons[i] = True
                    
                    correct_answer_index = question_data['answer'] 
                    # print(correct_answer_index)
                    correct_answer = question_data['options'][correct_answer_index ]
                    # print(correct_answer)
                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            # TestResult.objects.create(user=request.user, score=total_marks,section="IntermediatePHP")
        if total_marks :
            test_result = TestResult.objects.filter(user=request.user,section="IntermediatePHP").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks,section="IntermediatePHP")
            return render(request, 'intermediate_php.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'intermediate_php.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'intermediate_php.html', {'random_questions': random_questions})


class Intermediatelearn(TemplateView):
    template_name='intermediatephp_learn.html'



def advancedphp_section(request):
    random_questions = request.session.get('random_questions_advancedphp')
    print(random_questions)
    if not random_questions:
        random_questions = random.sample(php_advanced_questions, 10)
        request.session['random_questions_advancedphp'] = random_questions
    # else:
    #     random.shuffle(random_questions)
    
    if request.method == 'POST':
        total_marks = 0
        clicked_buttons = request.session.get('clicked_htmlbuttons', [False] * len(random_questions))
        finish_button_clicked = request.session.get('finish_htmlbutton_clicked', False)

        if not finish_button_clicked:
            for i, question_data in enumerate(random_questions):
                user_answer = request.POST.get(f"question_{i + 1}", "")
                clicked_button = request.POST.get("check_answers", "")
                print(user_answer)
                if clicked_button:
                    clicked_buttons[i] = True
                    
                    correct_answer_index = question_data['answer'] 
                    print(correct_answer_index)
                    correct_answer = question_data['options'][correct_answer_index ]
                    print(correct_answer)
                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            # TestResult.objects.create(user=request.user, score=total_marks,section="AdvancedPHP")
        if total_marks :
            test_result = TestResult.objects.filter(user=request.user,section="AdvancedPHP").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks,section="AdvancedPHP")
            return render(request, 'advanced_php.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'advanced_php.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'advanced_php.html', {'random_questions': random_questions})


# class Intermediatelearn(TemplateView):
#     template_name='advanced_htmlhtml_learn.html'

class phplearning_page(TemplateView):
    template_name="basic_learnphp.html"

class phpinter_learn(TemplateView):
    template_name="intermediatephp_learn.html"
    

class phplearnadv(TemplateView):
    template_name="advlearn_php.html"
    
def phpintro(request):
    return render(request, "phpintro.html")