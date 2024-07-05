import flet as ft

class player:
    # 正解数、不正解数のテキストオブジェクトを指す変数
    correct = ft.Text()
    miss = ft.Text()
    card = None
    
    def __init__(self, name:str, id, screen) -> None:
        self.name = name
        self.id = id
        self.screen = screen

    # 初回登録
    def register(self):
        pass

    def onpush_o(self, correct_list):
        self.update_list(correct_list)
        self.correct.value += 1
        self.correct.update()

    def onpush_o_other(self):
        pass

    def onpush_x(self, rengotou):
        self.miss.value += 1
        self.miss.update()

    def onpush_x_other(self):
        pass

    def through(self):
        pass

    def undo(self):
        pass


    def update_list(self, list):
        (last, n) = list[-1]
        list.pop(0)
        if last == self.id:
            list.append((self.id, n+1))
        else:
            list.append((self.id, 0))

    def reset(self):
        self.correct.value = 0
        self.correct.update()
        self.miss.value = 0
        self.miss.update()






#Cardの書き方
#Card - (content) - Stack - (controls) - Container - (content) - ////Column - (controls) < LastTile
#                                                                                  ////                           < Row - (controls) < Row - (controls) [correct, wrong]
#                                                                                                                                          < Row - (controls) [○, ×]
#                                                 - Row - (controls) - Text     # レイヤー
#
# ////より左を正しくしていればよい