import getpass

# ログイン名の取得
#user = getpass.GetPassWarning()
user = getpass.getuser()
# 取得したログイン名を表示
print(f'getpass.getuser() = {user}')
