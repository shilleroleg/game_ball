import tkinter as tk
from random import randint

WIDTH = 50
HEIGHT = 50


class Ball:
    def __init__(self):
        self.R = 20
        self.x = randint(1.1*self.R, WIDTH-1.1*self.R)
        self.y = self.R
        self.dx, self.dy = (+3, +3)

        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R,
                                          self.x + self.R, self.y + self.R,
                                          fill='green')

    def move(self):
        self.x = self.x
        self.y += self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.y)

    def get_coord(self):
        return self.x, self.y


def tick():
    print(balls.get_coord()[1])
    balls.move()
    balls.show()
    if balls.get_coord()[1] > HEIGHT:
        return

    root.after(100, tick)




def main():
    global root, canvas, balls

    root = tk.Tk()
    root.minsize(width=2*WIDTH, height=2*HEIGHT)
    root.title("Ball")

    tk.Label(root, text="Score:", font="Times 14").grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
    val_score = tk.Label(root, text=" ", font="Times 14").grid(row=0, column=1, sticky=tk.W, pady=10, padx=10)
    tk.Label(root, text="Life:", font="Times 14").grid(row=0, column=2, sticky=tk.W, pady=10, padx=10)
    val_life = tk.Label(root, text=" ", font="Times 14").grid(row=0, column=3, sticky=tk.W, pady=10, padx=10)

    # Создаем холст
    canvas = tk.Canvas(root, width=500, height=350)
    # canvas.bind("<Button-1>", canvas_callback)
    canvas.grid(row=1, column=0, columnspan=4)

    # Мяч
    num_balls = 0
    while num_balls < 2:
        balls = Ball()
        tick()
        num_balls += 1

    root.mainloop()


if __name__ == '__main__':
    main()
