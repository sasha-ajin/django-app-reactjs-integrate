# django-app-reactjs-integrate

## What is it?
 
This is django app for integration with ReactJS

## Usage

After installation you can insert ReactJS, which is assembled with **webpack**, to your template with **script** tag

```html
<script src={% static 'frontend_build/main.js' %}></script>
```

Or use default **frontend_view** from **views.py** for every url path

```python
from frontend.views import frontend_view
from django.urls import path

urlpatterns = [
    ...
    path("url_path/", frontend_view, name="url_name"),
]
```

## Installation to django project 

Firstly install the app 

```
git clone https://github.com/sasha-ajin/django-app-reactjs-integrate.git
```
### Setting up django 
After that, rename the app to **frontend**

```
mv django-app-reactjs-integrate/ frontend
```

Add **frontend** to your **INSTALLED_APPS**

```python
INSTALLED_APPS = [
    ...
    'frontend'
]
```

Also, you should have **static** folder in your django project, which should be available on [**your.domain.name/static/**](https://your.domain.name/static) 

### Setting up ReactJS

Inside **frontend** folder install **nodejs**

```
npm install
```

And assemble ***ReactJS*** in a single file

```
npm run dev
```

