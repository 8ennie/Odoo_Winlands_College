# Odoo_Winlands_College
The Odoo Project for Socio Informatics 354
# Group Members:
Andrew Prenter - 20456395
Ayaaz
Bennie Wiemamm - 23725648
Tomas Hegewisch - 21071926




# Instructions for installing the database

# Features
1.  Users + permissions  
-	Academic Staff User: 
•	Username: namesurname extended by “@cwc.ac.za”
•	Password: password

-	Admin staff user:
•	Username: namesurname extended by “@cwc.ac.za”
•	Password: password
 
-	Student user:
Students are provided their own computed login number from the server. This number will allow them to login into the student module in which they will have access to their respective modules (name, length of module and amount of credits) as well as their marks
.   
2. Login details 
-	Academic Staff User: 
•	Username: namesurname extended by “@cwc.ac.za”
•	Password: password

-	Admin staff user:
•	Username: namesurname extended by “@cwc.ac.za”
•	Password: password
 
-	Student user:
•	Username: number provided by the server extended by “@cwc.ac.za”
•	Password: password

3. How to create custom user 
-	Academic staff user
•	Click on College Admin module
•	Click on Academic Staff listed in the header 
•	Select the button create 
•	Fill in the respective fields 
  
-	Admin staff user:
•	Click on College Admin module
•	Click on Admin Staff listed in the header 
•	Select the button create 
•	Fill in the respective fields 
 
-	Student user:
•	Click on College Admin module
•	Click on Admin Staff listed in the header 
•	Select the button create 
•	Fill in the respective fields 
1.	Students can only see their own marks
 
2.	ISBN constraints: 
•	SQL constraint for the name of the department
•	Constraint in enrolled student so that a students marks cannot be above 100 or below 0
•	Timeframe constraint to make sure that the timeframe cannot be above 4 or under 0
•	Credit constraint so that the credits aren’t 0
•	Constraint on module so that the name cannot be null 
•	Constraint on the length of the module so that it cannot be longer than 10 years and less than 0  
  
8	Computed data: 
•	Amount of credits per student (Results Management Model - Student View) 
•	Amount of staff per department (College Admin Module - Department View)  
•	Amount of modules lectured per academic staff (College Admin Module - Academic Staff View) 
•	Amount of students per module (College Admin Module - Module View)
  
9	Drop down program qualifications 
•	Within the College Admin Module - Program View
•	Shows the available qualifications able to be selected for a program
   
10	Pen touch description:
•	Length (College Admin Module - Program View)
•	Timeframe (College Admin Module - Module View)
  
11	Academic Staff are restricted to only seeing the modules they are linked to in the department 

