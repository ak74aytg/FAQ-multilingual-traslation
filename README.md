# **FAQ backend system in django**

**Description**: a web-based application designed to manage FAQs efficiently. It provides a RESTful API that allows users to fetch, add, update, and delete questions. The app supports multilingual content and is designed to be scalable, easy to use, and integrate into various platforms. The project is built with Django on the backend and includes a straightforward frontend for interacting with the API.

---

**Features** : 
- Multi-language support for:
  - English (en)
  - Hindi (hi)
  - Bengali (bn)
- Rich text editing with CKEditor integration
- Automatic translation using googletrans library
- Redis-based caching system
- RESTful API with language parameter support


**Tech Stack**
- *Core Technologies*
  - Python 3.9
  - Django 5.1
  - Django REST Framework
  - Redis (for caching)

- *Dependencies*
  - django-ckeditor (for WYSIWYG editor)
  - googletrans (for automatic translations)



## **Table of Contents**
- [Installation](#installation)
- [API Usage Examples](#api-usage-examples)
- [License](#license)

---

## **Installation**

### **Prerequisites**

Before setting up the project, ensure you have the following installed:
- **Python 3.11+** (for backend)
- **Redis Server** 6.0 or higher

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/ak74aytg/FAQ-multilingual-traslation
cd FAQ-multilingual-traslation
```
### **Step 2: Setup the Project**
Python (Backend)

1. Create and activate a virtual environment:
```
python3.11 -m venv venv    # googletranslate requires a dependency on python 3.11
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
2. Install dependencies:
```
pip install -r requirements.txt

```
3. Creating admin
```
python manage.py migrate
python manage.py createsuperuser
```

4. Start server
```
python manage.py runserver
```

5. Start Redis server (if not running):
```
redis-server
```

## **Project Structure** 
he following structure represents the organization of the Django FAQ API project:
```
faq_project/
│── faq_project/          # Main Django project directory
│   │── __init__.py 
│   │── asgi.py           
│   │── settings.py       # Django settings file
│   │── urls.py           # Root URL configurations
│   │── wsgi.py           
│
│── faq/                  # Django app for FAQs
│   │── tests/            # Unit tests for the app
|       │──__init__.py
        │──test_models.py
        │──test_views.py

│── │── __init__.py       
│   │── admin.py          # Django admin panel configurations
│   │── models.py         # Database models
│   │── serializers.py    
│   │── urls.py           # App-level URL routing
│   │── views.py          # API views (business logic)
│
│── .flake8               # Linter configuration for PEP8 compliance
│── .gitignore           
│── db.sqlite3           
│── manage.py             # Django CLI management script
│── README.md             # Project documentation
│── requirements.txt      # Dependencies for the project

```
## **API Usage Examples**
### **Fetching All FAQs**
**Endpoint** : `GET /faqs/`    
               `GET /faqs/?lang=<la>`


**only supported language are : English(en), Hindi(hi), Bangla(bn)**
```
curl -X GET "http://localhost:8000/faqs/?lang=hi"
```
**Response:**
```json
[
    {
    "id": 4,
    "question": "Django क्या है?",
    "answer": "<p>Django एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।</p>"
  },
  {
    "id": 5,
    "question": "<p> <strong> <span style = \"font-size: 36px\"> आपका नाम क्या है? </span> </strong> </p>",
    "answer": "<p> <u> <em> <span style = \"font-size: 18px\"> मेरा नाम अक्षय पंत है </span> </em> </u> </p>"
  },
  {
    "id": 8,
    "question": "दुनिया का सबसे बड़ा एनीमे?",
    "answer": "<p><em><strong><span style=\"color:#4e5f70\"><span style=\"font-size:72px\">मैं आयरन मैन हूं!</span></span></strong></em></p>"
  },
  {
    "id": 9,
    "question": "दुनिया का सबसे बड़ा एनीमे?",
    "answer": "<p style=\"text-align:center\"><span style=\"font-size:72px\"><strong>एक टुकड़ा</strong></span></p><p style=\"text-align:center\"><span style=\"font-size:72px\"><strong>तब</strong></span></p>"
  }
]
```

### **Fetching a Single FAQ**
**Endpoint** : `GET /faqs/<int:faq_id>/`
```
curl -X GET "http://localhost:8000/faqs/9/?lang=hi"
```
**Response:**
```json
{
  "id": 9,
  "question": "दुनिया का सबसे बड़ा एनीमे?",
  "answer": "<p style=\"text-align:center\"><span style=\"font-size:72px\"><strong>एक टुकड़ा</strong></span></p><p style=\"text-align:center\"><span style=\"font-size:72px\"><strong>तब</strong></span></p>"
}
```


### **Adding a New FAQ**
**Endpoint** : `POST /faqs/`
```
curl -X POST "http://localhost:8000/faqs/" \
    -H "Content-Type: application/json" \
    -d '{"question": "What is Django?", "answer": "Django is a high-level Python web framework."}'

```
**Response:**
```json
{
  "id": 10,
  "question": "What is Django?",
  "answer": "Django is a high-level Python web framework.",
  "question_hi": "Django क्या है?",
  "answer_hi": "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
  "question_bn": "ডjango কি?",
  "answer_bn": "ডjango হল একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।"
}
```



### **Updating an Existing FAQ**
**Endpoint** : `PUT /faqs/<int:faq_id>/`
```
curl -X PUT "http://localhost:8000/faqs/1/" \
    -H "Content-Type: application/json" \
    -d '{"question": "What does this app do?", "answer": "This app helps you manage your tasks."}'

```
**Response:**
```json
{
    "id": 1,
    "question": "What does this app do?",
    "answer": "This app helps you manage your tasks."
}
```


### **Deleting an FAQ**
**Endpoint** : `DELETE /faqs/<int:faq_id>/`
```
curl -X DELETE "http://localhost:8000/faqs/1/"
```
**Response:**
```json
{
    "message": "FAQ deleted successfully."
}
```


### **License**

This project is licensed under the MIT License - see the LICENSE file for details.
