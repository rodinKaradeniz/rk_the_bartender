SELECT password_hash
FROM users
WHERE username = %(username)s;