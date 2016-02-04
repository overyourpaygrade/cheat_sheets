###### min_api1.py
```
$ curl http://127.0.0.1:5000/
127.0.0.1 - - [03/Feb/2016 23:10:32] "GET / HTTP/1.1" 200 -
{
    "hello": "world"
}
```

###### min_api2.py
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
