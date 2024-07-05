import flet as ft

import player, screen_c



class rule1_free(player.player):

    def register(self):
        num_correct = ft.Container(
            content=ft.Text(
                value=0,
                text_align=ft.TextAlign.CENTER,
                size=15
            ),
            width=40,
            height=40,
            bgcolor=ft.colors.BLACK38,
            alignment=ft.alignment.center,
            border_radius=10
        )
    
        num_miss = ft.Container(
            content=ft.Text(
                value=0,
                text_align=ft.TextAlign.CENTER,
                size=15
            ),
            width=40,
            height=40,
            bgcolor=ft.colors.RED_200,
            alignment=ft.alignment.center,
            border_radius=10
        )
    
        self.card=ft.Card(
            content=ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),
                                    title=ft.Text(self.name),
                                ),
                                ft.Row(
                                    [ft.Row([num_correct, num_miss], alignment=ft.MainAxisAlignment.CENTER), ft.Row([ft.TextButton("○", on_click=lambda e: self.screen.onpush_o(e, self.id)), ft.TextButton("×", on_click=lambda e: self.screen.onpush_x(e, self.id))], alignment=ft.MainAxisAlignment.END)],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ]
                        ),
                        width=400,
                        padding=10,
                    ),
                    ft.Row()
                ]
            )
        )
        self.correct = num_correct.content
        self.miss = num_miss.content

    def onpush_o_other(self):
        pass

    def onpush_x_other(self):
        pass

    def through(self):
        pass

    def undo(self, streak):
        if streak == -1:
            self.miss.value -= 1
        else:
            self.correct.value -= 1
        self.card.update()

