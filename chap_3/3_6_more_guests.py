guests = ["scarlet johansson", "charlie chaplin", "charlize teron", "megan fox"]
changed_guest = guests.pop()
guests.append("jennifer lawrence")
guests.insert(0, "dua lipa")
guests.insert(3, "audrey hepburn")
guests.append("paul newman")

removed_guest = guests.pop()
print(f"Dear {removed_guest.title()}, \nUnfortunately the table will not delivered on time and I won't be able to arrange the dinner. \nCiao,\nCarlo")
print()
removed_guest= guests.pop()
print(f"Dear {removed_guest.title()}, \nUnfortunately the table will not delivered on time and I won't be able to arrange the dinner. \nCiao,\nCarlo")
print()
removed_guest= guests.pop()
print(f"Dear {removed_guest.title()}, \nUnfortunately the table will not delivered on time and I won't be able to arrange the dinner. \nCiao,\nCarlo")
print()
removed_guest= guests.pop()
print(f"Dear {removed_guest.title()}, \nUnfortunately the table will not delivered on time and I won't be able to arrange the dinner. \nCiao,\nCarlo")
print()
removed_guest= guests.pop()
print(f"Dear {removed_guest.title()}, \nUnfortunately the table will not delivered on time and I won't be able to arrange the dinner. \nCiao,\nCarlo")
print()
#Only 2 remained
print()
print(f"Hello {guests[0].title()}, \nI would like to confirm you the dinner at my place tomorrow evening.\nI'm looking forward to see you.\nCiao,\nCarlo")
print()
print(f"Hello {guests[1].title()}, \nI would like to confirm you the dinner at my place tomorrow evening.\nI'm looking forward to see you.\nCiao,\nCarlo")
print()
#I found a bigger dinner table, so I added 3 new gests 
print()
print(f"{changed_guest.title()} will not able to join us")
print()
print("I found a bigger dinner table and I could invite three more people")
print("Unfortunately the new bigger dinner table won't arrive on time and I have space for only two people")
print()
del guests[0]
del guests[0]
print(guests)