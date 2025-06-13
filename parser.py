class Parser:
    def __init__(self):
        pass

    def parse(self, line):
        tokens = line.split()

        if len(tokens) == 0:
            return None, tuple()

        cmd_name = tokens[0]

        if len(tokens) == 1:
            return cmd_name, tuple()

        args = tokens[1:]

        return cmd_name, args


a = '   salut    " les    amis"  '
p = Parser()
print(p.parse(a))
