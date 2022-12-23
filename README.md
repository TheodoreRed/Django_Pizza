# Django Website

This is a simple Django website that demonstrates my knowledge of the Django web framework.

## Features
- Allows users to create a post about a pizza visit using a form that is saved to the SQLite database
- Displays a list of pizza posts on the homepage starting with the newest first.
- Hyperlinks to the home page, information page, and page to create a new post.

## Technologies Used

- Django
- Python
- HTML
- CSS

## Installation

To run this website locally, follow these steps:

1. Clone the repository:
   `git clone https://github.com/TheodoreRed/Django_Pizza.git`
2. Navigate to the project directory:
   `cd django_project`
3. Create a virtual environment:
   `python3 -m venv .env`
4.  Activate it:
   `.env/Scripts/Activate.ps1`
5. Install the required packages:
   `pip install -r requirements.txt`
6. Run the Django migrations:
   `python manage.py migrate`
7. Start the development server:
   `python manage.py runserver`

## Many ideas for future work
- Add bootstrap styling for the HTML & CSS and add 
- Make it so users have to log in first, can view their profile to see their posts, etc.
- Add pagination to view more pizza posts as scroll

![home](homepage.png)
![info](info.png)