import tkinter as tk


def main():
    root = tk.Tk()
    root.minsize(width=500, height=400)
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
    ball = canvas.create_oval(0, 100, 40, 140, fill='green')

    def motion():
        canvas.move(ball, 1, 0)
        if canvas.coords(ball)[2] < 500:
            root.after(10, motion)

    motion()


    root.mainloop()


if __name__ == '__main__':
    main()
