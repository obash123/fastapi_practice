from model import Todo
todos = [
    Todo(id=1,title="flyhigh",description="the alchemist",completed=False),
    Todo(id=2,title="Wolf",description="Tyler the creator",completed=True),
    Todo(id=3,title="mm Food",description="MF DOOM",completed=False)
]

def id_check(id):
    for i in todos:
        if i.id == id:
            return i 
