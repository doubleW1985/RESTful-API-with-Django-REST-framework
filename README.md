## RESTful API with Django REST framework

利用[Django REST framework](http://www.django-rest-framework.org/)，快速打造`RESTful API`。
<br>
<br>
* API Root
  <br>
  造訪[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)，取得API Root。
  ![Imgur](https://i.imgur.com/Yhku9my.png)
  <br>
  <br>
* Authentication
  <br>
  造訪[http://127.0.0.1:8000/api/CusApp/](http://127.0.0.1:8000/api/CusApp/)，如未取得授權，API將傳回`HTTP 403 Forbidden‵狀態碼。

  
  建立授權，以防API遭他人不受限制操作。
  ![Imgur](https://i.imgur.com/qJRXY6n.png)
  <br>
  使用命令提示字元 (cmd ) 於專案下建立超級使用者。
  
  >python manage.py createsuperuser
  
  ![Imgur](https://i.imgur.com/UR2h1yG.png)
  <br>
  <br>

  
  
