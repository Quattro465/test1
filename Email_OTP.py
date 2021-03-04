import smtplib                                      # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage              # Изображения

import random

random_num = random.randint(3456, 9999)

addr_from = "papper.team673@gmail.com"                # Адресат
addr_to = input("To: ")                                   # Получатель
password  = "papper.pass.6738"                                  # Пароль

msg = MIMEMultipart()                               # Создаем сообщение
msg['From']    = addr_from                          # Адресат
msg['To']      = addr_to                            # Получатель
msg['Subject'] = 'Подтверждение почты'                   # Тема сообщения

body = "Подтвердите вашу почту"
msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

html = """\
<html>
 
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
   <title>Tutsplus Email Newsletter</title>
   <style type="text/css">
    a {color: #d80a3e;}
  body, #header h1, #header h2, p {margin: 0; padding: 0;}
  #main {border: 1px solid #cfcece;}
  img {display: block;}
  #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
  #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
  #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
  h5 {margin: 0 0 0.8em 0;}
    h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
  p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
   </style>
</head>
 
<body>
 
<table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
<table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p><a href="#">View in Browser</a></p>
      </td>
    </tr>
  </table>
 
<table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
    <tr>
      <td>
        <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
          <tr>
            <td width="570" align="center"  bgcolor="#d80a3e"><h1>Papper Team</h1></td>
          </tr>
          <tr>
            <td width="570" align="right" bgcolor="#d80a3e"><p>Подтвердите почту</p></td>
          </tr>
        </table>
      </td>
    </tr>
 
    <tr>
      <td>
        <table id="content-3" cellpadding="0" cellspacing="0" align="center">
          <tr>
              <td width="15"></td>
            <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="https://c4.wallpaperflare.com/wallpaper/391/1021/87/4k-apple-think-different-logo-wallpaper-preview.jpg" width ="250" height="150" />
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table id="content-4" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td width="200" valign="top">
              <h5>Подтвердите почту</h5>
          </tr>
        </table>
      </td>
    </tr>
     
 
  </table>
  <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p>Design better experiences for web & mobile</p>
        <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
      </td>
    </tr>
  </table><!-- top message -->
</td></tr></table><!-- wrapper -->
 
</body>
</html>

"""
#<div class=ex1><h1>Papper Team</h1></div>

msg.attach(MIMEText(html, 'html', 'utf-8'))         # Добавляем в сообщение HTML-фрагмент

server = smtplib.SMTP('smtp.gmail.com', 587)        # Создаем объект SMTP
server.starttls()                                   # Начинаем шифрованный обмен по TLS
server.login(addr_from, password)                   # Получаем доступ
server.send_message(msg)                            # Отправляем сообщение
server.quit()                                       # Выходим