ch=raw_input("enter a character:")
if((ch>='a' and ch<='z') or (ch>'A' and ch<='Z')):
    if(ch=='a'or ch=='i' or ch=='o' or ch=='u' or ch=='e' or ch=='A' or ch=='I' or ch=='O' or ch=='U' or ch=='E'):
                                 print("it is a vowel")
    else:
                                 print("it is consonant")
else:
    print("please enter a valid character")
