truthy_or_faulty=[0,"Hello!"," ","!!",12,True,None,"","0",False,"False"]
for note in truthy_or_faulty:
    if bool(note):
        print(f"{note} is truthy")
    else:
        print(f"{note} is falsy")