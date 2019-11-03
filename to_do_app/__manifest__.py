{
 'name': 'todo',
 'description': 'This is an App that will allow use to store a todo list',
 'author': 'Tomas Hegewisch',
 'depends': ['base'],
 'application': True,
 'data': [
     'security/todo_decurity.xml',
     'security/ir.model.access.csv',
     'views/todo_menu.xml',
     'views/item.xml',
     'views/person.xml',
     'views/dependent.xml',
 ],
 'demo': [
    'data/todo.dependent.csv',
    'data/todo.item.csv',
    'data/todo.person.csv',
],

}

