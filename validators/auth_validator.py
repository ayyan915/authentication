def check_username(username):
    if not username:
        return "enter username"
def check_pass(password):
    if not password:
        return "enter password"
    
def check_pass_len(password):
    pass_len = len(password)
    if pass_len < 8:
        return "password must contain eight character"
    