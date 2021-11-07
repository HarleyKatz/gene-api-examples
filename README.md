# Example code for querying the gene API

Querying the gene API requires both a username and password. To request access to the API, contact David Bick. 

To query the API, first obtain a JWT token via the authentication endpoint. For example:

```
curl --request POST \
  --url https://david-gene-api.herokuapp.com/auth \ 
  --header 'content-type: application/json' \
  --data '{"username":"<username>","password":"<passowrd>"}'
```

Once the JWT token is obtained, you can then query the genes enpoint with
```
curl https://david-gene-api.herokuapp.com/auth/genes/<gene> -H "Accept: application/json" -H "Authorization: JWT <token>"
```

For example, one can replace `<gene>` with `brca2` to obtain information on the BRCA2 gene. The code will return a 401 error if the request is unauthorized or `NOT FOUND` for an unrecognized gene.

A python example using the `requests` library can be found in `example.py`