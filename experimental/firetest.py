from firebase import firebase

if __name__=="__main__":
    firebase = firebase.FirebaseApplication('https://plussteam.firebaseio.com', None)
    result = firebase.get('/users', None)
    values = result.values()
    vec = {}
    for i in values:
        name = i.get(u"firstName")
        major = i.get(u"major")
        if name != None and major != None:
            vec[i.get(u"firstName").encode("utf8")] = i.get(u"major").encode("utf8")
    print vec
