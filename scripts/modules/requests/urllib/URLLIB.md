## HTTP GET Requests with `urllib.request`

**HTTP Message** can be understood as text, transmitted as a stream of bytes.

**Decoded HTTP Message:**

It has two main parts:

 - Metadata
 - body


```bash
GET / HTTP/1.1
Host: www.google.com

```

- HTTP Method: GET (A commonly used HTTP method to request a specific resource from a server)
- Requested Resource: / (It is indicated by the forward slash to represent the root directory of the website. It means client is requesting the default resource from the server.)
- HTTP Version: HTTP/1.1 (HTTP Version used)
- Host: www.google.com (specifies domain name of the server)


**HTTP Response:**

It also has two parts

 - Status line
 - Metadata (Key-value pairs format contains body)


### Understand How `urllib.request` Represents an HTTP Message

- The `HTTPResponse` object is the main representation of an HTTP message used in `urllib.request`.

- `HTTPResponse` and `HTTPMessage` are the data structure provided by the http module and used by `urllib.request`.

- `pprint()` and `dir()` of `HTTPResponse` object can be used.

```yaml
<img width="968" height="522" alt="Image" src="https://github.com/user-attachments/assets/5aa52e20-a468-4c01-a756-ae60eed68c45" />

```


**dir():** It is a built-in function which doesn't need to be imported. It is used to list the attributes of an object. It returns all the list of attributes and methods associated with objecct you pass to it.


### Inspect All the Headers of the HTTPResponse object

- Access the headers using the .headers attribute of the HTTPResponse object.
- An HTTPMessage object can be treated like as dictionary by calling `.items()` on it to get all the headers as tuples.

### Get `HTTPResponse` Headers in urllib.request

- `.getheaders()` method returns a list of tuples containing all the headers.
- `.getheader("header_name")` method returns the value of the specified header.
- you can use the square bracket `([])` syntax on headers from HTTPMessage.