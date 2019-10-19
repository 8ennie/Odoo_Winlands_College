# Odoo_Winlands_College
The Odoo Project for Socio Informatics
# Roles are as followed(Product Owner):
### Views
Andrew
### Security
Tomas
### models
Bennie
### Demo_data
Ayaaz
### Logo
Ayaaz


# Extra features
* Chat function (students and Academic staff)
* Export-to-PDF
* The use of an API external API (like the weather API)
* Text-to-speech function (taking the marks and making it a MP3 file)

# Things to add to BRD - 'features worth trying'
1.	Richard student / Richard admin staff / Richard academic staff 
2.	Auto generated emails and logins 
3.	creating users
4.	limit view for marks for particular students 
5.	ISBN checks 
6.	pen touch description 
7.	allows a student to be registered for a module and module shows how many students are enrolled for each respective module 
8.	staff are restricted to only seeing the modules they are linked to in the department 
9.	Qualification drop down per module 
10.	Text-to-speech function (taking the marks and making it a MP3 file)

# Testing
College admin:
1. create a department 
2. create an admin staff 
3. create a acaddemic staff 
4. create a student 
5. create a program 
6. create a module 

College results:
1. upload a csv file for marks 
2. create student
3. create a module 

Big things:
1. Make sure modules work independently 
2. Be able to create and login as user and only see your respective information
3. Make sure it works on a new odoo (as if Richard were to install)

# Side Note
- departments can only be linked with modules and staff from one way 
- staff/admin get one snazy email because you cant have more than one login

# Comments from testing 
1.	Add title to admin staff
2.	Change order of admin menu: 
  •	Department 
  •	Program 
  •	Module 
  •	Admin staff 
  •	Academic staff 
  •	Student 
3.	Change list for qualification 
4.	We want the staff email address to show 
5.	Students: student table view, amount of modules + email address 
6.	Academic staff: table view, amount of lectured classes 
7.	Link lecturedclass with academic staff (both ways)
8.	Make sure that college admin staff cannot see/edit marks 
9.	In college_results in modules table, add a department column 
10.	Look at search 
11.	Students should only be able to see their own modules when logged in by a student 

All fixed besides 10 and 11

# Comments from testing 2
1.	Change qualification and length (program view in admin)
2.	Change lectured class to lecturer (Module view in admin)
3.	Remove DI from module (module view in admin) 
4.	How many students are in a module (module view in admin)
5.	Remove white spaces from staff email (admin staff view in admin)
6.	Add department to admin staff table (admin staff view in admin) 
