import random
import turtle as turtle_module
import colorgram


# def get_rgb_color():
#     colors = colorgram.extract('image.jpg', 30)
#     for color in colors:
#         color_rgb = color.rgb.r, color.rgb.g, color.rgb.b
#         color_list.append(color_rgb)
#
#
# get_rgb_color()

color_list = [(201, 164, 112), (238, 246, 241), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126),
              (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33),
              (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89),
              (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51),
              (108, 127, 151), (177, 192, 209), (88, 85, 28), (109, 136, 140), (251, 196, 3), (174, 198, 202)]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")


def hirst_painting(width, height, step, x, y):
    timmy.hideturtle()
    timmy.up()
    while height > 0:
        timmy.goto(x, y)
        for _ in range(width):
            timmy.dot(20, random.choice(color_list))
            timmy.forward(step)
        y += step
        height -= 1


hirst_painting(10, 10, 50, -230, -230)

screen = turtle_module.Screen()
screen.exitonclick()
