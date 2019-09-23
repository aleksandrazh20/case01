# case1
# Vlasov V, Anufrieva A, Zhuravleva A.
def triangle_type_1(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def triangle_type_2(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def triangle_type_3(x, y, a, color):
    # TODO: (Sasha) Paint a triangle.
    pass

def triangle_type_4(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def triangle_type_5(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def rectangle_type_1(x, y, a, color) :
    # TODO: (Sasha) Paint a rectangle.
    pass

def rectangle_type_2(x, y, a, b, color) :
    # TODO: (Nastya) Paint a rectangle.
    pass

def square(x, y, a, color) :
    # TODO: (Nastya) Paint a square.
    pass

def triangle_type_6(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def triangle_type_7(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def triangle_type_8(x, y, a, color) :
    # TODO: (Nastya) Paint a triangle.
    pass

def rectangle_type_3(x, y, a, color) :
    # TODO: (Sasha) Paint a rectangle.
    pass

def rectangle_type_4 (x, y, a, color) :
    # TODO: (Sasha) Paint a rectangle.
    pass
import turtle

def triangle_type_2(x, y, a) :

    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("light blue")
    turtle.fillcolor("light blue")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()

def triangle_type_5(x, y, a) :

    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("pink")
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(180)
    turtle.end_fill()


def rectangle_type_2(x, y, a, b) :

    '''
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rectangle
    :param b: side length of a rectangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.end_fill()

def triangle_type_1(x, y, a):

    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("green")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()

def triangle_type_4(x, y, a) :
    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''
    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("yellow")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()

def square(x, y, a,) :

    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()


def triangle_type_3(x, y, a) :

    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x,y,)
    turtle.forward(a)
    turtle.right(90)
    turtle.down()
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward((a*a*2)**0.5)
    turtle.right(45)
    turtle.end_fill()



def rectangle_type_1(x, y, a) :

    '''
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rectangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x,y)
    turtle.forward(a)
    turtle.down()
    turtle.color("light yellow")
    turtle.fillcolor("light yellow")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()

def triangle_type_6(x, y, a) :

    '''
     Function, drawing triangle.
     :param x: upper left corner coordinate x
     :param y: upper left corner coordinate y
     :param a: side length of a triangle
     :return: None
     '''

    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.end_fill()

def triangle_type_7(x, y, a) :

    '''
     Function, drawing triangle.
     :param x: upper left corner coordinate x
     :param y: upper left corner coordinate y
     :param a: side length of a triangle
     :return: None
     '''

    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("grey")
    turtle.fillcolor("grey")
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def triangle_type_8(x, y, a) :

    '''
     Function, drawing triangle.
     :param x: upper left corner coordinate x
     :param y: upper left corner coordinate y
     :param a: side length of a triangle
     :return: None
     '''

    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("purple")
    turtle.fillcolor('purple')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.end_fill()


def rectangle_type_4(x, y, a, b) :
    '''

    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rectangle
    :param b: side length of a rectangle
    :param color:
    :return: None
    '''

    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.color("light green")
    turtle.fillcolor("light green")
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.end_fill()

def rectangle_type_3(x, y, a, b) :
    '''

    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rectangle
    :param b: side length of a rectangle
    :param color:
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color("orange")
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.end_fill()



def fish():
    triangle_type_3(-199, 299, 60)
    triangle_type_8(-200, 360, 60)
    rectangle_type_1(-198, 322, 33)
    triangle_type_2(-135, 330, 50)
    rectangle_type_4(-240, 323, 30, 30)
    triangle_type_7(-220, 300, 18)
    triangle_type_3(-241, 300, 18)
fish()

def fly() :
    rectangle_type_2(-250, -10, 30, 30)
    triangle_type_5(-313, -30, 30)
    triangle_type_2(-273, -30, 60)
    triangle_type_4(-272, -30, 60)
    triangle_type_5(-336, -92, 30)
    triangle_type_1(-356, -71, 30)
    rectangle_type_1(-405, -42, 30)
fly()

def rabbit() :
  rectangle_type_4(-300, 300, 60, 100)
  square(-180, 227, 90)
  triangle_type_3(-355, 140, 170)
  triangle_type_7(-355, -35, 170)
  triangle_type_2(-180, 0, 50)
  triangle_type_3(-360, -105, 110)
  triangle_type_6(-245, -140, 70)
rabbit()