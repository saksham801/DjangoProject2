import pymongo

client = pymongo.MongoClient("mongodb+srv://dubeysaksham796:Iron_Man@adhyayancoachinginstitu.hqcuhrf.mongodb.net/?retryWrites=true&w=majority&appName=AdhyayanCoachingInstitute")
db = client['Adhyayan_Coaching_Institute']
collection = db['course']

def course_name(name,des,url):
    dict = {}

    dict['name_course'] = name
    dict['description'] = des
    dict['image_url'] =  url

    collection.insert_one(dict)

