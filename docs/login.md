# Login Endpoint

Login using `username` and `password`. Returns an `auth_token` which is required for sending and receiving messages.

**URL** : `/login`

**Method** : `POST`

**Query Params** :

* `username`
* `password`

## Success Response

**Code** : `200 OK`

**Content example**:

```json
{
    "auth_token": "6d9f4227-22cf-4601-a9c1-5ebcf756218e"
}
```
