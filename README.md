Назва: Отримання інформації про курси криптовалют. Використовуємо для цього CoinGecko API.

Опис: Цей приклад демонструє використання CoinGecko API для отримання інформації про поточні курси 
та інші статистичні дані про топ-10 криптовалют за ринковою капіталізацією. За допомогою цього API 
ми можемо отримати назву криптовалюти, її поточний курс у доларах США, а також відобразити цю 
інформацію за допомогою графіку.

Name: Bitcoin, Price: $67379
Name: Ethereum, Price: $3704.36
Name: Tether, Price: $0.999412
Name: BNB, Price: $596.33
Name: Solana, Price: $165.73
Name: Lido Staked Ether, Price: $3704.67
Name: USDC, Price: $0.999693
Name: XRP, Price: $0.528957
Name: Dogecoin, Price: $0.161809
Name: Toncoin, Price: $6.17

![image](https://github.com/Dianadel25/api_laba/assets/102838845/3cc5e40a-6eb0-4b1f-9435-ce65f9f6758f)


Звертання до серверу:
Використовуємо цю адресу: http://127.0.0.1:5000/personal_data?login=is-21fiot-22-038

Сервер видає прізвище, ім'я, курс та групу, а ще звертання містить мій логін від Moodle
{
  "course": "2 course",
  "group": "IC-21",
  "name": "Diana",
  "surname": "Delita"
}
