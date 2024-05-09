# alkye_blog
Simple blog application using Django and Django REST Framework, integrating basic CRUD (Create, Read, Update, Delete) functionalities.

## Installation

### Requirements
- Python
- Django
- Django rest Framework

  Complete list available in requirements.txt file

### Quickstart
- Clone the repo.  
    ```bash
    git clone https://github.com/shaweta/alkye_blog.git
    ```

- Inside the backend folder, make a virtual environment and activate it 
    ```bash
    cd myblog
    python -m venv env 
    source env/bin/activate(./env/Scripts/activate)

    ```

- Install requirements from requirements.txt
    ```
    pip install -r requirements.txt
    ```

- Makemigrations and migrate the project
    ```
    python manage.py makemigrations && python manage.py migrate
    ```

- Create a superuser
    ```
    python manage.py createsuperuser
    ```

- Runserver
    ```
    python manage.py runserver
    ```

**Note: After running the server, you can use the api inside browser or you can use Postman to make api calls. Make sure in each api call, you provide username, password by creating a user
Here  token authentication is applied so when testing with postman or thunder client in VSCode make sure to pass token in the header while making calls.
.**



While working with api in browser, you can login using `http://127.0.0.1:8000/api/` link.


## API
<details>
<summary> Post model </summary> 

- POST:
    - title: string(unique),
    - content: text,
    - author: text
    - published_date:Datetime field

</details>

<details>
<summary> Comments Model </summary>


</details>





### Endpoints

Brief explanation of endpoints:

| Function                                                                                               | REQUEST    | Endpoint                                                | Authorization | form-data                                 |
|--------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------|---------------|-------------------------------------------|
| Create new Post                                                                                      | POST       | http://127.0.0.1:8000/api/posts/                      | Token Auth                  |
| Returns list of all existing Posts                                                                   | GET        |  http://127.0.0.1:8000/api/posts/                     | Token Auth    |                                           |
| Returns the detail of an Post instance                                                               | GET        | http://127.0.0.1:8000/api/posts/{int:id}/             | Token Auth    |                                           |
| Update the detail of an Post instance                                                                | PUT, PATCH | http://127.0.0.1:8000/api/posts/{int:id}/             | Token Auth   |                                           |
| Delete an Post instance                                                                              | DELETE     | http://127.0.0.1:8000/api/posts/{int:id}/             | Token Auth    |                                           |
| Returns a list of all Comments on  existing Post                                                         | GET        | http://127.0.0.1:8000/api/posts/{int:id}/comments  | Token Auth  |                                           |
| Creates a new comment                                 | POST       | http://127.0.0.1:8000/api/api/post/{int:id}/comments              | Token Auth   |  |
| Returns the details comment.                                                     | GET        | http://127.0.0.1:8000/api/posts/{int:id}/comments/{int:id}/     | Token Auth    |                                           |
| Update or edit an existing Comment . Returns updated Purchase orders                                  | PUT, PATCH | http://127.0.0.1:8000/api/posts/{int:id}/comments/{int:id}/     | Token Auth   |  |
| Deletes the existing comment                                                                   | DELETE     | http://127.0.0.1:8000/api/posts/{int:id}/comments/{int:id}/     | Token Auth    |                                           |

 
You can use  VSCode thunder client or postman to interact with the apis and to get access of apiyou need to give Token in Header 
Adding Pictures of my Tests using thunderclient
## Post list -Get Request(with token Authenication)
![postget](https://github.com/shaweta/alkye_blog/assets/17871651/e1814e4c-b0ae-4a12-98c3-370f7b0af162)

## Post Instance -Get Request(with Authenication)

![post instance](https://github.com/shaweta/alkye_blog/assets/17871651/f37d1268-feb3-4584-9b54-207b530e9449)

## Post create -Post Request(with Authenication)

![createpost](https://github.com/shaweta/alkye_blog/assets/17871651/5402d9d4-c278-4e7b-b415-129191d85c4b)

## Post commentlist -Get Request(with Authenication)

![getcomment](https://github.com/shaweta/alkye_blog/assets/17871651/dd79190f-6ed4-4cda-8cd1-d00915553908)

## Post comment Instance -Get Request(with Authenication)
![get comment](https://github.com/shaweta/alkye_blog/assets/17871651/4b4707b1-8362-4b76-8b90-a1324a3699da)

## Post Comment create -Post Request(with Authenication)
![commentcreate](https://github.com/shaweta/alkye_blog/assets/17871651/c71c11f7-7591-4161-9469-ade64893cd48)
## Post Comment delete -Delete Request(with Authenication)

![delete](https://github.com/shaweta/alkye_blog/assets/17871651/f4855313-369d-4516-8c98-4e667076b262)
