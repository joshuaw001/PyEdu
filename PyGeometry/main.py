import turtle as t

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.style = None
		self.rendered = False
	def draw(self):
		t.goto(self.x,self.y)
		t.dot()
		self.rendered = True
	def __del__(self):
		self.draw()
		t.undo()
		self.rendered = False

class LineSegment:
	pass
