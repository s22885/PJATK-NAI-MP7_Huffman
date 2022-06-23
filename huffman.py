class Huffman:
    data: list
    res:str

    def __init__(self, data):
        self.data = data

    def get_res(self):
        if len(self.data) != 1:
            return
        if type(self.data[0]) != Strg:
            return
        self.res = ""
        self.get_res_recur(self.data[0], "")

    def get_res_recur(self, data, code):
        if type(data.left) != Strg:
            self.res += f"{data.left} {code}0\n"
        else:
            self.get_res_recur(data.left, code + "0")
        if type(data.right) != Strg:
            self.res += f"{data.right} {code}1\n"
        else:
            self.get_res_recur(data.right, code + "1")

    def calc(self):
        if len(self.data) > 1:
            tmpl = self.data.pop(0)
            tmpr = self.data.pop(0)
            tmps = (tmpl[1] if type(tmpl) == list else tmpl.size) + (tmpr[1] if type(tmpr) == list else tmpr.size)
            stor = Strg(tmpl[0] if type(tmpl) == list else tmpl, tmpr[0] if type(tmpr) == list else tmpr, tmps)
            for i in range(len(self.data)):
                tmp = self.data[i][1] if type(self.data[i]) == list else self.data[i].size
                if stor.size < tmp:
                    self.data.insert(i, stor)
                    break
                elif stor == tmp:
                    comp_val = self.data[i][0] if type(self.data[i]) == list else self.data.__str__() > stor.__str__()
                    if comp_val:
                        self.data.insert(i, stor)
                        break
                elif len(self.data) - 1 == i:
                    self.data.append(stor)
                    break
            if len(self.data) == 0:
                self.data.append(stor)
            self.calc()


class Strg:
    comb: str
    size: float

    def __init__(self, left, right, size):
        self.left = left
        self.right = right
        self.size = size
        self.comb = f"{self.left}{self.right}"

    def __str__(self):
        return f"{self.left}{self.right}"
