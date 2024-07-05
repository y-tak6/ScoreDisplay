import csv, time
import flet as ft
import math

q_url = "./data/questions.csv"
m_url = "./data/members.csv"

with open(q_url) as f:
    reader = csv.reader(f)
    QUES = [row for row in reader]

with open(m_url) as f:
    reader = csv.reader(f)
    MEMB = {row[0]:row[1].replace('\\n', '\n') for row in reader}


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