# Odoo_Winlands_College
The Odoo Project for Socio Informatics 354
# GROUP MEMBERS:
## Andrew Prenter - 20456395
## Ayaaz Mullajie - 19772815
## Bennie Wiemamm - 23725648
## Tomas Hegewisch - 21071926
----------------------------------------------------



# --- INSTRUCTIONS ---
## Install: 
./oddo-bin -d winelands -i winlands_college_bas_module,college_admin,results_managment

## Login:
User:admin
Password: password

## List of users for Richard

1. For Richard Admin:
- email: 49@cwc.ac.za
- Password: password

2. For Richard Student:
- email: 110@cwcw.ac.za
- password: password

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

## Filters:   
1. For Academic Staff:     
- Modules   
  • Modules taught by Academic Staff: Filters all Modules to only the modules that the Academic Staff are lecturing   
  • Modules this year: Filters all Modules to only show the modules being lectured this year    
- Students   
  • In Department: Filters Students to show only he ones in the same department as the staff member   
  • Being taught: Filter students to show only the ones being taught by specific lectures   
- Marks    
  • Current year: Filters the Marks to only show the ones of the current year   
  • No Mark allocated yet: Filters the Marks to only show the ones that have an allocated mark   
  • Received a mark: Filters the Marks to only show the ones that have an allocated Mark
  
2. For Student   
- Modules   
  • Modules this year: Filters all Modules to show only the ones that are lectured this year  
- Marks   
  • Current year: Filters the Marks to only show the ones of the current year   
  • No Mark allocated yet: Filters the Marks to only show the ones that have an allocated mark   
  • Received a mark: Filters the Marks to only show the ones that have an allocated Mark  
  • Passed: Filters the Marks to only show the Marks over 50%  • Failed: Filters the Marks to only show the Marks below 50

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
 - Select the button create 
 - Fill in the respective fields 
 
3.	Student user:
 - Click on College Admin module
 - Click on Admin Staff listed in the header 
 - Select the button create 
 - Fill in the respective fields 

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

