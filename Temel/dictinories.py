# -*- coding: utf-8 -*-

sozluk={
        "book":"kitap",
        "table":"masa"
        }

sozluk2=dict(kitap="book",masa="table")


sozluk["book"] ="kitap1"
print(sozluk["book"])
sozluk["pencil"] = "kalem"
print(sozluk)
del(sozluk["book"])
print(sozluk)
