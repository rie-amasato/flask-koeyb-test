pip freeze > requirements.txt

echo gunicorn >>requirements.txt
echo web: gunicorn --bind :8000 app:app > Procfile
