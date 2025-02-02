FAQ Multilingual System 


This project is a multilingual FAQ system built with Django and Django REST Framework. 
It allows users to manage Frequently Asked Questions (FAQs) in multiple languages 
(English, Hindi, Bengali). The system supports rich-text answers via the WYSIWYG editor
(django-ckeditor) and caches translated questions using Redis for improved performance.


## Features
- Multi-language FAQ management (English, Hindi, Bengali)
- WYSIWYG editor for rich-text answers
- Dynamic translation using Google Translate
- Fast and efficient API with caching

## Model Design

The system utilizes a Django model to store FAQs with the following fields:
- **Question:** A `TextField` to store the FAQ question.
- **Answer:** A `RichTextField` for rich-text formatting of the FAQ answer, utilizing the django-ckeditor.
- **Language-Specific Translations:** Fields for translations, such as `question_hi` for Hindi and `question_bn` for Bengali.

A method is implemented to retrieve translated text dynamically based on the selected language.

## WYSIWYG Editor Integration

The project integrates the `django-ckeditor` library to allow users to format answers properly. The WYSIWYG editor supports multilingual content to enhance the user experience.

## API Development

A Django REST API is created to manage FAQs with the following features:
- Support for language selection via the `?lang=` query parameter.
- Efficient responses leveraging pre-translation to enhance performance.




## Caching Mechanism

The Django caching framework is implemented to store translations efficiently. Redis is utilized for improved performance, ensuring quick access to frequently requested data.

![image](https://github.com/user-attachments/assets/a0934de9-cfba-4157-9021-ff860be4a576)


## Multi-language Translation Support

The project uses the Google Translate API (or `googletrans` library) to automate translations during object creation. In cases where a translation is unavailable, a fallback to English is provided.



## Django Admin Panel

The FAQ model is registered in the Django Admin panel, providing a user-friendly interface for managing FAQs, enabling easy addition, editing, and deletion of FAQs.


![Screenshot 2025-02-02 172941](https://github.com/user-attachments/assets/438376e3-1b68-424b-a663-0679f4887e81)



## Unit Tests & Code Quality

Unit tests are written using `pytest` or Django’s built-in unittest framework. Tests cover model methods and API responses to ensure functionality. The project adheres to PEP8 guidelines, utilizing `flake8` for linting.


## Installation

To set up the project locally, follow these steps:


1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yuvraj1507/faq-multilingual-system.git
   cd faq_project


# Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


# Install the required dependencies:
pip install -r requirements.txt


~ Set up Redis on my local machine or use Docker to run it. (Followed Redis installation for local setup)


# Run migrations to set up the database:
python manage.py migrate

# Run the development server:
python manage.py runserver

The app should be accessible at http://localhost:8000/.

~ (Optional) To test the app, you can also use Postman or curl commands to interact with the API. 
I Used Postman to Interact with the API.


![Screenshot 2025-02-02 175719](https://github.com/user-attachments/assets/bf0205da-f70a-4717-8438-6574d9527525)


API Usage:


Fetch FAQs in English (default):
http://localhost:8000/api/faqs/


Fetch FAQs in Hindi:
http://localhost:8000/api/faqs/?lang=hi


Fetch FAQs in Bengali:
http://localhost:8000/api/faqs/?lang=bn


~ Create a new FAQ (POST request):
-X POST http://localhost:8000/api/faqs/ -d '{"question": "What is Django?", "answer": "Django is a high-level Python web framework."}' 

The new FAQ will automatically be translated into Hindi and Bengali during creation.

Contributing

Thank you for considering my project submission for the hiring test at BharatFD. If you would like to contribute or provide feedback, here are the steps to follow:

1. Fork the repository: Create your own copy of the project repository on GitHub.
2. Create a new branch: For any features or fixes, create a new branch to work on. This helps keep the main branch clean and organized.
3. Run tests: Ensure that your code passes all tests and adheres to PEP8 guidelines to maintain code quality.
4. Submit a pull request: Once you're satisfied with your changes, submit a pull request to my repository. I will review it and merge it if everything looks good.

I appreciate any feedback or contributions you may have!

