# Django-NotesApp
#### Project Description:
This project is a web application for managing and sharing notes. It is built using Django, a Python web framework, and utilizes Bootstrap for the frontend styling. The application allows users to sign up, log in, and manage their notes. Users can add new notes, view their existing notes, delete notes, and share notes with other users.

#### Key Features:
*	User authentication: Sign up, log in, and log out functionality.
*	Note creation: Users can create new notes by providing a title, category, and file uploading.
*	Note listing: Users can view a list of their own notes and notes shared with them.
*	Note sharing: Users can share their notes with other registered users.
*	Note deletion: Users can delete their own notes or unshare notes shared with them.

#### Technologies Used:
*	Django: Python web framework for building the backend of the application.
*	Bootstrap: CSS framework used for frontend styling and responsive design.
*	HTML and CSS: Used for creating the web pages and styling the application.
*	SQLite: A lightweight and self-contained database engine storing the application's data.

#### Installation:
1.	Clone the project repository.
"git clone https://github.com/cswapnali/Django-NotesApp.git"
2.	Install the project dependencies using pip.
"pip install -r requirements.txt"
3.	Set up the database configuration in settings.py. Since the project is using SQLite, you don't need to make any changes to the database settings as the default configuration is already set to use SQLite.
4.	Apply database migrations by running the following command:
"python manage.py migrate"
5.	Create a superuser by running the following command and following the prompts:
"python manage.py createsuperuser"
This will allow you to access the Django admin interface and perform administrative tasks.
6.	Start the development server by running the following command:
"python manage.py runserver"
7.	Access the application in your browser at "http://localhost:8000".
8.	To upload files, make sure to create a media directory in the project's root directory.
Add the following lines to settings.py to configure media file handling:
"import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')"

#### How to Use:
To use this application:
1.	Sign up for an account using the "Signup" page.
2.	Login with your credentials on the "Login" page.
3.	After logging in, you will be redirected to the "Notes" page where you can view, add, and delete notes.
4.	Click on a note to view its details.
5.	To add a new note, click on the "Add Note" button and fill in the required fields.
6.	To share a note with another user, click on the "Share" button and enter the username of the user you want to share the note with.
7.	To log out, click on the "Logout" button in the top-right corner.

#### Screenshots: 
Please refer to the following Google Drive link to access screenshots and a demo video of the application: 
https://drive.google.com/drive/folders/1fvcWo5Wh-ADUaGiiNH6RujuvZYAo1QoC?usp=sharing

#### Contact Information:
*	LinkedIn: https://www.linkedin.com/in/swapnali-choudhari/
*	Portfolio: https://swapnalic14.pythonanywhere.com/






