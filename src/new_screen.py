import flet as ft
import data
import rule1_free, rule2_rentou


RULES = ["free", "連答付きn○n×"]


def change_rule(dlg:list, rule:str):
    dlg.clear()
    if rule == RULES[0]:
        pass
    elif rule == RULES[1]:
        cr = ft.Row([ft.Text("目標正解数 : "), ft.TextField(value=5, width=100, input_filter=ft.NumbersOnlyInputFilter(), text_align=ft.TextAlign.RIGHT)])
        wr = ft.Row([ft.Text("失格誤答数 : "), ft.TextField(value=3, width=100, input_filter=ft.NumbersOnlyInputFilter(), text_align=ft.TextAlign.RIGHT)])
        sw1 = ft.Switch(label="加速連答", value=False, label_position=ft.LabelPosition.LEFT)
        sw2 = ft.Switch(label="連誤答", value=False, label_position=ft.LabelPosition.LEFT)
        dlg.append(cr)
        dlg.append(wr)
        dlg.append(sw1)
        dlg.append(sw2)
    else:
        raise TypeError(1)

def parse(s:str):
    def f(s:str):
        s = s.strip()
        try:
            id = int(s)
            return (s, None, None)
        except:
            if ":" in s:
                [id, tail] = s.split(":")
                if "/" in tail:
                    [name, rule] = tail.split("/")
                    [rule_id, para] = rule.split("{")
                    para = para[:-1]
                    paras = para.split(" ")
                    paras = tuple(e == "True" if e == "True" or "False" else int(e) for e in paras)              # boolとintのみ許しているのでかえるならここ
                    return (id, name, (int(rule_id), paras))
                else:
                    return (id, tail, None)
            else:
                [id, rule] = s.split("/")
                [rule_id, para] = rule.split("{")
                para = para[:-1]
                paras = para.split(" ")
                paras = tuple(bool(e) if e == "True" or e == "False" else int(e) for e in paras)              # boolとintのみ許しているのでかえるならここ
                return (id, None, (int(rule_id), paras))
            
    strlist = s.split(",")
    parsedlist = tuple(map(f, strlist))
    return parsedlist

def on_change(e, m):
    try:
        texts = parse(e.data)
        text = ""
        for id, a, _ in texts:
            text += a + "\n" if a else data.MEMB[id] + "\n"
    except:
        return
    m.helper_text=text
    m.update()

def toplayer(name, id, screen, rule, paramlist):
    if rule == RULES[0]:
        return rule1_free.rule1_free(name, id, screen)
    elif rule == RULES[1]:
        if not paramlist[0]:
            paramlist[0] = 5
        if not paramlist[1]:
            paramlist[1] = 3
        return rule2_rentou.rule2_rentou(name, id, screen, paramlist)
    else:
        raise TypeError(1)


def close(s, member_str, rule, column_list, screen):
    memlist = parse(member_str)
    paramlist = tuple(c.value if "value" in dir(c) else c.controls[1].value for c in column_list)
    paramlist = tuple(e if type(e) is bool else int(e) for e in paramlist)
    for id, name, params in memlist:
        name = name or data.MEMB[id]
        if params:
            thisrule = RULES[int(params[0])]
            params = params[1]
        else:
            thisrule = rule
        params = params or paramlist
        player = toplayer(name, id, screen, thisrule, params)
        screen.add_member(player)
    if s:
        return s
    else:
        if rule == RULES[0]:
            return "Free"
        elif rule == RULES[1]:
            n = paramlist[0] or 5
            m = paramlist[1] or 3
            kasoku = "加速連答" if paramlist[2] else "連答"
            rengotou = "連誤答付き" if paramlist[3] else "付き"
            return kasoku + rengotou + str(n) + "○" + str(m) + "×"
        else:
            raise TypeError(1)

        



                    

