import tkinter as tk
from random import randint, choice

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self, dx, dy):
        self.R = randint(20, 30)
        self.x = randint(self.R, WIDTH-self.R)
        self.y = self.R
        self.dx = 0 if dx is None else dx
        self.dy = 2 if dy is None else dy
        # self.dy = dy

        self.color = choice(['blue', 'green', 'red', 'brown'])

        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=self.color)
        # canvas.tag_bind(self.ball_id, '<ButtonPress-1>', func=canvas.delete(self.ball_id))

    def move(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def get_coord(self):
        return canvas.coords(self.ball_id)
    #
    # def delete_ball(self, *args):
    #     canvas.delete(self.ball_id)


class Menu:
    def __init__(self):
        self.val_score_num = 10
        self.val_life_num = 3

        self.frame_top = tk.Frame(root)

        self.label_1 = tk.Label(self.frame_top, text="Score:", font="Times 14")
        self.val_score_label = tk.Label(self.frame_top, text=str(self.val_score_num), font="Times 14")

        self.label_2 = tk.Label(self.frame_top, text="Life:", font="Times 14")
        self.val_life_label = tk.Label(self.frame_top, text=str(self.val_life_num), font="Times 14")

        self.frame_top.pack(side='top')
        self.label_1.pack(side='left', padx=10, pady=10)
        self.val_score_label.pack(side='left', padx=10, pady=10)
        self.label_2.pack(side='left', padx=10, pady=10)
        self.val_life_label.pack(side='left', padx=10, pady=10)

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


def create_ball():
    global ball_id
    ball_id = Ball(0, 2)


def motion():
    # canvas.move(ball_id, 0, 1)
    ball_id.move()
    # print(canvas.coords(ball_id))
    if int(ball_id.get_coord()[1]) < HEIGHT + ball_id.R:
        root.after(15, motion)
    else:
        # print("Else")
        canvas.delete(ball_id)
        create_ball()
        motion()


def main():
    global root, canvas, menu, ball_id

    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(side='bottom')

    menu = Menu()

    create_ball()
    motion()

    root.mainloop()


if __name__ == '__main__':
    main()
