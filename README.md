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
  造訪[http://127.0.0.1:8000/api/CusApp/](http://127.0.0.1:8000/api/CusApp/)，如未成功授權，API將傳回`HTTP 403 Forbidden`（資源不允許訪問）狀態碼。
  ![Imgur](https://i.imgur.com/qJRXY6n.png)
  <br>
  授權方式是以命令提示字元（cmd）於專案下，使用以下指令建立超級使用者。
  >python manage.py createsuperuser
  
  ![Imgur](https://i.imgur.com/UR2h1yG.png)
  <br>
  <br>
* GET（讀取資源）
  <br>
  造訪[http://127.0.0.1:8000/api/CusApp/](http://127.0.0.1:8000/api/CusApp/)，取得所有客戶資料。
  ![Imgur](https://i.imgur.com/88hqIbk.png)
  <br>
  JSON格式下，所有客戶資料。
  ![Imgur](https://i.imgur.com/HP4ge1o.png)
  <br>
  <br>
  123

  
  
