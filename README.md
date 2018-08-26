# Django_Blog
blog with comments and registration. The ability to upload user avatars (RabbitMQ).

# django-betterforms

Installation
Install the package:

$ pip install celery


https://www.rabbitmq.com/download.html
http://www.erlang.org/downloads

запуск rebbitMQ:
net start rabbitmq
rabbitmq-plugins enable rabbitmq_management
оболочка: guest / guest
http://localhost:15672/#/

запуск просмтра очереди:
celery -A blog_project worker --pool=solo -l info

