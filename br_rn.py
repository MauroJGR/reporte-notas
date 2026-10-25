"""Harmless animated prank window; no file or network access."""
import sys


def main() -> int:
    """Show a dismissible fictional alert and reveal the joke."""
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError:
        print('This Python installation does not include tkinter.')
        return 1
    try:
        window = tk.Tk()
    except tk.TclError as error:
        print(f'Cannot open the window: {error}')
        return 1
    window.title('Grade Virus - Simulation')
    window.geometry('620x360')
    window.resizable(False, False)
    window.configure(bg='#101218')
    window.bind('<Escape>', lambda event: window.destroy())
    style = ttk.Style(window)
    style.theme_use('clam')
    style.configure(
        'Alert.Horizontal.TProgressbar', background='#ff4058',
        troughcolor='#252936', thickness=24,
    )
    title = tk.Label(
        window, text='THREAT DETECTED', bg='#101218', fg='#ff4058',
        font=('Segoe UI', 26, 'bold'),
    )
    title.pack(pady=(28, 12))
    status = tk.Label(
        window, text='GRADE_VIRUS.exe is taking control...',
        bg='#101218', fg='white', font=('Segoe UI', 12),
    )
    status.pack(pady=8)
    bar = ttk.Progressbar(
        window, style='Alert.Horizontal.TProgressbar',
        maximum=100, length=520, mode='determinate',
    )
    bar.pack(pady=(18, 10))
    percent = tk.Label(
        window, text='0%', bg='#101218', fg='#ff697c',
        font=('Consolas', 15, 'bold'),
    )
    percent.pack()
    tk.Label(
        window, text='SIMULATION - Press Esc or Close to exit',
        bg='#101218', fg='#aeb6c8', font=('Segoe UI', 10),
    ).pack(pady=(16, 8))
    tk.Button(
        window, text='Close', command=window.destroy,
        bg='#2b3040', fg='white', relief='flat', padx=26, pady=7,
    ).pack()

    def advance(value: int = 0) -> None:
        """Animate the interface only, then reveal the prank."""
        bar['value'] = value
        percent.config(text=f'{value}%')
        if value >= 70:
            status.config(text='Preparing academic world domination...')
        elif value >= 35:
            status.config(text='Injecting perfect scores into the system...')
        if value < 100:
            window.after(65, advance, value + 1)
        else:
            title.config(text='JUST KIDDING!', fg='#65e6b4')
            status.config(text='Your files and grades are untouched.')
            percent.config(text='100% theater - 0% virus', fg='#65e6b4')

    window.after(500, advance)
    window.mainloop()
    return 0


if __name__ == '__main__':
    sys.exit(main())
