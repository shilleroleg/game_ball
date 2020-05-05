import tkinter as tk
from random import randint, choice

WIDTH = 300
HEIGHT = 400


class Ball:
    def __init__(self):
        self.R = randint(20, 30)
        self.x = randint(self.R, WIDTH-self.R)
        self.y = self.R
        self.dx, self.dy = (0, 5)

        self.color = choice(['blue', 'green', 'red', 'brown'])

        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R,
                                          self.x + self.R, self.y + self.R,
                                          fill=self.color)

    def move(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def get_coord(self):
        return canvas.coords(self.ball_id)

    def delete_ball(self):
        canvas.delete(self.ball_id)


class Menu:
    def __init__(self):
        self.val_score_num = 10
        tk.Label(root, text="Score:", font="Times 14").grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
        self.val_score_label = tk.Label(root, text=str(self.val_score_num), font="Times 14")
        self.val_score_label.grid(row=0, column=1, sticky=tk.W, pady=10, padx=10)

        self.val_life_num = 3
        tk.Label(root, text="Life:", font="Times 14").grid(row=0, column=2, sticky=tk.W, pady=10, padx=10)
        self.val_life_label = tk.Label(root, text=str(self.val_life_num), font="Times 14")
        self.val_life_label.grid(row=0, column=3, sticky=tk.W, pady=10, padx=10)

    def score_increase(self):
        self.val_score_num += 1
        self.val_score_label['text'] = str(self.val_score_num)

    def score_decrease(self):
        self.val_score_num -= 1
        self.val_score_label['text'] = str(self.val_score_num)

    def life_increase(self):
        pass

    def life_decrease(self):
        pass


def tick():
    ball.move()
    # print(int(ball.get_coord()[1]))
    if int(ball.get_coord()[1]) > HEIGHT:
        ball.delete_ball()
        menu.score_decrease()
        run_game()

    root.after(100, tick)
    # print("Exit tick")


def run_game():
    global ball
    # Мяч
    ball = Ball()
    tick()
    # print("Exit run_game")


def main():
    global root, canvas, menu

    root = tk.Tk()
    root.minsize(width=WIDTH, height=HEIGHT)
    root.title("Ball")

    # Создаем холст
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    # canvas.bind("<Button-1>", canvas_callback)
    canvas.grid(row=1, column=0, columnspan=4)

    menu = Menu()

    run_game()

    # print("Exit main")

    root.mainloop()


if __name__ == '__main__':
    main()
