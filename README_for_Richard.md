# Odoo_Winlands_College
The Odoo Project for Socio Informatics 354
# GROUP MEMBERS:
## Andrew Prenter - 20456395
## Ayaaz
## Bennie Wiemamm - 23725648
## Tomas Hegewisch - 21071926
----------------------------------------------------



# --- INSTRUCTIONS ---
---------------------------------------------------
# --- FEATURES ---
## Users + permissions:  
1. Academic Staff User: 
 - Username: namesurname extended by “@cwc.ac.za”
 - Password: password

2. Admin staff user:
 - Username: namesurname extended by “@cwc.ac.za”
 - Password: password
 
3. Student user:
Students are provided their own computed login number from the server. This number will allow them to login into the student module in which they will have access to their respective modules (name, length of module and amount of credits) as well as their marks.

## Login details: 
1. Academic Staff User: 
 - Username: namesurname extended by “@cwc.ac.za”
 - Password: password

2. Admin staff user:
 - Username: namesurname extended by “@cwc.ac.za”
 - Password: password
 
3. Student user:
 - Username: number provided by the server extended by “@cwc.ac.za”
 - Password: password

## How to create custom users:  
1. Academic staff user
 - Click on College Admin module
 - Click on Academic Staff listed in the header 
 - Select the button create 
 - Fill in the respective fields 
  
2. Admin staff user:
 - Click on College Admin module
 - Click on Admin Staff listed in the header 
•	Select the button create 
•	Fill in the respective fields 
 
3.	Student user:
•	Click on College Admin module
•	Click on Admin Staff listed in the header 
•	Select the button create 
•	Fill in the respective fields 

## Students can only see their own marks
 
## ISBN constraints: 
1. SQL constraint for the name of the department
2. Constraint in enrolled student so that a students marks cannot be above 100 or below 0
3.	Timeframe constraint to make sure that the timeframe cannot be above 4 or under 0
4.	Credit constraint so that the credits aren’t 0
5.	Constraint on module so that the name cannot be null 
6.	Constraint on the length of the module so that it cannot be longer than 10 years and less than 0  
  
## Computed data: 
1. Amount of credits per student (Results Management Model - Student View) 
2. Amount of staff per department (College Admin Module - Department View)  
3. Amount of modules lectured per academic staff (College Admin Module - Academic Staff View) 
4. Amount of students per module (College Admin Module - Module View)
  
## Drop down program qualifications: 
1. Within the College Admin Module - Program View
2. Shows the available qualifications able to be selected for a program
   
## Pen touch description:
1. Length (College Admin Module - Program View)
2. Timeframe (College Admin Module - Module View)
  
## Academic Staff are restricted to only seeing the modules they are linked to in the department 

------------------------------------------------------------------------------------------------

