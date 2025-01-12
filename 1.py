import smtplib

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login('glum0vnick@yandex.ru', 'm314Gs14')
server.sendmail('glum0vnick@yandex.ru', 'glum0vnick@yandex.ru','letter')
server.quit()


letter="""\
From: glum0vnick@yandex.ru
To: glum0vnick@yandex.ru
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8"

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

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
letter=letter.replace("%website%","https://dvmn.org/profession-ref-program/nekitglum/PNiP3/")
letter=letter.replace("%friend_name%","Игорь")
letter=letter.replace("%my_name%","Евгений")

letter = letter.encode("UTF-8")

print(letter)