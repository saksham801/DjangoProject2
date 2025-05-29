

import pymongo


def login_data(name,password,email,age,phone_no,user_name):
    client = pymongo.MongoClient("mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute")
    db = client['Adhyayan_Coaching_Institute']
    collection = db['login_user']


    dict = {}
    dict['name'] = name
    dict['password'] = password
    dict['Emails'] = email
    dict['user_name'] = user_name
    dict['age'] = age
    dict['phone_no'] = phone_no


    collection.insert_one(dict)


