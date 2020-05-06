import tkinter as tk
from random import randint, choice

WIDTH = 300
HEIGHT = 400


class Ball:
    def __init__(self, dx, dy):
        self.R = randint(20, 30)
        self.x = randint(self.R, WIDTH-self.R)
        self.y = self.R
        self.dx = 0 if dx is None else dx
        # self.dy = 5 if dy is None else dy
        self.dy = dy

        self.color = choice(['blue', 'green', 'red', 'brown'])

        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=self.color)
        canvas.tag_bind(self.ball_id, '<ButtonPress-1>', func=self.delete_ball)

    def move(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def get_coord(self):
        return canvas.coords(self.ball_id)

    def delete_ball(self, *args):
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

    def score_increase(self, count):
        # Увеличивае кол-во очков на величину count
        self.val_score_num += count
        self.val_score_label['text'] = str(self.val_score_num)

    def score_decrease(self, count):
        # Уменьшаем кол-во очков на величину count
        self.val_score_num -= count
        self.val_score_label['text'] = str(self.val_score_num)

    def life_increase(self):
        pass

    def life_decrease(self):
        pass


def tick():
    ball.move()
    # Если шарик лопнул, увеличиваем очки на 3 и перезапускаем
    if len(ball.get_coord()) == 0:
        menu.score_increase(3)
        run_game()
    # Если шарик вышел за границы экрана, уменьшаем очки на 1 и перезапускаем
    if len(ball.get_coord()) > 0 and int(ball.get_coord()[1]) > HEIGHT:
        ball.delete_ball()
        menu.score_decrease(1)
        run_game()

    root.after(100, tick)


def run_game():
    global ball
    # Мяч
    ball = Ball(0, 5)
    tick()
    # print("Exit run_game")


def main():
    global root, canvas, menu

    root = tk.Tk()
    root.minsize(width=WIDTH, height=HEIGHT)
    root.title("Ball")

    # Создаем холст
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.grid(row=1, column=0, columnspan=4)

    menu = Menu()

    run_game()

    root.mainloop()


if __name__ == '__main__':
    main()
