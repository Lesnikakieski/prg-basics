import turtle

def draw_square(pen, length):
    """Rysuje kwadrat o boku length."""
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    """Rysuje trójkąt równoramienny (tu równoboczny) o boku length."""
    for _ in range(3):
        pen.forward(length)
        pen.left(120)   # 3 * 120° = 360°

def draw_rectangle(pen, length_a, length_b):
    """Rysuje prostokąt o bokach length_a i length_b."""
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)