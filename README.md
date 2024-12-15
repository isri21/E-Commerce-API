# Authentication
Endpoint: `api/login/`
Method: `POST`
Body:
```json
{
	"username: "username",
	"password": "password"
}
```
## Responses:
Response Body:
{
    "token": "<generated_token>"
}
Response Status: 200 OK

Response Body:
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}

Response Status: 400 Bad Request
