pip freeze > requirements.txt

echo gunicorn >>requirements.txt
echo web: gunicorn app:app > procfile
