code={'A':'Z','B':'Y','C':'X','D':'W','E':'V',
      'F':'U','G':'T','H':'S','I':'R','J':'Q',
      'K':'P','L':'O','M':'N','N':'M','O':'L',
      'P':'K','Q':'J','R':'I','S':'H','T':'G',
      'U':'F','V':'E','W':'D','X':'C','Y':'B',
      'Z':'A'}
class Crypt:
    def __init__(self):
        print("WELCOME TO ATBASH CIPHER!!!")
    def cryption(self):
        print("ENTER THE TEXT TO BE "+choice.upper()+"ED:")
        s=input()
        words=list(s)
        length=len(words)
        message=''
        for j in range(0,length):
            if(words[j].isupper()):
                if (words[j].isalpha()):
                    message += code[words[j]]
                else:
                    message += words[j]
            else:
                if(words[j].isalpha()):
                    message +=code[words[j].upper()].lower()
                else:
                    message += words[j]
        print(choice.upper()+"ED TEXT IS:"+message)    
        
c=Crypt()
choice=input("ENTER YOUR CHOICE TO PERFORM ENCRYPT/DECRYPT:")
if choice.lower()=="encrypt":
    c.cryption()
elif choice.lower()=="decrypt":
    c.cryption()
else:
    print("YOUR CHOICE IS WRONG ENTER THE CORRECT CHOICE.")
