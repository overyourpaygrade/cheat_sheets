[Flask-RESTful ](http://flask-restful-cn.readthedocs.org/en/0.3.4/)

##### min_api1.py
```
$ curl http://127.0.0.1:5000/
127.0.0.1 - - [03/Feb/2016 23:10:32] "GET / HTTP/1.1" 200 -
{
    "hello": "world"
}
```

##### min_api2.py
```
$ curl http://127.0.0.1:5000/todo1 -d "data=Remember the milk" -X PUT
127.0.0.1 - - [03/Feb/2016 23:15:08] "PUT /todo1 HTTP/1.1" 200 -
{
    "todo1": "Remember the milk"
}
$ curl http://127.0.0.1:5000/todo1
127.0.0.1 - - [03/Feb/2016 23:15:21] "GET /todo1 HTTP/1.1" 200 -
{
    "todo1": "Remember the milk"
}
$ curl http://127.0.0.1:5000/todo2 -d "data=Change the breakpads" -X PUT
127.0.0.1 - - [03/Feb/2016 23:16:22] "PUT /todo2 HTTP/1.1" 200 -
{
    "todo2": "Change the breakpads"
}
$ curl http://127.0.0.1:5000/todo2
127.0.0.1 - - [03/Feb/2016 23:16:24] "GET /todo2 HTTP/1.1" 200 -
{
    "todo2": "Change the breakpads"
}

```

##### min_api_final.py
###### GET all todos
```
$  curl http://localhost:5000/todos
{
    "todo1": {
        "task": "build an API"
    },
    "todo2": {
        "task": "?????"
    },
    "todo3": {
        "task": "profit!"
    }
}

```

###### GET single todo
```
$ curl http://localhost:5000/todos/todo3
{
    "task": "profit!"
}

```

###### DELETE a todo
```
$ curl http://localhost:5000/todos/todo2 -X DELETE -v
* About to connect() to localhost port 5000 (#0)
*   Trying 127.0.0.1...
* connected
* Connected to localhost (127.0.0.1) port 5000 (#0)
> DELETE /todos/todo2 HTTP/1.1
> User-Agent: curl/7.26.0
> Host: localhost:5000
> Accept: */*
>
* additional stuff not fine transfer.c:1037: 0 0
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.11.3 Python/2.7.3
< Date: Fri, 05 Feb 2016 00:05:38 GMT
<
* Closing connection #0

```

###### PUT (add a task)
```
$ curl http://localhost:5000/todos -d "task=something new" -X POST -v
* About to connect() to localhost port 5000 (#0)
*   Trying 127.0.0.1...
* connected
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /todos HTTP/1.1
> User-Agent: curl/7.26.0
> Host: localhost:5000
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 18 out of 18 bytes
* additional stuff not fine transfer.c:1037: 0 0
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 32
< Server: Werkzeug/0.11.3 Python/2.7.3
< Date: Fri, 05 Feb 2016 00:05:54 GMT
<
{
    "task": "something new"
}
* Closing connection #0

```

###### POST (update a task)
```
$ curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
* About to connect() to localhost port 5000 (#0)
*   Trying 127.0.0.1...
* connected
* Connected to localhost (127.0.0.1) port 5000 (#0)
> PUT /todos/todo3 HTTP/1.1
> User-Agent: curl/7.26.0
> Host: localhost:5000
> Accept: */*
> Content-Length: 24
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 24 out of 24 bytes
* additional stuff not fine transfer.c:1037: 0 0
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 38
< Server: Werkzeug/0.11.3 Python/2.7.3
< Date: Fri, 05 Feb 2016 00:06:04 GMT
<
{
    "task": "something different"
}
* Closing connection #0
```

##### api_wdb.py
###### Get root
```
curl http://localhost:5000/
<ul class=posts>

        <li><h2> First Entry</h2>This is some text

        <li><h2> Second Entry</h2>This is some more text

        <li><h2> Third Entry</h2>This is some more text again

</ul>  
```

###### Get all db items
```
$ curl http://localhost:5000/api/v1/posts/
{
  "count": 3,
  "posts": [
    {
      "text": "This is some text",
      "title": "First Entry"
    },
    {
      "text": "This is some more text",
      "title": "Second Entry"
    },
    {
      "text": "This is some more text again",
      "title": "Third Entry"
    }
  ]
}
```

###### Get one item
```
$ curl http://localhost:5000/api/v1/posts/1
{
  "count": 1,
  "posts": [
    {
      "text": "This is some text",
      "title": "First Entry"
    }
  ]
}
```

###### Delete a post
```
$ curl http://localhost:5000/api/v1/posts/1 -X DELETE -v
* About to connect() to localhost port 5000 (#0)
*   Trying 127.0.0.1...
* connected
* Connected to localhost (127.0.0.1) port 5000 (#0)
> DELETE /api/v1/posts/1 HTTP/1.1
> User-Agent: curl/7.26.0
> Host: localhost:5000
> Accept: */*
>
* additional stuff not fine transfer.c:1037: 0 0
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 30
< Server: Werkzeug/0.11.3 Python/2.7.3
< Date: Fri, 05 Feb 2016 01:49:27 GMT
<
{
  "status": "Post deleted"
* Closing connection #0
}
```
