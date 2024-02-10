import ezgmail

keywords = ['Swiggy', 'Udemy', 'Zomato']
for keyword in keywords: 
   threads = ezgmail.search()
   print(f'There are {len(threads)} emails with the keyword, {keyword}')
   ezgmail.summary(threads) #You can check a summary just to make sure you’re not deleting anything important
   for i in range(len(threads)):
       if len(threads)==0:
          print('No \'{keyword}\' messages to delete, moving on to the next')
       else:
         print('Deleted Email \'{i}\' of \'{keyword}\'')
         threads[i].trash()
