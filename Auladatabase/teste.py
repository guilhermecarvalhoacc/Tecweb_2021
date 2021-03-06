from database import Note,Database
note = Note(123,"dani","bestola")
print("INSERT INTO note (title,content) VALUES (note.title,note.content);")

db = Database('banco_novo')

db.add(note)

