# Create Account Endpoint

Creates a new account with the given `username` and `password`. Requires a `creation_key`, a **one-time-use** GUID provided to the new user.

*User creation can be done through the provided `/create_account/` page. It doesn't need to be implemented by the front-end.*

**URL** : `/create_account/create`

**Method** : `POST`

**Query Params** :

* `creation_key`
* `username`
* `password`

## Success Response

**Code** : `200 OK`
