# django-app-reactjs-integrate

## What is it?
 
This is django app for integration ReactJS to the project.You can install one and insert ReactJS, which is assembled with **webpack**, to your template with **script** tag, or use **frontend_view** in **views.py**

## Installation to django project 

Firstly install the app 

```console
git clone https://github.com/sasha-ajin/django-app-reactjs-integrate.git
```
### Setting up django 
After that, rename the app to **frontend**

```console
mv django-app-reactjs-integrate/ frontend
```

Add **frontend** to your **INSTALLED_APPS**

```python
INSTALLED_APPS = [
    ...
    'frontend'
]
```

Also, you should have static folder in your django project
### Setting up Reactjs

Inside **frontend** folder install nodejs

```console
npm install
```

And assemble Reactjs in a single file

```console
npm run dev
```
