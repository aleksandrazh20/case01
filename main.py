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

def main() :
    pass

import turtle


def triangle_type_2(x, y, a, color) :
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

def triangle_type_5(x, y, a, color) :
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

def rectangle_type_2(x, y, a, b, color) :
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

def triangle_type_1(x, y, a, color):
    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)

def triangle_type_4(x, y, a, color) :
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

def square(x, y, a, color) :
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

def triangle_type_2(x, y, a) :
    '''
    Function, drawing square.
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
    turtle.forward(a*a*2)


def square(x, y, a) :
    '''

    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
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

def triangle_type_6(x, y, a, color) :
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

def triangle_type_6(x, y, a, color) :
    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)

def triangle_type_8(x, y, a, color) :
    b = (a * a + a * a) ** 0.5
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)


def main() :
    square()

main()
