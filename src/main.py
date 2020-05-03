import tkinter as tk
from random import randint

WIDTH = 300
HEIGHT = 300


class Ball:
    def __init__(self):
        self.R = 30
        self.x = randint(1.1*self.R, WIDTH-1.1*self.R)
        self.y = self.R
        self.dx, self.dy = (0, +3)

        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R,
                                          self.x + self.R, self.y + self.R,
                                          fill='green')
        # print("init ", self.ball_id, self.dy)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # print("move ", self.ball_id, self.dy)

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)
        # print("show ", self.ball_id, self.dy)

    def get_coord(self):
        return canvas.coords(self.ball_id)

    def delete_ball(self):
        canvas.delete(self.ball_id)


def tick():
    balls.move()
    balls.show()
    if balls.get_coord()[1] > HEIGHT:
        balls.delete_ball()
        create_ball()

    root.after(100, tick)


def create_ball():
    global balls
    balls = Ball()
    tick()


def main():
    global root, canvas

    root = tk.Tk()
    root.minsize(width=WIDTH, height=HEIGHT)
    root.title("Ball")

    tk.Label(root, text="Score:", font="Times 14").grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
    val_score = tk.Label(root, text=" ", font="Times 14").grid(row=0, column=1, sticky=tk.W, pady=10, padx=10)
    tk.Label(root, text="Life:", font="Times 14").grid(row=0, column=2, sticky=tk.W, pady=10, padx=10)
    val_life = tk.Label(root, text=" ", font="Times 14").grid(row=0, column=3, sticky=tk.W, pady=10, padx=10)

    # Создаем холст
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    # canvas.bind("<Button-1>", canvas_callback)
    canvas.grid(row=1, column=0, columnspan=4)

    # # Мяч
    # num_balls = 0
    # while num_balls < 2:
    #     balls = Ball()
    #     tick()
    #     num_balls += 1
    create_ball()

    root.mainloop()


if __name__ == '__main__':
    main()
