class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
        
    def type_text(self,new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()
        print(f"Text after typing: {self.text}")
        self.display_all()
        
    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
            print(f"Text after undo: {self.text}")
            self.display_all()
        else:
            print("Nothing to undo")
            
    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
            print("Redo: ",self.text)
            self.display_all()
        else:
            print("Nothing to redo")
            
    def display_all(self):
        print(f"display all: {self.text}\n")
        
editor = TextEditor()
editor.type_text("hello")
editor.type_text("world")
editor.undo()
editor.undo()
editor.redo()