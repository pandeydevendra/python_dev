PRD = project requirement Document
'library' book management system
1. manage book details: 
   add, update,delete, record
2. manage students details:
   add, update,delete, record
   
3. issue/activity:
  
4. return book:
   ASK student name-->> SEARCH student id --> 
   GET BOOK_LIST ISSUED TO THE STUDENT........ 
      
   ASK book title --> GET book_id
   check if book is assigned to the student or not...
   if match --> assign h
   Update issue_status , return_date in issues_book_details   
   ASK book title--->>> UPDATE books table with 'available + 1'




x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
print(x)
