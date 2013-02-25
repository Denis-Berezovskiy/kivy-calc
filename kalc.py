
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty



class Kalc(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)
        self.layout = BoxLayout(orientation='vertical')
        self.layout_b = GridLayout( cols = 4, rows = 4)
        self.textinput = TextInput (multiline=False, border=[10,10,10,10],\
            font_size =100, readonly=True, size_hint=[ 1.0, 0.3])
          
        btn1 = Button(text='1', font_size=50, on_press = self.btn_input) 
        btn2 = Button(text='2', font_size=50, on_press = self.btn_input)
        btn3 = Button(text='3', font_size=50, on_press = self.btn_input)
        btnp = Button(text='+', font_size=50, on_press = self.btn_input) 
        btn4 = Button(text='5', font_size=50, on_press = self.btn_input)
        btn5 = Button(text='4', font_size=50, on_press = self.btn_input)
        btn6 = Button(text='6', font_size=50, on_press = self.btn_input)
        btnm = Button(text='-', font_size=50, on_press = self.btn_input)
        btn7 = Button(text='7', font_size=50, on_press = self.btn_input)
        btn8 = Button(text='8', font_size=50, on_press = self.btn_input)
        btn9 = Button(text='9', font_size=50, on_press = self.btn_input)
        btnx = Button(text='*', font_size=50, on_press = self.btn_input)
        btnc = Button(text='c', font_size=50, background_color=[255,0,0,1] , on_press = self.remove)
        btn0 = Button(text='0', font_size=50, on_press = self.btn_input)
        btnr = Button(text='=', font_size=50, on_press = self.kalcul)
        btnd = Button(text='/', font_size=50, on_press = self.btn_input)    
        self.layout.add_widget(self.textinput)
        self.layout_b.add_widget(btn1)
        self.layout_b.add_widget(btn2)
        self.layout_b.add_widget(btn3)
        self.layout_b.add_widget(btnp)
        self.layout_b.add_widget(btn4)
        self.layout_b.add_widget(btn5)
        self.layout_b.add_widget(btn6)
        self.layout_b.add_widget(btnm)
        self.layout_b.add_widget(btn7)
        self.layout_b.add_widget(btn8)
        self.layout_b.add_widget(btn9)
        self.layout_b.add_widget(btnx)
        self.layout_b.add_widget(btnc)
        self.layout_b.add_widget(btn0)
        self.layout_b.add_widget(btnr)
        self.layout_b.add_widget(btnd)
        self.layout.add_widget(self.layout_b)
        self.add_widget(self.layout)
         
    def btn_input(self,x):
        self.textinput.text+=x.text   
        
    def remove(self,x):
        if x:
            self.textinput.text = self.textinput.text[:-1]  
              
    def kalcul(self,x):
        if not x:
            return
        try :
            self.textinput.text = str(eval(self.textinput.text))
        except:
            self.textinput.text = 'Eror'           
        
        
        
        
class KalcApp(App):
    title = '1234567890'
    def build(self):
        return Kalc() 
             
        
        
if __name__ == '__main__':
    KalcApp().run()        
