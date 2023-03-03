import kivy
import functions
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file("kivy stuff/design.kv")
Window.size = (999,635)


class body(Widget):
    current_val = 1 

    def function_check(self,*args):
        if args[1] < self.current_val:
            self.desliding(args[1])
        elif args[1] > self.current_val:
            self.sliding(args[1])
    

    def desliding(self,x):

        functions.config(int(x))
        l = [self.face1, self.face2, self.face3, self.face4, self.face5]
        if functions.num_dice < 5:
            self.current_val = functions.num_dice
            l[x].source = ""
        self.num_die.text = "Number of Dice in use: {}".format(functions.num_dice)
        

    def sliding(self,x):
        
        functions.config(int(x))
        l = [self.face1, self.face2, self.face3, self.face4, self.face5]
        if functions.num_dice <= 5:
            self.current_val = functions.num_dice
            l[x-1].source = "kivy stuff/1.png"
        self.num_die.text = "Number of Dice in use: {}".format(functions.num_dice)
            
    
    def rolling(self):
        x = functions.roll()
        self.face1.source = "kivy stuff/{}.png".format(x[0])
        l = [self.face1,self.face2,self.face3,self.face4,self.face5]
        if functions.num_dice > 1:
            for n,t in zip(range(1,(functions.num_dice+1)),l):
                t.source = "kivy stuff/{}.png".format(x[n-1])

        

class Die_roller(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return body()
    
if __name__ == "__main__":
    Die_roller().run()
