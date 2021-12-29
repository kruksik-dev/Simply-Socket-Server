
# Simply Socket Server (JSON)

A simple server that supports JSON queries. The server performs a predefined function contained in the `funcs.py` file.

The server configuration was set to localhost, if there was a need to test it on 2 separate networks, the server and client IP addressing should be properly configured.




## Usage/Examples
Run the server and client file. It is recommended when opening the client to use the built-in python interperet to be able to send commands directly from the terminal and have a live preview of what is happening between the client and the server
```python
1st tab:
python server.py 

2nd tab:
python -i client.py

```

To be able to send json to the server, you can use the built-in method of the client class named do_cmd, which as the first argument to json takes the name of the function called on the server and then you can give arguments


```python

cli.do_cmd(['name_of_func', *args])

```


## API Reference

#### Say Hello 

| Name | Arguments     | Description                |
| :-------- | :------- | :------------------------- |
| `say_hello ` | `None` | Return String |

#### Say Goodby 

| Name | Arguments     | Description                |
| :-------- | :------- | :------------------------- |
| `say_goodbye ` | `None` | Return String |


#### Say Something 

| Name | Arguments     | Description                |
| :-------- | :------- | :------------------------- |
| `say_sth ` | `String` | Return String |



#### Add

| Name | Arguments     | Description                |
| :-------- | :------- | :------------------------- |
| `add ` | `digits` | Return Digit |

#### Multiply

| Name | Arguments     | Description                |
| :-------- | :------- | :------------------------- |
| `multiply ` | `digits` | Return Digit |


#### Open Browser

| Name | Arguments     | Description                |
| :-------- | :------- | :------------------------- |
| `open_browser ` | `None` | Open Browser, Return String |






## Screenshots

![Zrzut ekranu 2021-12-29 135039](https://user-images.githubusercontent.com/77121786/147664204-fef96b34-8ffb-4618-81a9-41c62c024b5d.png)
