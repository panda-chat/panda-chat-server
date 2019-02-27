# Authentication

User accounts are provided manually by giving a `creation_key` to each new user. The client can then use that `creation_key` to create a username/password combination for that user account using the [Create Account endpoint](create_account.md).

After a username/password combination is created, the client can login using the [Login endpoint](login.md). This endpoint returns an `auth_token`, which is required to use all non-authentication endpoints/connections. **Authentication tokens live forever.** If the client keeps the authentication token (for example, as a cookie), the client should never have to login again -- obviously this is valuing convenience over security.
