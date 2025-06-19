list=['arko','ridhima','9875 67832','bro.c.ii']
for i in list:
         try: 
          a=i.replace(" ","")
          b=int(a)+1 
          PhoneNumber=a
          break#will have to change.Numbers cant have spaces.Hence number strings with spaces cant be converted to int 
          #if len(i.text)==12:#is also flawed,cuz for one result there was "Find a table" which matches 12 characters.So gotta change this too.
           #PhoneNumber=i.text
           #break
          #else:
           # PhoneNumber="No Value"

         except:
          print("Trouble rendering phone number")
          PhoneNumber="Not present on google business profiles"
print(PhoneNumber)