#find roots
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return (x, x)
    else:
        x1 = (-b + discriminant ** 0.5) / (2*a)
        x2 = (-b - discriminant ** 0.5) / (2*a)
        return (x1, x2)

#find vertex
def find_vertex(a, b, c):
    h = -b / (2*a)
    k = a * h**2 + b * h + c
    return (h, k)

#put into factor form
def factored_form(a, b, c):
    roots = find_roots(a, b, c)
    if roots is None:
        return None
    else:
        x1, x2 = roots
        return f"{a:.1f}(x - {x1:.3f})(x - {x2:.3f})"

#put into vertex form
def vertex_form(a, b, c):
    h, k = find_vertex(a, b, c)
    return f"{a:.1f}(x - {h:.3f})^2 + {k:.1f}"

#put into standard
def standard_form(a, h, k):
    b = -2*a*h
    c = a*h**2 + k
    return (a, b, c)