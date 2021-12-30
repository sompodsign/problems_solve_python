import pickle

Shampad = {'Name': 'Shampad', 'age': '45', 'pay': '50k'}

db = {}
db['Shampad'] = Shampad

dbfile = open('examplepickle', 'ab')

pickle.dump(db, dbfile)
dbfile.close()

dbfile = open('examplepickle', 'rb')

db = pickle.load(dbfile)

print(db)