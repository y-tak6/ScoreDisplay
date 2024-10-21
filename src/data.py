import csv, time
import flet as ft
import math

q_url = "./data/questions.csv"
m_url = "./data/members.csv"

def file_change(url, q_or_m):
    global QUES, MEMB
    try:
        with open(url, encoding="utf-8") as f:
            reader = csv.reader(f)
            if q_or_m == "q":
                QUES = [row for row in reader] 
            elif q_or_m == "m":
                MEMB = {row[0]:row[1].replace('\\n', '\n') for row in reader}
    except:
        return

file_change(q_url, "q")
file_change(m_url, "m")

# 問題ファイルの変更
def pick_files_result(e: ft.FilePickerResultEvent):
    if e.files:
        url = e.files[0].path
        file_change(url, "q")


def win(card: ft.Card):
    card.content.controls[1] = ft.Row([ft.Text("Win", color=ft.colors.RED_300, size=40, rotate=math.pi / 4)])
    card.color=ft.colors.RED_900
    card.update()

def lose(card:ft.Card):
    card.content.controls[1] = ft.Row([ft.Text("Lose", color=ft.colors.BLUE_300, size=40, rotate=math.pi / 4)])
    card.color=ft.colors.BLUE_900
    card.update()

def freeze(card:ft.Card):
    card.content.controls[1] = ft.Row([ft.Text("Freeze", color=ft.colors.BLUE_300, size=40, rotate=math.pi / 4)])
    card.color=ft.colors.DEEP_PURPLE_200
    card.update()

def reset_win_lose(card:ft.Card):
    card.content.controls[1] = ft.Row()
    card.color = None
    card.update()