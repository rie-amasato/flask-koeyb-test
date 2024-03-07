pip freeze > requirements.txt

echo gunicorn >>requirements.txt
echo web: gunicorn --bind :$PORT app:app > Procfile
