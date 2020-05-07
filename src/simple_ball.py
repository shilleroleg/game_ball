import tkinter as tk
from random import randint, choice

WIDTH = 300
HEIGHT = 400


class Ball:
    def __init__(self, dx, dy):
        self.ball_exist = True
        self.R = randint(20, 30)
        self.x = randint(self.R, WIDTH-self.R)
        self.y = self.R
        self.dx = 0 if dx is None else dx
        self.dy = 2 if dy is None else dy

        self.color = choice(['blue2', 'dodger blue', 'green2', 'red', 'yellow3', 'oliveDrab1', 'orange', 'coral'])

        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=self.color)
        canvas.tag_bind(self.ball_id, '<ButtonPress-1>', func=self.delete_ball)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        canvas.move(self.ball_id, self.dx, self.dy)

    def delete_ball(self, *args):
        self.ball_exist = False
        # canvas.delete(self.ball_id)


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

    def score_change(self, count):
        # Увеличивае кол-во очков на величину count
        self.val_score_num += count
        self.val_score_label['text'] = str(self.val_score_num)

        # Если очков меньше нуля, уменьшает жизнь на 1,
        # и восстанавливаем начальное кол-во очков
        if self.val_score_num < 1:
            self.life_change(-1)
            self.val_score_num = 10
            self. score_change(0)

    def life_change(self, count):    # TODO: Закончить игру при 0 жизней
        # Увеличивает кол-во жизней
        self.val_life_num += count
        self.val_life_label['text'] = str(self.val_life_num)


def create_ball(dx=0, dy=2):
    """
    Создаем новый объект шарик

    :param dx: Шаг смещения по оси х
    :param dy: Шаг смещения по оси у
    :return: Объект шар
    """
    balls.append(Ball(dx, dy))


def motion():
    # TODO: Сначала добавляем несколько шариков одновременно на экране
    # TODO: Затем ускоряем падение шариков

    is_need_ball = False    # Флаг определяющий нужно ли создавать еще шар
    for ball in balls:
        if ball.ball_exist:
            ball.move()
        else:               # Если шарик лопнул, увеличиваем очки на 1 и поднимаем флаг на создание нового шарика
            balls.remove(ball)
            canvas.delete(ball.ball_id)
            menu.score_change(+1)
            is_need_ball = True

        if ball.y > HEIGHT + ball.R:    # Если шарик вышел за границы экрана - уменьшаем очки на 2
            balls.remove(ball)          # и поднимаем флаг на создание нового шарика
            canvas.delete(ball)
            menu.score_change(-2)
            is_need_ball = True
    else:                           # Продолжаем если не было событий
        if is_need_ball:
            create_ball()
        root.after(25, motion)


def main():
    global root, canvas
    global menu, balls

    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(side='bottom')

    menu = Menu()

    balls = []
    create_ball()
    motion()

    root.mainloop()


if __name__ == '__main__':
    main()
