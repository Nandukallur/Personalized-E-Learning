from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import FeedbackForm, ProjectUploadForm
# Create your views here.

html_questions = [
    {
        'question': 'What does HTML stand for?',
        'options': ['Hyper Trainer Marking Language', 'Hyper Text Markup Language', 'Hyper Text Managing Language',
                    'Hyper Text Marketing Language'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Which tag is used to create a hyperlink in HTML?',
        'options': ['<a>', '<b>', '<p>', '<li>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which HTML tag is used to define an unordered list?',
        'options': ['<ol>', '<li>', '<ul>', '<p>'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What does the HTML attribute "href" define?',
        'options': ['The hypertext reference of the link', 'The header of the page', 'The heading of the link',
                    'The hierarchy of the page'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which HTML element is used for creating a line break?',
        'options': ['<lb>', '<nl>', '<br>', '<break>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the acronym HTML represent?',
        'options': ['Hyperlinks and Text Markup Language', 'Hyper Text Markup Language', 'Hyper Text Model Language',
                    'High Text Markup Language'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'In HTML, which attribute is used to provide a tooltip for an element?',
        'options': ['tooltip', 'hint', 'info', 'title'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Which HTML tag is used for creating an image?',
        'options': ['<image>', '<img>', '<picture>', '<imgsrc>'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the HTML element used to define important text?',
        'options': ['<important>', '<em>', '<strong>', '<bold>'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which HTML tag is used to define a table row?',
        'options': ['<tr>', '<td>', '<table-row>', '<row>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the correct HTML for inserting a comment?',
        'options': ['<!--This is a comment-->', '<?--This is a comment-->', '<!---This is a comment---!>',
                    '<#This is a comment#>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which tag is used to create a clickable button in HTML?',
        'options': ['<btn>', '<click>', '<input>', '<button>'],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Which tag is used to define the header of a page in HTML?',
        'options': ['<header>', '<head>', '<h1>', '<title>'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML <meta> tag?',
        'options': ['To define metadata about an HTML document', 'To display images in the browser',
                    'To define a hyperlink', 'To format text'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which attribute is used to provide additional information about an element for user interaction?',
        'options': ['data-info', 'alt', 'tooltip', 'data-extra'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What is the correct HTML for creating a hyperlink?',
        'options': ['<a href="http://www.example.com">Click here</a>',
                    '<link href="http://www.example.com">Click here</link>',
                    '<href>http://www.example.com</href>Click here</a>',
                    '<a link="http://www.example.com">Click here</a>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which attribute is used in the <img> tag to specify an alternate text for an image?',
        'options': ['alt', 'title', 'src', 'link'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML <aside> tag represent?',
        'options': ['A secondary header', 'An image gallery', 'A section of content aside from the main content',
                    'An important section'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which HTML tag is used to create an ordered list?',
        'options': ['<ul>', '<li>', '<ol>', '<dt>'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What does the HTML <nav> tag define?',
        'options': ['An area of navigation links', 'A new webpage', 'A navigation bar',
                    'A section to input navigation commands'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Which attribute in the <script> tag specifies an external file containing a JavaScript code?',
        'options': ['file', 'src', 'link', 'external'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What does the HTML <hr> tag represent?',
        'options': ['A horizontal line', 'A highlighted text', 'A header', 'A hyperlink'],
        'answer': 0,
        'mark': 1
    },
]

html_intermediate_questions = [
    {
        'question': 'What is the purpose of the HTML5 <canvas> element?',
        'options': ['To draw graphics, animations, and other visual images on the fly using JavaScript',
                    'To display a gallery of images', 'To embed audio files in a webpage',
                    'To create hyperlinks between web pages'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML5 <article> tag represent?',
        'options': ['An external resource', 'An independent piece of content that can stand alone',
                    'A list of articles', 'A footer section'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML5 <section> tag?',
        'options': ['To define a section of content within a document', 'To create a hyperlink',
                    'To specify a footer section', 'To insert a video'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'In HTML, which tag is used for grouping and applying styles to inline elements?',
        'options': ['<div>', '<span>', '<section>', '<style>'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What does the HTML <figure> tag represent?',
        'options': ['An important piece of content', 'A multimedia element, such as an image or video, with a caption',
                    'A link to a separate document', 'A navigation bar'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML <details> tag?',
        'options': ['To define a list of details', 'To specify a summary of a document',
                    'To create an accordion-like widget', 'To define the structure of a table'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which HTML5 attribute is used to provide additional information about an element?',
        'options': ['extra-info', 'aria-label', 'data-info', 'tooltip'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What does the HTML <time> tag represent?',
        'options': ['A clock widget', 'A block of code', 'A specific period in time or date', 'A timer'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which HTML5 attribute is used to specify the main content of a document?',
        'options': ['main', 'content', 'primary', 'role'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML5 <progress> element?',
        'options': ['To display the progress of a file download', 'To create a progress bar',
                    'To track user interactions on a webpage', 'To show the completion of a form'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML <footer> tag?',
        'options': ['To define the footer section of a document or a section',
                    'To create a section at the bottom of the page for links', 'To insert a footer image',
                    'To highlight important content at the bottom'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the role of the HTML5 <header> tag?',
        'options': ['To define the introductory content at the beginning of a document or section',
                    'To add a header image to the webpage', 'To create a navigation bar', 'To create a footer'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML5 <nav> tag represent?',
        'options': ['A section for navigation links', 'A list of articles', 'An external resource',
                    'A multimedia element'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML <abbr> tag?',
        'options': ['To define an abbreviation or an acronym', 'To create a hyperlink', 'To specify an external link',
                    'To highlight important text'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML <blockquote> tag indicate?',
        'options': ['An important block of text', 'A code snippet', 'A quotation from another source',
                    'A highlighted paragraph'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Which HTML element is used to create a dropdown list?',
        'options': ['<select>', '<drop>', '<list>', '<dropdown>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML <cite> tag represent?',
        'options': ['A reference to a citation or creative work', 'A highlighted text', 'A block of code',
                    'An emphasized text'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'In HTML, what is the function of the <kbd> tag?',
        'options': ['To define keyboard input', 'To highlight text', 'To insert a hyperlink',
                    'To display a code snippet'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which HTML5 element is used to define an area within a page where users can input data?',
        'options': ['<input>', '<dataentry>', '<form>', '<textbox>'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML5 <output> tag?',
        'options': ['To display the output of a calculation or script', 'To create a summary of a document',
                    'To show a list of outputs', 'To generate a footer section'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML <datalist> element define?',
        'options': ['A list of predefined options for input controls', 'A section for displaying data',
                    'A dropdown list for dates', 'A list of data sources'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML5 <mark> tag represent?',
        'options': ['An important section', 'A highlighted text or section', 'A link to related content',
                    'A block of code'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'In HTML, what is the role of the <fieldset> tag?',
        'options': ['To group related form elements and their labels', 'To define a footer',
                    'To create a navigation section', 'To display a set of images'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML5 <aside> element?',
        'options': ['To represent additional content that is related to the main content',
                    'To define an external resource', 'To insert a sidebar navigation', 'To display a footer section'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which HTML tag is used for semantic inline markup?',
        'options': ['<div>', '<span>', '<article>', '<header>'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML5 <figcaption> tag?',
        'options': ['To define a figure in a document', 'To add a caption to an image or figure',
                    'To create a footer section', 'To highlight important text'],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'What does the HTML <s> tag indicate?',
        'options': ['An important piece of content', 'A highlighted text', 'A strikethrough text', 'A blockquote'],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'What is the purpose of the HTML5 <time> element with datetime attribute?',
        'options': ['To represent a specific date and time', 'To create a countdown timer', 'To display the time zone',
                    'To indicate a past date'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Which HTML tag is used for indicating importance within content?',
        'options': ['<strong>', '<important>', '<emphasis>', '<important>'],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'What does the HTML5 <meter> tag represent?',
        'options': ['A measurement within a defined range', 'A unit of measurement', 'A countdown timer',
                    'A progress bar'],
        'answer': 0,
        'mark': 1
    }
]

html_advanced_questions = [
    {
        'question': 'Explain the benefits of using HTML5 semantic elements over traditional <div> and <span> elements in web development.',
        'options': [
            'Better structure, clarity, and meaning to the content.',
            'Used only for specific design purposes.',
            'Less compatible with modern browsers.',
            'No significant benefits over <div> and <span> elements.'
        ],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Discuss the importance of the HTML5 <time> element in displaying date and time information on webpages.',
        'options': [
            'Used for displaying date and time together.',
            'Creates countdown timers.',
            'Embeds multimedia content.',
            'Represents a specific date or time with styling options.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <progress> element in form design and user experience.',
        'options': [
            'Displays a list of tasks.',
            'Creates loading animations.',
            'Styles form elements.',
            'Represents the progress of a task or process.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Describe the usage of the HTML5 <datalist> element in enhancing user input within forms.',
        'options': [
            'Creates dynamic form validations.',
            'Stores data submitted through forms.',
            'Creates data tables within forms.',
            'Provides a predefined list of options for input controls.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <details> and <summary> elements.',
        'options': [
            'Used for creating dropdown menus.',
            'Represents metadata about a document.',
            'Defines a disclosure widget from which the user can obtain additional information.',
            'Used for embedding audio and video content.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Discuss the significance of the HTML5 <figure> and <figcaption> elements in web design.',
        'options': [
            'Used for creating tables within webpages.',
            'Defines the structure of an HTML document.',
            'Represents content such as images with a caption or legend.',
            'Specifies a grouping content element.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the role of the HTML5 <canvas> element in web development.',
        'options': [
            'Used for creating responsive layouts.',
            'Represents a container for external content or embedded applications.',
            'Provides a way to draw graphics, render images, or create animations on the fly.',
            'Defines a section in a document.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Describe the usage of the HTML5 <article> element in structuring content.',
        'options': [
            'Represents a sidebar or "aside" content in a document.',
            'Defines a header for a document or a section.',
            'Represents a self-contained piece of content that could be distributed and reused independently.',
            'Specifies the main content of a document.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the significance of the HTML5 <nav> element and its role in website navigation.',
        'options': [
            'Represents a section in a document with content that is tangentially related to the content around the <nav> element.',
            'Used for defining the main header of a document or a section.',
            'Represents a container for metadata or tag-like labels.',
            'Defines a navigation menu or links to other pages or resources.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the role of the HTML5 <main> element in structuring web content.',
        'options': [
            'Represents a secondary or sidebar content in a document.',
            'Defines a footer for a document or a section.',
            'Represents the main content of a document, excluding headers, footers, and sidebars.',
            'Specifies a navigation menu within a document.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Discuss the purpose of the HTML5 <mark> element in highlighting text.',
        'options': [
            'Used for creating custom fonts in web design.',
            'Represents a small print or fine print text.',
            'Specifies a navigation link.',
            'Highlights or marks portions of text for reference or user attention.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the significance of the HTML5 <abbr> element and its usage.',
        'options': [
            'Used for creating abbreviations in web design.',
            'Represents an acronym in a document.',
            'Specifies a navigation link.',
            'Represents an abbreviation or acronym with optional expansion text.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Describe the usage of the HTML5 <cite> element in citing references.',
        'options': [
            'Used for creating citations and bibliographies.',
            'Represents a citation or reference in a document.',
            'Specifies a container for metadata or tag-like labels.',
            'Defines a section in a document with content that is tangentially related to the content around the <cite> element.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <details> and <summary> elements.',
        'options': [
            'Used for creating dropdown menus.',
            'Represents metadata about a document.',
            'Defines a disclosure widget from which the user can obtain additional information.',
            'Used for embedding audio and video content.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the usage of the HTML5 <blockquote> element and its significance in structuring content.',
        'options': [
            'Used for creating inline quotes within a paragraph.',
            'Represents a container for metadata or tag-like labels.',
            'Defines a block-level quotation in a document.',
            'Specifies a navigation link.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Discuss the purpose of the HTML5 <address> element in web development.',
        'options': [
            'Represents an email address in a document.',
            'Defines a container for navigation links.',
            'Specifies a footer for a document or a section.',
            'Represents the contact information for the nearest ancestor or article element.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the role of the HTML5 <kbd> element in displaying user input.',
        'options': [
            'Used for creating keyboard shortcuts in web design.',
            'Represents a small print or fine print text.',
            'Specifies a navigation link.',
            'Defines text that the user typically enters from a keyboard.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Describe the usage of the HTML5 <samp> element and its significance in displaying sample output.',
        'options': [
            'Represents a sample or quoted output in a document.',
            'Specifies a container for metadata or tag-like labels.',
            'Defines a section in a document with content that is tangentially related to the content around the <samp> element.',
            'Used for creating responsive layouts.'
        ],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <pre> element in preserving whitespace and line breaks.',
        'options': [
            'Defines a container for navigation links.',
            'Used for creating inline quotes within a paragraph.',
            'Preserves both spaces and line breaks in the text.',
            'Specifies a navigation link.'
        ],
        'answer': 2,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <code> element and its role in displaying inline code snippets.',
        'options': [
            'Defines a container for navigation links.',
            'Represents code text in a document.',
            'Specifies a navigation link.',
            'Used for creating inline quotes within a paragraph.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Discuss the significance of the HTML5 <dfn> element in defining terms.',
        'options': [
            'Defines a section in a document with content that is tangentially related to the content around the <dfn> element.',
            'Used for creating keyboard shortcuts in web design.',
            'Represents a container for navigation links.',
            'Represents the defining instance of a term.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the usage of the HTML5 <var> element in representing variables.',
        'options': [
            'Represents a sample or quoted output in a document.',
            'Used for creating keyboard shortcuts in web design.',
            'Specifies a navigation link.',
            'Represents the name of a variable in a programming context.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Describe the purpose of the HTML5 <ruby> and <rt> elements in displaying ruby annotations.',
        'options': [
            'Defines a container for navigation links.',
            'Represents code text in a document.',
            'Used for creating inline quotes within a paragraph.',
            'Represents base text and ruby text for annotations in East Asian typography.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the role of the HTML5 <ins> and <del> elements in indicating changes in text.',
        'options': [
            'Defines a container for navigation links.',
            'Represents a container for metadata or tag-like labels.',
            'Specifies a navigation link.',
            'Represents inserted and deleted text in a document.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <bdi> element in handling bidirectional text.',
        'options': [
            'Isolates text with different directionality.',
            'Defines a section in a document.',
            'Represents navigation links.',
            'Handles keyboard shortcuts in web design.'
        ],
        'answer': 0,
        'mark': 1
    },
    {
        'question': 'Discuss the significance of the HTML5 <wbr> element and its usage.',
        'options': [
            'Specifies navigation links.',
            'Creates inline quotes within a paragraph.',
            'Represents sample or quoted output.',
            'Indicates word break opportunities in text.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Explain the role of the HTML5 <time> element in representing dates and times.',
        'options': [
            'Defines navigation links.',
            'Creates inline quotes.',
            'Represents progress of tasks or processes.',
            'Represents specific dates or times with styling.'
        ],
        'answer': 3,
        'mark': 1
    },
    {
        'question': 'Describe the usage of the HTML5 <abbr> element in providing abbreviations or acronyms.',
        'options': [
            'Specifies navigation links.',
            'Creates abbreviations in web design.',
            'Represents metadata or tag-like labels.',
            'Represents abbreviations or acronyms.'
        ],
        'answer': 1,
        'mark': 1
    },
    {
        'question': 'Explain the purpose of the HTML5 <cite> element and its role in citing references.',
        'options': [
            'Creates citations and bibliographies.',
            'Defines navigation links.',
            'Represents email addresses.',
            'Represents citations or references.'
        ],
        'answer': 0,
        'mark': 1
    },

]

from exam.models import TestResult
import random
from django.views.generic import TemplateView
from accounts.models import CustUser


def basichtml_section(request):
    random_questions = request.session.get('random_questionshtml')
    print(random_questions)
    if not random_questions:
        random_questions = random.sample(html_questions, 10)
        request.session['random_questionshtml'] = random_questions
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
                    correct_answer = question_data['options'][correct_answer_index]
                    print(correct_answer)
                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            # TestResult.objects.create(user=request.user, score=total_marks,section="BasicHTML")
        if total_marks:
            test_result = TestResult.objects.filter(user=request.user.id, section="BasicHTML").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                user_instance = CustUser.objects.get(id=request.user.id)  # Assuming request.user is the user ID
                TestResult.objects.create(user=user_instance, score=total_marks, section="BasicHTML")
            return render(request, 'basic_html.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'basic_html.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'basic_html.html', {'random_questions': random_questions})


def intermediatehtml_section(request):
    scores=TestResult.objects.filter(user=request.user)
    print(scores)
    random_questions = request.session.get('random_questions_intermediatehtml')

    if not random_questions:
        random_questions = random.sample(html_intermediate_questions, 10)
        request.session['random_questions_intermediatehtml'] = random_questions
    # else:

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
                    correct_answer = question_data['options'][correct_answer_index]
                    # print(correct_answer)
                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            # TestResult.objects.create(user=request.user, score=total_marks,section="IntermediateHTML")
        if total_marks:
            test_result = TestResult.objects.filter(user=request.user, section="IntermediateHTML").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks, section="IntermediateHTML")
            return render(request, 'intermediate_html.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'intermediate_html.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'intermediate_html.html', {'random_questions': random_questions,'score':scores})

@login_required
def advancedhtml_section(request):
    scores = TestResult.objects.filter(user=request.user)
    random_questions = request.session.get('random_questions_advancedhtml')
    print(random_questions)
    if not random_questions:
        random_questions = random.sample(html_advanced_questions, 10)
        request.session['random_questions_advancedhtml'] = random_questions
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
                    correct_answer = question_data['options'][correct_answer_index]
                    print(correct_answer)
                    if user_answer == correct_answer:
                        total_marks += question_data['mark']
                        request.session['total_marks'] = total_marks
            request.session['clicked_buttons'] = clicked_buttons
            max_marks = sum(question_data['mark'] for question_data in random_questions)
            percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
            print(total_marks)
            # TestResult.objects.create(user=request.user, score=total_marks,section="AdvancedHTML")
        if total_marks:
            test_result = TestResult.objects.filter(user=request.user, section="AdvancedHTML").first()
            if test_result:
                if total_marks > test_result.score:
                    test_result.score = total_marks
                    test_result.save()
            else:
                TestResult.objects.create(user=request.user, score=total_marks, section="AdvancedHTML")
            return render(request, 'advanced_html.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })
        else:
            return render(request, 'advanced_html.html', {
                'random_questions': random_questions,
                'total_marks': total_marks,
            })

    return render(request, 'advanced_html.html', {'random_questions': random_questions,'score':scores})


class learning_page(TemplateView):
    template_name = "basic_learnhtml.html"


class Basiclearn(TemplateView):
    template_name = 'basic_learnhtml.html'


def intermediate_text_material(request):
    return render(request, 'intermediatehtml_learn.html')


class Intermediatelearn(TemplateView):
    template_name = 'intermediatehtml_learn.html'


def advanced_text_material(request):
    return render(request, "advancedhtml_learn.html")


# def htmlintro(request):
#     return render(request, "htmlintro.html")
class htmlintro(TemplateView):
    template_name = 'htmlintro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TestResult.objects.filter(user=self.request.user)
        return context



@login_required
def upload_project2(request):
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the uploaded project with the authenticated user
            project = form.save(commit=False)  # Don't save to database yet
            project.student = request.user  # Associate with the authenticated user
            project.save()  # Now save to database
            return redirect('project_list')  # Redirect to file list page after successful upload
    else:
        form = ProjectUploadForm()  # Create a new form instance if not a POST request
    return render(request, 'upload_project2.html', {'form': form})  # Render the form template
