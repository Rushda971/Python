import mysql.connector
# is program main sirf cconnection create hogya
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )
print(mydb)
'''localhost sirf yeh batata hai ki server kahaan hai
Lekin username batata hai ki kaun access kar raha hai
Agar username/password nahi diya, toh server bolega:
"pehle apni identity batao"
Socho tum ek website bana rahe ho:

Tumne ek database banaya users ka
Ab:
Website ka backend → app_user use karega
(sirf read + write)
Admin ka kaam → root karega
(full control)

👉 Agar backend ko root de diya:

galti se pura database delete bhi ho sakta hai 😅
4️⃣ Authentication kyu zaroori hai (localhost pe bhi)?

Ab main point 👇

Chahe server localhost pe hi kyu na ho:

system ko yeh pata hona chahiye:
kaun access kar raha hai
usko kya karne ki permission hai

Agar authentication na ho:

koi bhi program connect karke data chhed sakta hai ❌'''

