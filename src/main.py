import flet as ft


import player
import rule1_free, rule2_rentou
import screen_c
import data, new_screen



# 存在するスクリーン
screens = [screen_c.screen_c(0)]
# 表示するスクリーン
screen = screens[0]



def main(page: ft.Page):
   
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1300
    page.window_height = 800

    # 問題文と得点状況
    box = ft.Column()
    page.add(box)

 # windowを変える、消す
    def change_window(n):
        global screen
        if screen == screens[n]:
            print("same")
            return
        screen.vanish(box)
        screen = screens[n]
        if n == -1:
            screen.register(box)
        else:
            screen.display(box)

    def delete_window(item, n):
        appbar.items.remove(item)
        
        appbar.update()



# windowを追加する
    def open_config(e):
        global screen
        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def close_ok(e, str, member_str, rule, column_list):
            global screen
            dlg_modal.open = False
            page.update()
            newscreen =  screen_c.screen_c(0)
            try:
                str = new_screen.close(str, member_str, rule, column_list, newscreen)
            except:
                return

            x = len(screens)
            item = ft.PopupMenuItem(on_click=lambda _:change_window(x), content=ft.Row([ft.Text(str), ft.IconButton(icon=ft.icons.DELETE)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))
            item.content.controls[1].on_click = lambda _:delete_window(item, x)
            appbar.items.insert(-2, item)

            
            screens.append(newscreen)
            screen.vanish(box)
            newscreen.register(box)
            screen = newscreen

        def change_rule(e:ft.ControlEvent):
            new_screen.change_rule(dlg_modal.content.controls[1].controls, e.data)
            dlg_modal.update()

        name = ft.TextField(label="name")
        member = ft.TextField(label="member", helper_text="id(:\"name\")?(/rule_id{para1 para2 ...})? (, ... )*", on_change=lambda e:new_screen.on_change(e, member))
        rules = ft.Dropdown(options=[ft.dropdown.Option(i) for i in new_screen.RULES], on_change=change_rule, value="free")

        dlg_modal = None
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Column(controls=[ft.Column([name, member, rules]), ft.Column([])]),
            actions=[
                ft.TextButton("Yes", on_click=lambda e: close_ok(e, name.value, member.value, rules.value, dlg_modal.content.controls[1].controls)),
                ft.TextButton("No", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=close_dlg,
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()



    appbar = ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        content=ft.Row([
                            ft.Text("window 1"),
                            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _:print(1)),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        on_click=lambda _:change_window(0)), 
                    ft.PopupMenuItem(),
                ]
            )
    
    appbar.items.append(ft.PopupMenuItem(
                        text="Add window", icon=ft.icons.ADD_SHARP, on_click=open_config
                    ))

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("Quiz"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[appbar
        ],
    )


    for id,m in data.MEMB.items():
        screen.add_member(rule1_free.rule1_free(m, id, screen))
        if int(id) > 20:
            break
    screen.register(box)


    page.add(ft.Row([ft.ElevatedButton("reset", on_click=lambda _:screen.reset()), ft.ElevatedButton("undo", on_click=lambda _:screen.undo())], alignment=ft.alignment.bottom_right))      #, ft.ElevatedButton("Change or add a window", on_click=lambda _: page.show_end_drawer(end_drawer))
    pick_files_dialog = ft.FilePicker(on_result=data.pick_files_result)
    page.overlay.append(pick_files_dialog)
    page.add(ft.ElevatedButton("change questions", icon=ft.icons.UPLOAD_FILE, on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False)))

    
ft.app(target=main)