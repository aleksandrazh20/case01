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
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)

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
    turtle.left(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(180)

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
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)

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
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)

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
    turtle.right(90)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)

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
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)


def triangle_type_3(x, y, a) :

    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :return: None
    '''

    turtle.up()
    turtle.setposition(x,y)
    turtle.forward(a)
    turtle.right(90)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward((a*a*2)**0.5)
    turtle.right(45)



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
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)

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
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)

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
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)

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
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)


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
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)

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
    turtle.right(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)



def fish():
    triangle_type_3(-199, 299, 60)
    triangle_type_8(-200, 360, 60)
    rectangle_type_1(-198, 322, 33)
    triangle_type_2(-135, 330, 50)
    rectangle_type_4(-240, 323, 30, 30)
    triangle_type_7(-220, 300, 18)
    triangle_type_3(-241, 300, 18)



def fly() :
    rectangle_type_2(-250, -10, 30, 30)
    triangle_type_5(-313, -30, 30)
    triangle_type_2(-273, -30, 60)
    triangle_type_4(-272, -30, 60)
    triangle_type_5(-336, -92, 30)
    triangle_type_1(-356, -71, 30)
    rectangle_type_1(-405, -42, 30)



def rabbit() :
  rectangle_type_4(-600, 380, 40, 70)
  square(-520, 325, 70)
  triangle_type_3(-665, 290, 140)
  triangle_type_7(-665, 145, 140)
  triangle_type_2(-520, 180, 50)
  triangle_type_3(-665, 90, 90)
  triangle_type_6(-570, 60, 60)



def person() :
    rectangle_type_1(450, 380, 70)
    triangle_type_8(410, 280, 110)
    triangle_type_7(520, 280, 110)
    triangle_type_3(450, 170, 70)
    triangle_type_6(520, 170, 70)
    triangle_type_8(560, 97, 50)
    triangle_type_3(440, 97, 50)



def ship() :
    triangle_type_6(100, -10, 50)
    triangle_type_2(100, -60, 90)
    triangle_type_3(15, -80, 80)
    triangle_type_5(105, -190, 50)


ship()