import turtle

# Setup
turtle.speed(0)
turtle.bgcolor("orange")
turtle.pensize(20)  # Increase the pen width for the border effect

# RGB colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet","white","pink","lime","olive"]
num_colors = len(colors)

# Draw the RGB color ring with a border
for _ in range(360):
    turtle.pencolor(colors[_ % num_colors])
    turtle.forward(100)  # Move forward to draw the ring
    turtle.backward(100)  # Move backward to create the ring effect
    turtle.right(7)  # Rotate slightly to create the revolving effect

    # Change color every 1 millisecond
    if _ % 38 == 0:
        colors.append(colors.pop(0))

# Draw the loading text below the ring
turtle.penup()
turtle.goto(0, -120)  # Position below the ring
turtle.pendown()
turtle.color("black")  # Set text color
loading_text = "Loading"
dots = ""  # Initial dots
for i in range(20):  # Increase the range for more dots
    dots += "."
    turtle.clear()  # Clear previous text
    turtle.write(f"{loading_text}{dots}", align="center", font=("Arial", 16, "normal"))
    turtle.delay(100)  # Delay between adding dots

# Hide turtle and display
turtle.hideturtle()
turtle.done()
this code is by techno solutions code developer
