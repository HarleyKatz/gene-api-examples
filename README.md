# Example code for querying the gene API

Querying the gene API requires both a username and password. To request access to the API, contact David Bick. 

To query the API, first obtain a JWT token via the authentication endpoint. For example:

```
curl --request POST \
  --url https://david-gene-api.herokuapp.com/auth  \                                                                              --header 'content-type: application/json' \
  --data '{"username":"<username>","password":"<passowrd>"}'
```