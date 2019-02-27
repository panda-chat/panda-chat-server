# Create Account Endpoint

Creates a new account with the given `username` and `password`. Requires a `creation_key`, a **one-time-use** GUID provided to the new user.

**URL** : `/create_account`

**Method** : `POST`

**Query Params** :

* `creation_key`
* `username`
* `password`

## Success Response

**Code** : `200 OK`
