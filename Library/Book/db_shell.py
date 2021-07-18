from Book.models import Book
# exec(open('D:\\Django\\Library\\Book\db_shell.py').read())
# aa_data=Book.objects.all()
# print(aa_data)

# sid=1
# b2=Book.objects.get(id=sid)
# print(b2)

# b3=Book.objects.create(name="oracle",author="jbsdh",qty=12,price=345)
# print(b3.id)


# all_data=Book.objects.all()
# for book in all_data:
#     print("---------Details for ID Number",book.id,"-----")
#     print("Book Name:-",book.name)
#     print("Author Name:-",book.author)
#     print("Quantity:-",book.qty)
#     print("price per Book:-",book.price)
    # book.qty=15
    # book.save()
import random  
for i in range(1,36):
    b=Book(name=chr(random.randint(65,90))*5,author="abc",qty=random.randint(15,85),price=random.randint(100,900))
    b.save()