# paw = input('請輸入密碼：')


      # while paw == 'a123456':
      #   paw = input('請輸入密碼：')
      #   n = 2
      #   while n > 0 :
      #     print('密碼錯誤！！ 還有', n,'次機會')
      #     n = n - 1
      #     print('密碼錯三次了')
      #   print('登入成功')
# n = 3
# while True:
#   paw = input('請輸入密碼：')
#   if paw == 'a123456':
#     print('登入成功')
#     if n > 0 :
#       print('密碼錯誤！！ 還有', n,'次機會')
#       n = n - 1
password = 'a123456'
n = 3
while n > 0:
  n = n - 1
  pwd = input('請輸入密碼：')
  if pwd == password:
    print('登入成功')
    break
  else:
    print('密碼錯誤！')
    if n > 0:
      print('還有', n, '次機會')
    else:
      print('密碼錯三次了')

  