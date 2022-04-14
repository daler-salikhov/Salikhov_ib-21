class LeftParagraph:
    def __init__ (self , n):
        self.kol = n
        self.ab = []
 
    def add_word (self , s):
        if len (self.ab) == 0 or len (self.ab[-1]) + len (s) > self.kol - 1:
            self.ab += [s]
        else:
            self.ab[-1] += " " + s
 
    def end (self):
        print (*self.ab , sep="\n")
 
 
class RightParagraph:
    def __init__ (self , n):
        self.kol = n
        self.ab = []
 
    def add_word (self , s):
        if len (self.ab) == 0 or len (self.ab[-1]) + len (s) > self.kol - 1:
            self.ab += [s]
        else:
            self.ab[-1] += " " + s
 
    def end (self):
        for i in self.ab:
            print (" " * (self.kol - len (i)) + i)
lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()