# import hashlib
# import re
#
#
# def encrypt(passwd):
#     return hashlib.md5(passwd.encode(encoding='UTF-8')).hexdigest()
#
#
# def match(char, rule, err):
#     try:
#         re.match(rule, char)
#         return True
#     except:
#         return err
#
#
# def create_user(username, passwd, email):
#     match(r'^[-_a-zA-Z0-9]{4,16}$', 'james_', '用户名不符合规则')
#     isinstance(match(r'^[a-zA-Z0-9]{1,10}@[a-zA-Z0-9]{1,5}\.[a-zA-Z0-9]{1,5}$', email, '邮箱格式不对'), bool)
#     pass
#
#
# def delete_user(username, passwd):
#     pass
#
#
# def change_passwd(username, passwd):
#     pass

