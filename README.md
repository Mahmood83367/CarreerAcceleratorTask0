# **Degtalize Computiq Career Accelerator qulifcation Task**

## **Description**

This project is a test by Computiq to test the skills of the participants in the back-end part and their proficiency.
This project adds fields to a table and queries about these fields, and there is an integrated application for the Users.

## **Installation**
* Fork this repo into your device and open it in any code editor.
* You need Python Versin is **3.11.0**
* You need to install the Requirements by **Type this in console** 
```pip install -r requirements.txt```

## **Usage**
* first thing you need to migrate to build database.
because i am using a custom User model, you can do 4 steps:
1. Comment out ***django.contrib.admin*** in ```CareerAcceleratorTask0/settings/INSTALLED_APPS ```
```
  INSTALLED_APPS = [
   ...
   #'django.contrib.admin',
   ...
   ]
```
2. Comment out admin path in ```CareerAcceleratorTask0/urls.py/```
```
   urlpatterns = [
   ...
   #path('admin/', admin.site.urls) 
   ...
]
```
3. Then run 
```
python manage.py makemigrations
python manage.py migrate

```
4. **When done, uncomment all back**

* now you can run project by type
```python manage.py runserver```

* To see the api go to this url 
http://127.0.0.1:8000/api/docs/
