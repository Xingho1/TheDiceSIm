import kivy
import functions
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file("kivy stuff/design.kv")
Window.size = (999,635)


class body(Widget):

    # def desliding(self):
    #     l = [self.face1, self.face2, self.face3, self.face4, self.face5]
    #     if functions.num_dice < f:
    #         for n, t in zip(range(f,f-2,-1), l.reverse()):
    #             t.source = ""
    #             f -= 1

    def sliding(self,*args):
        global f
        f = 0
        functions.config(int(args[1]))
        #self.add_widget(Image(source= "kivy stuff/1.png", keep_ratio= True, size_hint= (None, None) size= (200, 200),pos_hint= {"center_x": 0.5}))
        l = [self.face1, self.face2, self.face3, self.face4, self.face5]
        if functions.num_dice > 1:
            for n,t in zip(range(1,functions.num_dice+1),l):
                t.source = "kivy stuff/1.png"
                f += 1
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
