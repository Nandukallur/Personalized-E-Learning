
# Personalized E-Learning



## Getting Started

Follow these steps to set up and run the project on your local machine:

## System Requirments
Ensure that your system meets the following requirements to successfully set up and run the Personalized E-Learning:

## Software Requirements

Python: Version 3.6 or higher

Django: Version 3.0 or higher

Database: SQLite (default for Django)


## Installation

Clone this repository to your local machine

```bash
 git clone https://github.com/sumodkanth/Personalized-E-Learning.git
```


    
## Deployment

1. Navigate to the project directory.

```bash
  cd E_Learning 
```

2. Activate the virtual Environment.

```bash
  myenv\scripts\activate
```

3. Install the required dependencies.
```bash
  pip install -r requirements.txt
```

4. Apply initial migrations to set up the database:
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
Configure email settings in the settings.py file to enable the "Reset Password" feature.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'your_smtp_server'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your_email@example.com'

EMAIL_HOST_PASSWORD = 'your_email_password'


5. Start the server
```bash
  python manage.py runserver
```
The server will be running at http://127.0.0.1:8000/.
## Demo Login
Username: admin2

Password: admin2