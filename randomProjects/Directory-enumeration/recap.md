# Dir Enumeration Tool - Basics

- Read paths from a file
- Sanitize each path: .strip().lstrip('/')
- Build full URL: url.rstrip('/') + '/' + dir.lstrip("/")
- Send GET request with requests
- If 200 OK, save to output file
- Understood use of in -> [301,302] instead of using or
- Catch errors (FileNotFound, RequestException, etc.)
