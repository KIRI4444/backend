# from config import *

# def adduser(id, email, hash_password):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT COUNT() as 'count' FROM user_login WHERE email LIKE ?''', (str(email),))
#     conn.commit()
#     res = cursor.fetchone()
#     if res[0] > 0:
#       print('Пользователь с такой почтой уже существует')
#       return -1
#     cursor.execute('''INSERT INTO user_login (user_id, email, password) VALUES (?, ?, ?)''', (id, email, hash_password),)
#     conn.commit()
#     conn.close()
#   except Exception as e:
#     return "Ошибка! " + str(e)



# def register_user():
#   try:
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     if not email or not password:
#       return jsonify('error: Не все данные заполнены')
#     else:
#       hash_password = generate_password_hash(str(password))
#       conn = sqlite3.connect('database.db')
#       cursor = conn.cursor()
#       cursor.execute("SELECT user_id from user_login")
#       conn.commit()
#       users_from_db = cursor.fetchall()
#       id = 0 if len(users_from_db) == 0 else users_from_db[-1][0] + 1
#       conn.close()
#       adduser(id, email, hash_password)
#       return jsonify(id)
#   except Exception as e: 
#     return jsonify({'error: Ошибка при регистрации пользователя'})


# def login():
#   try:
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     if not email or not password:
#       return jsonify('error: Не все данные заполнены')
#     cursor.execute('''SELECT COUNT() as 'count' FROM user_login WHERE email LIKE ?''', (str(email),))
#     conn.commit()
#     res = cursor.fetchone()
#     if res[0] > 0:
#       cursor.execute('''SELECT password FROM user_login WHERE email LIKE ?''', (str(email),))
#       conn.commit()
#       a = cursor.fetchall()
#       if check_password_hash(a[0][0], str(password)):
#         login_status = 0
#         cursor.execute('''SELECT user_id FROM user_login WHERE email LIKE ?''', (str(email),))
#         conn.commit()
#         b = cursor.fetchall()
#         conn.close()
#         return jsonify({"login_status": login_status, "user_id": b[0][0]})
#       else:
#         login_status = -1
#         list = {"login_status": login_status, "user_id": -1}
#         return jsonify(list) 
#     else:
#       login_status = -2
#       list = {"login_status": login_status, "user_id": -2}
#       return jsonify(list)

#   except Exception as e:
#     return f"Суета + {e}"




# def send_form(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * from user_info WHERE user_id LIKE ?', (str(user_id),))
#     conn.commit()
#     user_from_db = cursor.fetchall()
#     conn.close()
#     return jsonify(user_from_db)
#   except Exception as e:
#     return "Ошибка" + str(e)





# def get_form(user_id, name, surname, age, sex, about, telegram):
#   try : 
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO user_info (name, surname, age, sex, about, telegram) VALUES (?, ?, ?, ?, ?, ?)''', (str(name), str(surname), str(age), str(sex), str(about), str(telegram)))
#     conn.commit()
#     form_from_db = cursor.fetchall()
#     conn.close()
#     return jsonify(form_from_db)
#   except Exception as e:
#     return "Ошибка" + str(e)



# def set_admin(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO user_login (role) VALUES ?''', str('1'),)
#     conn.commit()
#     conn.close()
#     print('Пользователь' + str(user_id) + 'успешно стал админом')
#     return '1'
#   except Exception as e:
#     return "Ошибка" + str(e)




# def delete_admin(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO user_login (role) VALUES ?''', str('0'),)
#     conn.commit()
#     conn.close()
#     print('Пользователь' + str(user_id) + 'перестал стал админом')
#     return '1'
#   except Exception as e:
#     return "Ошибка" + str(e)



# def add_agreement(user_id, during):
#   try:
#     conn = sqlite3.connect('databas.db')
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO meetings_on_week (user_id, during) VALUES (?, ?)''', (str(user_id), during))
#     cursor.execute('''INSET INTO meetings_on_week (meetings_count) VALUES (?)''', get_user_meetings_count(user_id))
#     conn.commit()
#     conn.close()
#     print('Пользователь' + str(user_id) + 'успешно согласился на встречу длительность' + str(during))
#     return 1
#   except Exception as e:
#     return "Ошибка" + str(e)



# def get_user_meetings_count(user_id, methods=['GET']):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT COUNT() as 'count' FROM  meetings WHERE user_id_1 LIKE ? OR user_id_2 LIKE (?)''', (str(user_id)),)
#     conn.commit()
#     count_meetings = cursor.fetchone()
#     conn.close()
#     return count_meetings
#   except Exception as e:
#     return "Ошибка" + str(e)





# def check_my_meetings(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT COUNT() as 'count' FROM meetings WHERE (user_id_1 LIKE ? OR user_id_2 LIKE ?) AND status LIKE ? ''', ((str(user_id)), 0))
#     conn.commit()
#     count_meetings = cursor.fetchone()
#     conn.close()
#     if count_meetings > 0:
#       return 1
#     else:
#       return 0
#   except Exception as e:
#     return "Ошибка" + str(e)




# def send_form_if_meeting(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT user_id_1, user_id_2 FROM meetings''')
#     conn.commit()
#     a = cursor.fetchall()

#     if a[0][0] == user_id:
#       user_id_form = a[0][1]
#     else:
#       user_id_form = a[0][0]

#     cursor.execute('''SELECT name, surname, age, sex, about, telegram FROM user_info WHERE user_id LIKE ?''', (str(user_id_form),))
#     conn.commit()
#     b = cursor.fetchall()
#     print(f'Пользователю {user_id} пришла анкета напарника ({user_id_form})')
#     conn.close()
#     return jsonify(b)

#   except Exception as e:
#     return "Ошибка" + str(e)



# def was_meeting(status):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO meetings (status) VALUES (?) ''', (str(status)),)
#     conn.commit()
#     print('Статус встречи успешно изменен')
#     conn.close()
#     return 1
#   except Exception as e:
#     return "Ошибка" + str(e)





# def create_random_meeting():
#   try:
#       conn = sqlite3.connect('database.db')
#       cursor = conn.cursor()

#       cursor.execute('''SELECT user_id, during, meetings_count FROM meetings_on_week''')
#       rows = cursor.fetchall()
#       during_dict = {}
#       for row in rows:
#           user_id, during, meetings_count = row
#           if during not in during_dict:
#               during_dict[during] = []
#           during_dict[during].append((user_id, meetings_count))

#       for during, users in during_dict.items():
#           if len(users) % 2 != 0:
#               users.sort(key=lambda x: x[1])
#               users.pop()
#           random.shuffle(users)
#           while len(users) >= 2:
#               user1 = users.pop()
#               user2 = users.pop()
#               cursor.execute('''INSERT INTO meetings (user_id_1, user_id_2, during) VALUES (?, ?, ?)''',
#                              (user1[0], user2[0], during))
#               cursor.execute('''DELETE FROM meetings_on_week WHERE user_id IN (?, ?)''', (user1[0], user2[0]))
#               conn.commit()

#       conn.close()
#       return "Встречи созданы"
#   except Exception as e:
#       return "Ошибка: " + str(e)




# def schedule_meeting():
#   create_random_meeting()




# def user_meeting(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT user_id_1, user_id_2, during FROM meetings WHERE (user_id_1 LIKE ? OR user_id_2 LIKE ?) AND status = 0 ''', (str(user_id),))
#     conn.commit()
#     a = cursor.fetchall()
#     conn.close()
#     return jsonify(a)
#   except Exception as e:
#     return "Ошибка" + str(e)




# def get_all_users():
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT user_id FROM user_login''')
#     conn.commit()
#     a = cursor.fetchall()
#     conn.close()
#     return jsonify(a)
#   except Exception as e:
#     return "Ошибка" + str(e)




# def user_meeting_history(user_id):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT user_id_1, user_id_2, during FROM meetings WHERE (user_id_1 LIKE ? OR user_id_2 LIKE ?) AND status = 1 ''', (str(user_id)),)
#     conn.commit()
#     a = cursor.fetchall()
#     conn.close()
#     return jsonify(a)
#   except Exception as e:
#     return "Ошибка" + str(e)



# def check_users():
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT * from user_login''')
#     a = cursor.fetchall()
#     return a
#   except Exception as e:
#     return "Ошибка! " + str(e)


# def adduser(id, email, hash_password):
#   try:
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''SELECT COUNT() as 'count' FROM user_login WHERE email LIKE ?''', (str(email),))
#     conn.commit()
#     res = cursor.fetchone()
#     if res[0] > 0:
#       print('Пользователь с такой почтой уже существует')
#       return -1
#     cursor.execute('''INSERT INTO user_login (user_id, email, password) VALUES (?, ?, ?)''', (id, email, hash_password),)
#     conn.commit()
#     conn.close()
#   except Exception as e:
#     return "Ошибка! " + str(e)