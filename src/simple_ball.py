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
        self.dy = 2 if dy is None else dy

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

        # Если очков меньше нуля, уменьшает жизнь на 1,
        # и восстанавливаем начальное кол-во очков
        if self.val_score_num < 1:
            self.life_decrease()
            self. score_increase(10)

    def life_increase(self):
        # Увеличивает кол-во жизней
        self.val_life_num += 1
        self.val_life_label['text'] = str(self.val_life_num)

    def life_decrease(self):    # TODO: Закончить игру при 0 жизней
        # Уменьшает кол-во жизней
        self.val_life_num -= 1
        self.val_life_label['text'] = str(self.val_life_num)


def create_ball(dx, dy):
    """
    Создаем новый объект шарик

    :param dx: Шаг смещения по оси х
    :param dy: Шаг смещения по оси у
    :return: Объект шар
    """
    global ball_id
    ball_id = Ball(dx, dy)


def motion():
    # TODO: Сначала добавляем несколько шариков одновременно на экране
    # TODO: Затем ускоряем падение шариков
    ball_id.move()

    # Если шарик лопнул, увеличиваем очки на 3 и перезапускаем
    if len(ball_id.get_coord()) == 0:
        menu.score_increase(3)
        create_ball(0, 2)

    # Если шарик НЕ вышел за границы экрана - продолжаем
    if len(ball_id.get_coord()) > 0 \
            and int(ball_id.get_coord()[1]) < HEIGHT + ball_id.R:
        root.after(25, motion)
    else:   # Иначе, уменьшаем очки на 1 и перезапускаем
        canvas.delete(ball_id)
        menu.score_decrease(1)
        create_ball(0, 2)
        motion()


def main():
    global root, canvas, menu, ball_id

    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(side='bottom')

    menu = Menu()

    create_ball(0, 2)
    motion()

    root.mainloop()


if __name__ == '__main__':
    main()
