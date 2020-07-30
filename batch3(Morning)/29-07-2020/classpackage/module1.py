class first:
    def a():
        print("first  class method executed ")
class second(first):   #a,b 
    def b():
        print("second class method executed ")
class three(second):  #a,b,c are the features
    def c():
        print("thrid class method executed")
class four(three):  #a,b,c,d are the features
    def d():
        print("four class method exceuted")