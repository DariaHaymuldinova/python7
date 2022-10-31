def import_phone():
      file = 'phone.csv'
      with open (file, 'w', encoding = 'utf-8') as data:
          data.write(f'Фамилия;Имя;Номер телефона;Комментарий\n')