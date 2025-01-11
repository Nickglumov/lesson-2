letter = '''\
frm=' glum0vnick@yandex.ru'
to='nekitglum@gmail.com'
subject='Приглашение'
Content-Type: text/plain; charset="UTF-8";

text="""From:{a}
To:{b}
Subject:{c}
""".format(a=frm,b=to,c=subject)

print(text)
print ("""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл"""
.format(a=frm,b=to,c=subject)
.replace("%website%","https://dvmn.org/profession-ref-program/nekitglum/PNiP3/")
.replace("%friend_name%","Игорь")
.replace("%my_name%","Евгений"))'''

letter = letter.encode("UTF-8")

print(letter)


import smtplib

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login=('glum0vnick@yandex.r', 'm314Gs14')
server.sendmail=("glum0vnick@yandex.ru", 'nekitglum@gmail.com', b'frm=\' glum0vnick@yandex.ru\'\nto=\'nekitglum@gmail.com\'\nsubject=\'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5\'\nContent-Type: text/plain; charset="UTF-8";\n\ntext="""From:{a}\nTo:{b}\nSubject:{c}\n""".format(a=frm,b=to,c=subject)\n\nprint(text)\nprint ("""\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, %friend_name%! %my_name% \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x88\xd0\xb0\xd0\xb5\xd1\x82 \xd1\x82\xd0\xb5\xd0\xb1\xd1\x8f \xd0\xbd\xd0\xb0 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82 %website%!\n\n%website% \xe2\x80\x94 \xd1\x8d\xd1\x82\xd0\xbe \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xb2\xd0\xb5\xd1\x80\xd1\x81\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xbd\xd0\xbb\xd0\xb0\xd0\xb9\xd0\xbd-\xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd0\xb0 \xd0\xbf\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8e. \n\xd0\x98\xd0\xb7\xd1\x83\xd1\x87\xd0\xb0\xd0\xb5\xd0\xbc Python \xd0\xb8 \xd0\xbd\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe. \xd0\xa0\xd0\xb5\xd1\x88\xd0\xb0\xd0\xb5\xd0\xbc \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8. \xd0\x9f\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb0\xd0\xb5\xd0\xbc \xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e \xd0\xbe\xd1\x82 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f. \n\n\xd0\x9a\xd0\xb0\xd0\xba \xd0\xb1\xd1\x83\xd0\xb4\xd0\xb5\xd1\x82 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x85\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb2\xd0\xb0\xd1\x88\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0 %website%? \n\n\xe2\x86\x92 \xd0\x9f\xd0\xbe\xd0\xbf\xd1\x80\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xba\xd1\x83\xd0\xb5\xd1\x88\xd1\x8c\xd1\x81\xd1\x8f \xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xba\xd0\xb5\xd0\xb9\xd1\x81\xd0\xb0\xd1\x85. \n\xd0\x97\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8 \xd0\xbe\xd1\x82 \xd1\x82\xd0\xb8\xd0\xbc\xd0\xbb\xd0\xb8\xd0\xb4\xd0\xbe\xd0\xb2 \xd1\x81\xd0\xbe \xd1\x81\xd1\x82\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbc \xd0\xbe\xd1\x82 10 \xd0\xbb\xd0\xb5\xd1\x82 \xd0\xb2 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8.\n\xe2\x86\x92 \xd0\x91\xd1\x83\xd0\xb4\xd0\xb5\xd1\x88\xd1\x8c \xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x81\xd1\x82\xd1\x80\xd0\xb5\xd1\x81\xd1\x81\xd0\xb0 \xd0\xb8 \xd0\xb1\xd0\xb5\xd1\x81\xd1\x81\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xbd\xd0\xbe\xd1\x87\xd0\xb5\xd0\xb9. \n\xd0\x97\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8 \xd0\xbd\xd0\xb5 \xc2\xab\xd1\x81\xd0\xb3\xd0\xbe\xd1\x80\xd1\x8f\xd1\x82\xc2\xbb \xd0\xb8 \xd0\xbd\xd0\xb5 \xd1\x83\xd0\xb9\xd0\xb4\xd1\x83\xd1\x82 \xd0\xba \xd0\xb4\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xbc\xd1\x83. \xd0\x97\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xb9\xd1\x81\xd1\x8f \xd0\xb2 \xd1\x83\xd0\xb4\xd0\xbe\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb8 \xd1\x80\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xbe \xd1\x81\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe, \xd1\x81\xd0\xba\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x88\xd1\x8c.\n\xe2\x86\x92 \xd0\x9f\xd0\xbe\xd0\xb4\xd0\xb3\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x88\xd1\x8c \xd0\xba\xd1\x80\xd0\xb5\xd0\xbf\xd0\xba\xd0\xbe\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x8e\xd0\xbc\xd0\xb5.\n\xd0\x92\xd1\x81\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd1\x8b \xe2\x80\x94 \xd0\xbe\xd0\xbd\xd0\xb8 \xd0\xb6\xd0\xb5 \xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd1\x88\xd0\xb8\xd1\x85 \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb5\xd0\xba \xe2\x80\x94 \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd1\x82\xd1\x8c \xd0\xbd\xd0\xb0 \xd1\x82\xd0\xb2\xd0\xbe\xd1\x91\xd0\xbc GitHub. \xd0\xa0\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8 \xd1\x82\xd0\xb0\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd1\x8f\xd1\x82. \n\n\xd0\xa0\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd1\x83\xd0\xb9\xd1\x81\xd1\x8f \xe2\x86\x92 %website%  \n\xd0\x9d\xd0\xb0 \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x8b, \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b\xd0\xb5 \xd0\xb5\xd1\x89\xd0\xb5 \xd0\xbd\xd0\xb5 \xd0\xb2\xd1\x8b\xd1\x88\xd0\xbb\xd0\xb8, \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xb8 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb8\xd1\x82\xd1\x8c \xd1\x83\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xbe\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbe \xd1\x80\xd0\xb5\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb5 \xd1\x81\xd1\x80\xd0\xb0\xd0\xb7\xd1\x83 \xd0\xbd\xd0\xb0 \xd0\xb8\xd0\xbc\xd0\xb5\xd0\xb9\xd0\xbb"""\n.format(a=frm,b=to,c=subject)\n.replace("%website%","https://dvmn.org/profession-ref-program/nekitglum/PNiP3/")\n.replace("%friend_name%","\xd0\x98\xd0\xb3\xd0\xbe\xd1\x80\xd1\x8c")\n.replace("%my_name%","\xd0\x95\xd0\xb2\xd0\xb3\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9"))')
server.quit()