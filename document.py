import htmldeparser
from collections import Counter
import urllib2
import string
import similarity

#TODO: Make DocumentSpace more efficient


class Document(object):
    """
    Document class stores strings and the frquency of the words in it
    """
    def __init__(self, doc):
        self.doc = doc.lower()
        self.frequency = Counter(self.doc.split()).most_common()
    def getFrequency(self):
        return self.frequency
    def getDoc(self):
        return self.doc

class DocumentSpace(object):
    """
    DocumentSpace determines the space that two documents lie in and then converts two documents into vectors. This is useful for the similarity modules of PUGS
    """
    def __init__(self, doc1, doc2):
        list1 = [x[0] for x in doc1.getFrequency()]
        list2 = [x[0] for x in doc2.getFrequency()]
        self.spaces = list(set(list1 + list2))
        ##This is a terrible hack.I need to make this more efficient
        vec1 = []
        vec2 = []
        dict1 = dict(doc1.getFrequency())
        dict2 = dict(doc2.getFrequency())
        for i in self.spaces:
            if i in dict1:
                vec1.append(dict1[i])
            else:
                vec1.append(0)
            if i in dict2:
                vec2.append(dict2[i])
            else:
                vec2.append(0)
        self.vec1 = vec1
        self.vec2 = vec2

    def getvec1(self):
        return self.vec1
    def getvec2(self):
        return self.vec2

def htmltodoc(url):
    response = urllib2.urlopen(url)
    html = response.read()
    html = htmldeparser.dehtml(html)
    return html

def main():
    doc1 = Document(htmltodoc('https://docs.python.org/2/howto/urllib2.html'))
    doc2 = Document(htmltodoc('http://www.aaronsw.com/2002/html2text'))
    space = DocumentSpace(doc1, doc2)
    print similarity.cosine(space.getvec1(), space.getvec2())


if __name__=="__main__":
    main()
