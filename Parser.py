class Node:
    def __init__(self, t, c, s):
        self.token_value = t
        self.code_value = c
        self.shape = s
        self.children = []
        self.sibling = None
        self.index = None

    def set_children(self, y):
        try:
            assert isinstance(y, list)
            for i in y:
                self.children.append(i)
        except:
            self.children.append(y)

    def set_sibling(self, y):
        self.sibling = y


class Parser:
    nodes_table = {}
    tmp_index = 0
    edges_table = []

    def __init__(self):
        self.token = str
        self.tokens_list = []
        self.code_list = []
        self.Line_list = []
        self.tmp_index = 0
        self.token = None
        self.parse_tree = None
        self.nodes_table = None
        self.edges_table = None
        self.same_rank_nodes = []
        self.error = False
        self.errorToken = []

    def set_tokens_list_and_code_list(self, Complete_Token_List):
        self.tokens_list = []
        self.code_list = []
        self.Line_list = []
        for Token in Complete_Token_List:
            self.tokens_list.append(Token[2])
            self.code_list.append(Token[0])
            self.Line_list.append(Token[3])
        self.tmp_index = 0
        self.token = self.tokens_list[self.tmp_index]

    def next_token(self):
        if self.tmp_index == len(self.tokens_list)-1:
            return False  # we have reached the end of the list
        self.tmp_index = self.tmp_index + 1
        self.token = self.tokens_list[self.tmp_index]
        return True

    def match(self, x):
        if self.token == x:
            self.next_token()
            return True
        else:
            self.error = True
            temperrortoken = []
            temperrortoken.append(self.token)
            temperrortoken.append(self.code_list[self.tmp_index])
            temperrortoken.append(self.Line_list[self.tmp_index])
            self.errorToken.append(temperrortoken)

    def statement(self):
        if self.token == 'IF':
            t = self.if_stmt()
            return t
        elif self.token == 'REPEAT':
            t = self.repeat_stmt()
            return t
        elif self.token == 'ID':
            t = self.assign_stmt()
            return t
        elif self.token == 'READ':
            t = self.read_stmt()
            return t
        elif self.token == 'WRITE':
            t = self.write_stmt()
            return t
        else:
            self.error = True
            temperrortoken = []
            temperrortoken.append(self.token)
            temperrortoken.append(self.code_list[self.tmp_index])
            temperrortoken.append(self.Line_list[self.tmp_index])
            self.errorToken.append(temperrortoken)

    def stmt_sequence(self):
        t = self.statement()
        p = t
        while self.token == 'SEMI_COLON':
            q = Node(None, None, None)
            self.match('SEMI_COLON')
            q = self.statement()
            if q == None:
                break
            else:
                if t == None:
                    t = p = q
                else:
                    p.set_sibling(q)
                    p = q
        return t

    def factor(self):
        if self.token == "LEFT_BRACKET":
            self.match("LEFT_BRACKET")
            t = self.exp()
            self.match("RIGHT_BRACKET")
        elif self.token == "NUM":
            t = Node(
                'CONSTANT', '(' + self.code_list[self.tmp_index] + ')', 'o')
            self.match("NUM")
        elif self.token == "ID":
            t = Node('IDENTIFIER',
                     '(' + self.code_list[self.tmp_index] + ')', 'o')
            self.match("ID")
        else:
            self.error = True
            temperrortoken = []
            temperrortoken.append(self.token)
            temperrortoken.append(self.code_list[self.tmp_index])
            self.errorToken.append(temperrortoken)
        return t

    def term(self):
        t = self.factor()
        while self.token == "TIMES" or self.token == "DIVIDE":
            p = Node(
                'OPERATOR', '(' + self.code_list[self.tmp_index] + ')', 'o')
            p.set_children(t)
            t = p
            self.mulop()
            p.set_children(self.factor())
        return t

    def simple_exp(self):
        t = self.term()
        while self.token == "PLUS" or self.token == "MINUS":
            p = Node(
                'OPERATOR', '(' + self.code_list[self.tmp_index] + ')', 'o')
            p.set_children(t)
            t = p
            self.addop()
            t.set_children(self.term())
        return t

    def exp(self):
        t = self.simple_exp()
        if self.token == "LESS_THAN" or self.token == "EQUAL" or self.token == "GREATER_THAN":
            p = Node(
                'OPERATOR', '(' + self.code_list[self.tmp_index] + ')', 'o')
            p.set_children(t)
            t = p
            self.comparison_op()
            t.set_children(self.simple_exp())
        return t

    def if_stmt(self):
        t = Node("IF", '', 's')
        if self.token == "IF":
            self.match("IF")
            t.set_children(self.exp())
            self.match("THEN")
            t.set_children(self.stmt_sequence())
            if self.token == "ELSE":
                self.match("ELSE")
                t.set_children(self.stmt_sequence())
            self.match("END")
        return t

    def comparison_op(self):
        if self.token == "LESS_THAN":
            self.match("LESS_THAN")
        elif self.token == "EQUAL":
            self.match("EQUAL")
        elif self.token == "GREATER_THAN":
            self.match("GREATER_THAN")

    def addop(self):
        if self.token == "PLUS":
            self.match("PLUS")
        elif self.token == "MINUS":
            self.match("MINUS")

    def mulop(self):
        if self.token == "TIMES":
            self.match("TIMES")
        elif self.token == "DIVIDE":
            self.match("DIVIDE")

    def repeat_stmt(self):
        t = Node('REPEAT', '', 's')
        if self.token == "REPEAT":
            self.match("REPEAT")
            t.set_children(self.stmt_sequence())
            self.match('UNTIL')
            t.set_children(self.exp())
        return t

    def assign_stmt(self):
        t = Node('ASSIGN', '(' + self.code_list[self.tmp_index] + ')', 's')
        self.match("ID")
        self.match("ASSIGN")
        t.set_children(self.exp())
        return t

    def read_stmt(self):
        t = Node('READ', '(' + self.code_list[self.tmp_index+1] + ')', 's')
        self.match('READ')
        self.match('ID')
        return t

    def write_stmt(self):
        t = Node('WRITE', '', 's')
        self.match('WRITE')
        t.set_children(self.exp())
        return t

    def create_nodes_table(self, args=None):
        if args == None:
            self.parse_tree.index = Parser.tmp_index
            Parser.nodes_table.update(
                {Parser.tmp_index: [self.parse_tree.token_value, self.parse_tree.code_value, self.parse_tree.shape]})
            Parser.tmp_index = Parser.tmp_index+1
            if len(self.parse_tree.children) != 0:
                for i in self.parse_tree.children:
                    self.create_nodes_table(i)
            if self.parse_tree.sibling != None:
                self.create_nodes_table(self.parse_tree.sibling)
        else:
            args.index = Parser.tmp_index
            Parser.nodes_table.update(
                {Parser.tmp_index: [args.token_value, args.code_value, args.shape]})
            Parser.tmp_index = Parser.tmp_index+1
            if len(args.children) != 0:
                for i in args.children:
                    self.create_nodes_table(i)
            if args.sibling != None:
                self.create_nodes_table(args.sibling)

    def create_edges_table(self, args=None):
        if args == None:
            if len(self.parse_tree.children) != 0:
                for i in self.parse_tree.children:
                    Parser.edges_table.append((self.parse_tree.index, i.index))
                for j in self.parse_tree.children:
                    self.create_edges_table(j)
            if self.parse_tree.sibling != None:
                Parser.edges_table.append(
                    (self.parse_tree.index, self.parse_tree.sibling.index))
                self.same_rank_nodes.append(
                    [self.parse_tree.index, self.parse_tree.sibling.index])
                self.create_edges_table(self.parse_tree.sibling)
        else:
            if len(args.children) != 0:
                for i in args.children:
                    Parser.edges_table.append((args.index, i.index))
                for j in args.children:
                    self.create_edges_table(j)
            if args.sibling != None:
                Parser.edges_table.append((args.index, args.sibling.index))
                self.same_rank_nodes.append([args.index, args.sibling.index])
                self.create_edges_table(args.sibling)

    def run(self):
        self.parse_tree = self.stmt_sequence()  # create parse tree
        self.create_nodes_table()  # create nodes_table
        self.create_edges_table()  # create edges_table
        self.edges_table = Parser.edges_table  # save edges_table
        self.nodes_table = Parser.nodes_table  # save nodes_table
        Return = []
        if (self.tmp_index < len(self.tokens_list) - 1) or self.error:
            Return.append(True)
        elif self.tmp_index == len(self.tokens_list)-1:
            Return.append(False)
        Return.append(self.errorToken)
        self.errorToken = []
        self.error = False
        return Return


    def clear_tables(self):
        self.nodes_table.clear()
        self.edges_table.clear()
