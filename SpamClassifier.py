# %%
import glob as gb
ham=gb.glob("spam_ham_mails/ham/*.txt")
spam=gb.glob("spam_ham_mails/spam/*.txt")
main_dict={}
def test_classifier(test_file,y,words_main):
    for file in test_file:
        h=1
        s=1
        words=get_words(file)
        for w in words_main:
            w=w.lower()
            if ham_words.get(w)!=None and w in words:
                h1=ham_words[w]/total_ham
                h=h*h1
            elif w in ham_words:
                h1=ham_words[w]/total_ham
                h1=1-h1
                h=h1*h
            if spam_words.get(w)!=None and w in words:
                s1=spam_words[w]/total_spam
                s=s*s1
            elif w in spam_words:
                s1=spam_words[w]/total_spam
                s1=1-s1
                s=s*s1
        if(h*y>s*(1-y)):
            print("0")
        else:
            print("1")
def get_words(file):
    f=open(file,'r', errors="ignore")
    words=f.read()
    f.close()
    words=words.replace("\n"," ").split(" ")
    return set(words)
ham_words={}
ham_files=[]
total_ham=0
init=1
temp=1
for file in ham:
    words=get_words(file)
    ham_files.append(words)
    for w in words:
        if w.isalpha():
            w=w.lower()
            if ham_words.get(w)==None:
                ham_words[w]=init
                temp+=1
                main_dict[w]=init
            else:
                ham_words[w]=ham_words[w]+init
                temp-=1
                main_dict[w]=main_dict[w]+init
    total_ham+=1
spam_words={}
total_spam=0
spam_files=[]
for file in spam:
    words=get_words(file)
    spam_files.append(words)
    for w in words:
        if w.isalpha():
            w=w.lower()
            if w not in main_dict:
                main_dict[w]=0
            if spam_words.get(w)==None:
                spam_words[w]=1
            else:
                main_dict[w]+=1
                spam_words[w]+=1
    total_spam+=1
words_main = sorted(main_dict,key=main_dict.get,reverse=True)[:2000]
y=total_ham/(total_ham+total_spam)
test=gb.glob("test/*.txt")
test_classifier(test,y,words_main)



# %%



