## RESTful API with Django REST framework

利用[Django REST framework](http://www.django-rest-framework.org/)，快速打造「Customers」的`RESTful API`。
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
  造訪[http://127.0.0.1:8000/api/CusApp/](http://127.0.0.1:8000/api/CusApp/)，如未成功授權，API返回`HTTP 403 Forbidden`（資源不允許訪問）狀態碼。
  ![Imgur](https://i.imgur.com/qJRXY6n.png)
  <br>
  授權方式是以命令提示字元（cmd）於專案下，使用以下指令建立超級使用者。
  >python manage.py createsuperuser
  
  ![Imgur](https://i.imgur.com/UR2h1yG.png)
  <br>
  <br>
* GET（資源讀取）
  <br>
  造訪[http://127.0.0.1:8000/api/CusApp/](http://127.0.0.1:8000/api/CusApp/)（以下簡稱客戶API），取得**所有客戶資料**，並允許HTTP請求方法「GET（讀取）、POST（新增）、 HEAD（讀取HTTP標頭訊息）、OPTIONS」。
  ![Imgur](https://i.imgur.com/88hqIbk.png)
  <br>
  於客戶API後加入`?format=json`，如[http://127.0.0.1:8000/api/CusApp/?format=json](http://127.0.0.1:8000/api/CusApp/?format=json)，返回**JSON格式下，所有客戶資料**。
  ![Imgur](https://i.imgur.com/HP4ge1o.png)
  <br>
  於客戶API後加入`欲查詢id`，如[http://127.0.0.1:8000/api/CusApp/92/](http://127.0.0.1:8000/api/CusApp/92/)，返回**該id下，客戶資料**，並允許HTTP請求方法「GET、PUT（替換）、PATCH（部分更新）、DELETE（刪除）、HEAD、OPTIONS」。
  ![Imgur](https://i.imgur.com/xGe4t1E.png)
  <br>
  承上，於id後加入`detail_part/`，如[http://127.0.0.1:8000/api/CusApp/90/detail_part/](http://127.0.0.1:8000/api/CusApp/90/detail_part/)，同樣返回**該id下，客戶(部分)資料**，但僅允許HTTP請求方法「GET、HEAD、OPTIONS」（即不允許異動）。
  ![Imgur](https://i.imgur.com/5uHLwtj.png)
  <br>
  於客戶API後加入`raw_sql_query/`以及參數`?CompanyQuery=欲查詢公司名稱`，如[http://127.0.0.1:8000/api/CusApp/raw_sql_query/?CompanyQuery=WILMAN KALA](http://127.0.0.1:8000/api/CusApp/raw_sql_query/?CompanyQuery=WILMAN%20KALA)，可藉由SQL SELECT句法，返回**該公司名稱下，客戶資料**，並僅允許HTTP請求方法「GET、HEAD、OPTIONS」（即不允許異動）。
  ![Imgur](https://i.imgur.com/uzd2ifR.png)
  <br>
   於客戶API後加入`all_company/`，如[http://127.0.0.1:8000/api/CusApp/all_company/](http://127.0.0.1:8000/api/CusApp/all_company/)，返回客戶API中**所有客戶公司名稱**，並僅允許HTTP請求方法「GET、HEAD、OPTIONS」（即不允許異動）。
   ![Imgur](https://i.imgur.com/zqfVhtK.png)
   <br>
   <br>
* PUT（資源替換） vs PATCH（資源部分更新）
  <br>
  造訪某一id客戶資料，如[http://127.0.0.1:8000/api/CusApp/93/](http://127.0.0.1:8000/api/CusApp/93/)，可於HTTP允許之請求方法「PUT、PATCH」下，進行資源替換或資源部分更新。
  ![Imgur](https://i.imgur.com/DsO0ynB.png)
  ![Imgur](https://i.imgur.com/0lOxD1b.png)
  <br>
  亦可於[http://127.0.0.1:8000/api/CusApp/93/sql_cursor_update/](http://127.0.0.1:8000/api/CusApp/93/sql_cursor_update/)，藉由傳遞參數`CompanyUpdate=欲更新公司名稱`以及SQL UPDATE句法，進行公司名稱更新。
  ![Imgur](https://i.imgur.com/RYfqX6V.png)
  ![Imgur](https://i.imgur.com/UvfCVIP.png)
   <br>
   <br>
* DELETE（資源刪除）
  <br>
  造訪某一id客戶資料，如[http://127.0.0.1:8000/api/CusApp/92/](http://127.0.0.1:8000/api/CusApp/92/)，可於HTTP允許之請求方法「DELETE」下，進行資源刪除，並於刪除成功後返回`HTTP 204 No Content`（成功刪除）狀態碼。
  ![Imgur](https://i.imgur.com/jyWxwB3.png)
  ![Imgur](https://i.imgur.com/dbKVovZ.png)
  ![Imgur](https://i.imgur.com/CLX5R2D.png)
   <br>
   <br>
* POST（資源新增）
  <br>
  造訪[http://127.0.0.1:8000/api/CusApp/](http://127.0.0.1:8000/api/CusApp/)，可於HTTP允許之請求方法「POST」下，進行資源新增，並於新增成功後返回`HTTP 201 Created`（成功建立）狀態碼。
  ![Imgur](https://i.imgur.com/13D0XA0.png)
  <br>
  如需限定Content-Type為application/json，直接於[views.py](https://github.com/doubleW1985/RESTful-API-with-Django-REST-framework/blob/master/DjangoRestFramework/CusApp/views.py)加入`parser_classes = (JSONParser,)`即可。更多資訊可參考[http://www.django-rest-framework.org/api-guide/parsers/#parsersr](http://www.django-rest-framework.org/api-guide/parsers/#parsersr)。 
  ![Imgur](https://i.imgur.com/VkJP9fx.png)
  ![Imgur](https://i.imgur.com/Sr9CCze.png)
  

  
  
