import flet as ft
import data

ROLLBACK = 10

class screen_c:
    members = {}


    def __view(self):
        try:
            QA = data.QUES[self.q_n]
        except:
            QA = ["", "", ""]
        self.tb1.value = QA[1]
        self.tb2.value = QA[2]
        self.q_n += 1
        self.tb1.update()
        self.tb2.update()

    def __init__(self, inital) -> None:
        self.members = {}
        self.streak = [(-1,0) for _ in range(ROLLBACK)]
        self.q_n = inital


    def add_member(self, member):
        self.members[member.id] = member
        member.register()

    def register(self, box):
        # 問題表示
        self.tb1 = ft.TextField(label="ここに問題文が表示されます",read_only=True, max_lines=4, min_lines=4)
        self.tb2 = ft.TextField(label="ここに答えが表示されます",read_only=True, max_lines=1, min_lines=1)
        box.controls.append(self.tb1)
        box.controls.append(self.tb2)
        member_grid = ft.Row(controls=[], scroll=ft.ScrollMode.ALWAYS, vertical_alignment=ft.CrossAxisAlignment.START)
        for i, m in enumerate(self.members.values()):
            if i % 3 == 0:
                column = ft.Column(alignment=ft.MainAxisAlignment.START)
                member_grid.controls.append(column)
            m.register()
            column.controls.append(m.card)
        box.controls.append(member_grid)
        box.update()
        

    def vanish(self, box):
        box.controls = []
        box.update()

    def display(self, box):
        box.controls.append(self.tb1)
        box.controls.append(self.tb2)
        member_grid = ft.Row(controls=[], scroll=ft.ScrollMode.ALWAYS, vertical_alignment=ft.CrossAxisAlignment.START)
        for i, m in enumerate(self.members.values()):
            if i % 3 == 0:
                column = ft.Column(alignment=ft.MainAxisAlignment.START)
                member_grid.controls.append(column)
            column.controls.append(m.card)
        box.controls.append(member_grid)
        box.update()



    def onpush_o(self, e,  pusher_id):
        self.__view()
        for m in self.members.values():
            if m.id == pusher_id:
                m.onpush_o(self.streak)
            else:
                m.onpush_o_other()

    def onpush_x(self, e, pusher_id):
        self.__view()
        for m in self.members.values():
            if m.id == pusher_id:
                m.onpush_x(1)
                (n, _) = self.streak[-1]
                if n == m.id:
                    self.streak.pop(0)
                    self.streak.append((n, -1))
            else:
                m.onpush_x_other()

    def through(self):
        self.__view()
        for m in self.members.values():
            m.through()

    def undo(self):
        (id, streak) = self.streak.pop(-1)
        self.streak.insert(0, (-1,0))
        if id == -1:
            return
        self.members[id].undo(streak)


    def reset(self):
        self.streak = [(-1,0) for _ in range(ROLLBACK)]
        for m in self.members.values():
            m.reset()