========================================================================================================================
# Django_Blog
blog with comments and registration. The ability to upload user avatars and resize him (RabbitMQ)

###### Version
_import django
django.get_version()
'1.11.3'_

### Installation
Install the package:
$ pip install celery

https://www.rabbitmq.com/download.html
http://www.erlang.org/downloads

run rebbitMQ:
  rabbitmq-service
  rabbitmq-plugins enable rabbitmq_management
  http://localhost:15672/#/   (user: guest, password: guest)

run and show Queue:
celery -A blog_project worker --pool=solo -l info
========================================================================================================================
####	- Общее описание -
-Для беглого ознакомления без развертывания, можно просмотреть в папке PrintScrn скрины с некоторых страниц сайта.
-Также в корне находится ERM-диаграмма.
-В blog_app\migrations\*.sql содержится дамп рабочей базы включающей в себя:
	4-х зарегистрированных пользователей (хэш всех пользователей соответствует паролю 1111qqqq, также указан email при регистрации и настроен на вывод в консоль при утере пароля),
	аватарки,
	их статьи и комментарии,
	комментарии к комментариям,
	подписки пользователей друг на друга.
	Пользователя admin (хэш соответствует паролю adminadmin, email также указан)
- В качестве DB при разработке использовалась MySQL. При использовании другой DB нужно сменить настройки.
- JS на страницах не используется , за исключением страницы со статьей и комментариям к ней.


- главная страница различается для авторизованного пользователя и для гостя сайта:
	* изменены ссылки NavBar
	* для гостя лента новостей выглядит как 10 случайных статей случайных пользователей
	* для пользователя в ленте отображаются 10 случайных статей случайных пользователей, кроме собственных статей пользователя.
	* изображение в левой части сайта всегда случайное.

- страницы авторизации/регистрации содержат ссылки друг на друга и на сброс пароля через email.
	* при регистрации необходимо добавить изображение для аватарки.

- подписки пользователя <Favorites> содержат информацию о пользователях добавленных в подписку, а также информацию о том, как давно был
пользователь зарегистрирован на сайте.
	* подписаться на пользователя можно, например, кликнув на главной странице по аватврке пользователя. Откроется страница со всеми статьями
пользователя, в самом низу будет ссылка <Add to MyFavorites> позволяющай добавить пользователя в список понравившихся. при клике
на эту ссылку рядом появится flash сообщение о статусе операции.

- <MyPost> содержит все опубликованные статьи пользователя.

- для просмотра статьи и комментариев к ней нужно кликнуть на тему статьи.
	* можно добавить комментарий к статьей
	* можно добавить комментарии к комментарию любой вложенности,
	* форма комментария появится автоматически.


- <New Post> страница с формой для добавления новой статьи.
========================================================================================================================
####	- Подробное описание -
#####   Описание схемы базы данных (откройте файл ERM.png)



========================================================================================================================
