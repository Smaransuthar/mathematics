import math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import wave

Res = math.floor(float(input("Resolution = ")))
yn = input("\nScaling option:\n(i) Custom\n(ii) Preset\n\n")

if (yn == '(i)') or (yn == '1'):
    PZ = float(input("Vertical Zoom = "))
    
else:
    print("\n(i) mm\n(ii) cm\n(iii) m\n(iv) Inch\n")
    preset = input()
    if preset == 'mm':
4        PZ = 3.78
    elif preset == 'cm':
        PZ = 37.8
    elif preset == 'm':
        PZ = 378
    elif preset == 'Inch':
        PZ = 96

graph = Image.new("RGB", (Res, Res), (0, 0, 0))

graph.save("graph.png", "PNG")

draw = ImageDraw.Draw(graph)

width, height = graph.size

def originiser(coordinates):
    return((math.floor(coordinates[0] + (Res/2)), math.floor(coordinates[1] + (Res/2))))

def drawer(coordinates):
        graph.putpixel(originiser(((PZ * coordinates[0]), (PZ * coordinates[1]))), (255, 0, 0))
        graph.putpixel(originiser(((PZ * coordinates[0]), (PZ * coordinates[1]) + 1)), (255, 0, 0))
        graph.putpixel(originiser(((PZ * coordinates[0]), (PZ * coordinates[1]) - 1)), (255, 0, 0))
        graph.putpixel(originiser(((PZ * coordinates[0]) - 1, (PZ * coordinates[1]))), (255, 0, 0))
        graph.putpixel(originiser(((PZ * coordinates[0]) + 1, (PZ * coordinates[1]))), (255, 0, 0))
        
for i in range(height):
    graph.putpixel(((math.floor(Res/2)), i), (0, 255, 0))
    graph.putpixel((i, math.floor((Res/2))), (0, 255, 0))

def quadraticiser(A, B, C, D, E, Offset):
    c = (-Res) * PZ
    while c <= (Res/2):
        x = c
        y = (((A * ((c) ** 4)) + (B * (c ** 3)) + (C * (c ** 2)) + (D * (c)) + E))
        c += 0.01
        if (((PZ * y) < (Res/2)) and ((PZ * y) > -(Res/2))) and (((PZ * x) < (Res/2)) and ((PZ * x) > -(Res/2))):
            if ((((PZ * y) + 1) < (Res/2)) and (((PZ * y) - 1) > -(Res/2))) and ((((PZ * x) + 1) < (Res/2)) and (((PZ * x) - 1) > -(Res/2))):
                drawer((x, y))
        else:
            continue
        
def exponential(n, a, b, C):
    c = (-Res) * PZ

    while c <= (Res/2):
        x = c
        y = ((a * (n)) ** ((b) * c)) + C
        c += 0.01
        if (((PZ * y) < (Res / 2)) and ((PZ * y) > -(Res / 2))) and (((PZ * x) < (Res/2)) and ((PZ * x) > -(Res/2))):
                drawer((x, y))    

        else:
            continue

def trigonometric(Zoom, a, b, C, p, q, r, m, n, o):
    c = (-Res) * PZ

    while c <= (Res/2):
        x = c
        y = math.floor(Zoom * ((a * math.sin(b * (c ** C)) + (p * math.cos(q * (c ** r)) + (m * math.tan(n * (c ** o)))))))
        c += 0.01
        if (((PZ * y) < (Res/2)) and ((PZ * y) > -(Res/2))) and (((PZ * x) < (Res/2)) and ((PZ * x) > -(Res/2))):
            if ((((PZ * y) + 1) < (Res/2)) and (((PZ * y) - 1) > -(Res/2))) and ((((PZ * x) + 1) < (Res/2)) and (((PZ * x) - 1) > -(Res/2))):
                drawer((x, y))
        else:
            continue

def logarithmic(base, a, b):
    c = 0.01

    while c <= (Res/2):
        x = c
        y = (a * (math.log(c, base))) + b
        c += 0.01
        
        if (((PZ * y) < (Res/2)) and ((PZ * y) > -(Res/2))) and (((PZ * x) < (Res/2)) and ((PZ * x) > -(Res/2))):
            if ((((PZ * y) + 1) < (Res/2)) and (((PZ * y) - 1) > -(Res/2))) and ((((PZ * x) + 1) < (Res/2)) and (((PZ * x) - 1) > -(Res/2))):
                drawer((x, y))
        else:
            continue
        
def inverse(A, B, C, D, E, Offset):
    c = (-Res) * PZ
    
    while c <= (Res/2):
        x = c
        y = 1 / (((A * ((c) ** 4)) + (B * (c ** 3)) + (C * (c ** 2)) + (D * (c)) + E))
        c += 0.01
        if (((PZ * y) < (Res/2)) and ((PZ * y) > -(Res/2))) and (((PZ * x) < (Res/2)) and ((PZ * x) > -(Res/2))):
            if ((((PZ * y) + 1) < (Res/2)) and (((PZ * y) - 1) > -(Res/2))) and ((((PZ * x) + 1) < (Res/2)) and (((PZ * x) - 1) > -(Res/2))):
                drawer((x, y))
        else:
            continue

form = input("\nSelect Graph form:\n(i) Polynomial\n(ii) Trigonometric\n(iii) Exponential\n(iv) Logarithmic\n(v) Inverse Polynomial\n\n")

if (form == '1') or (form == '(i)'):
    A = float(input("\nAx^4 + Bx^3 + Cx^2 + Dx + E\n\nA = "))
    B = float(input("B = "))
    C = float(input("C = "))
    D = float(input("D = "))
    E = float(input("E = "))
    Offset = float(input("Offset = "))
    quadraticiser(A, B, C, D, E, Offset)

elif (form == '3') or (form == '(iii)'):
    print("a(n^bx) + c\n")
    n = float(input("n = "))
    a = float(input("a = "))    
    b = float(input("b = "))
    C = float(input("c = "))
    exponential(n, a, b, C)

elif ((form == '2') or (form == '(ii)')):
    print("\nasinbx^c + pcosqx^r + mtannx^o\n")
    Zoom = float(input("Zoom = "))
    a = float(input("a = "))
    b = float(input("b = "))
    C = float(input("c = "))
    p = float(input("p = "))
    q = float(input("q = "))
    r = float(input("r = "))
    m = float(input("m = "))
    n = float(input("n = "))
    o = float(input("o = "))
    trigonometric(Zoom, a, b, C, p, q, r, m, n, o)

elif ((form == '4') or (form == '(iv)')):
    base = float(input("\nalog.base(x) + b\n\nBase = "))
    a = float(input("A = "))
    b = float(input("B = "))
    logarithmic(base, a, b)

elif ((form == '5') or (form == '(v)')):
    A = float(input("\nAx^4 + Bx^3 + Cx^2 + Dx + E\n\nA = "))
    B = float(input("B = "))
    C = float(input("C = "))
    D = float(input("D = "))
    E = float(input("E = "))
    Offset = float(input("Offset = "))
    inverse(A, B, C, D, E, Offset)

m = Res/2
txt = 0

while m <= height:
    if PZ < 15:
        break
    else:
        draw.text(((Res/2) + 2, m), str(txt), fill = (0, 0, 255))
        draw.text((m, (Res/2) + 2), str(txt), fill = (0, 0, 255))
        m += PZ
        txt += 1

m = Res/2 - PZ
txt = -1

while m >= -height:
    if PZ < 15:
        break
    else:
        draw.text(((Res/2) + 2, m), str(txt), fill = (0, 0, 255))
        draw.text((m, (Res/2) + 2), str(txt), fill = (0, 0, 255))
        m -= PZ
        txt -= 1

graph = graph.rotate(180, expand = 1)
graph = graph.transpose(Image.FLIP_LEFT_RIGHT)
graph.show()
