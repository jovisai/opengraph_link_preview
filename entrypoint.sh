# start memcached server
memcached -p 11211 -U 11211 -u root -m 64 -d

# start the flask app
gunicorn -b :8000 wsgi:app