fav_books=["Qur'an","AGIR","The Alchemist","The 10X Rule","The 4-Hour Workweek"]
book=input("    >    ")
if book in fav_books:
    print(f"{book} is one of my favourite books too")
else:
    print("I haven't read that book")