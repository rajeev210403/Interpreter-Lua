###############################################################################     
#                                                                             #
#                                  LUA(Team-12)                               #
#                                                                             #
###############################################################################

PLUS='PLUS'
MINUS='MINUS'
MUL='MUL'
DIV='DIV'
MOD='MOD'
INTEGER='INTEGER'
REAL='REAL'
EOF='EOF'
STRING='STRING'
TRUE='TRUE'
FALSE='FALSE'
ID='ID'

EQUAL='=='
NOT='!='
GREATER='>'
LEST='<'
GRTE='>='
LESE='<='
ASSIGN='='
SEMI=';'
COMMA=','
DOT='.'
LEFTPAR='('
RIGHTPAR=')'
APOS='"'

FOR='for'
WHILE='while'
IF='if'
THEN ='then'                                                          #Used in if statement in LUA
DO ='do'                                                              #Used in WHILE Loop  in LUA
END = 'end'                                                           #Used in WHILE Loop  in LUA
ELSE='else'
ELSIF='elsif'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self._str_()


RESERVED_KEYWORDS={
    'if': Token(IF,'if'),
    'elsif': Token(ELSIF, 'elsif'),                         
    'else': Token(ELSE, 'else'),
    'while': Token(WHILE, 'while'),
    'do':Token(DO, 'do'),                                        #Used with while loop in LUA
    'end':Token(END,'end'),
    'then':Token(THEN,'then'),
}

###############################################################################
#                                                                             #
#                                  LEXER                                      #
#                                                                             #
###############################################################################

class Lexer(object):
    def __init__(self, text):
        # string input: "23 + 13"
        self.text = text
        # index to the text
        self.pos = 0
        # line of the text
        self.line = 1
        # current token
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid syntax')
    

    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            
    

    def peek(self, n):
        peek_pos = self.pos + n
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_white_space(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line += 1
            self.advance()

    def skip_comment(self): #for skipping the comment
        while self.current_char not in ['\n','\x00']:
            self.advance()

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
                token = Token('REAL', float(result))

        else:
            token = Token('INTEGER', int(result))
        return token

    def string(self):
        result = ''
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()
        token = Token('STRING', result)
        return token

    def _id(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum() or self.current_char=='_':
            result += self.current_char
            self.advance()

        token = RESERVED_KEYWORDS.get(result, Token(ID, result))
        return token

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            
            if self.current_char == '-' and self.peek(1) =='-':
                self.advance()
                self.skip_comment()                                                      #This is for skipping the comment
                continue
            
            if self.current_char.isspace():
                self.skip_white_space()                                                  #Any white spaces in the code will be ignored
                continue

            if self.current_char.isdigit():
                return self.number()
            
            if self.current_char.isalpha():
                return self._id()

            if self.current_char == '=' and self.peek(1) !='=':
                self.advance()
                return Token(ASSIGN, '=')

            if self.current_char == '=' and self.peek(1)=='=':
                self.advance()
                self.advance()
                return Token(EQUAL, '==')

            if self.current_char == '!' and self.peek(1)=='=':
                self.advance()
                self.advance()
                return Token(NOT, '!=')

            if self.current_char == '>' and self.peek(1)!='=':
                self.advance()
                return Token(GREATER, '>')

            if self.current_char == '<' and self.peek(1) == '=':
                self.advance()
                self.advance()
                return Token(LESE, '<=')

            if self.current_char == '>' and self.peek(1) != '=':
                self.advance()
                return Token(GRTE, '>')

            if self.current_char == '<' and self.peek(1) != '=':
                self.advance()
                return Token(LEST, '<')

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')
            
            if self.current_char=='f' and self.peek(1)=='o' and self.peek(2)=='r':
                self.advance()
                self.advance()
                self.advance()
                return Token(FOR,'for')
            
            if self.current_char == 'w' and self.peek(1) == 'h' and self.peek(2) == 'i' and self.peek(3) == 'l' and self.peek(4) == 'e' and self.peek(5):
                for x in range (1,6):
                    self.advance()
                return Token(WHILE, 'while')

            if self.current_char == 'i' and self.peek(1) == 'f':
                self.advance()
                self.advance()
                return Token(IF, 'if')
            
            if self.current_char =='t' and self.peek(1)=='h' and self.peek(2)=='e'and self.peek(3)=='n':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return Token(THEN,'then')
            
            if self.current_char=='d' and self.peek(1)=='o':
                self.advance()
                self.advance()
                return Token(DO,'do')
            
            if self.current_char=='e' and self.peek(1)=='n' and self.peek(2)=='d':
                self.advance()
                self.advance()
                self.advance()
                return Token(END,'end')

            if self.current_char=='e' and self.peek(1)=='l' and self.peek(2)=='s' and self.peek(3)=='e':
                self.advance()
                self.advance()
                self.advance()
                self.advance()
                return Token(ELSE,'else')
            
            if self.current_char == 'e' and self.peek(1) == 'l' and self.peek(2) == 's' and self.peek(3) == 'i' and self.peek(4) == 'f':
                for x in range (0,5):
                    self.advance()
                return Token(ELSIF,'elsif')
            
            if self.current_char == '.':
                self.advance()
                return Token(DOT, '.')

            if self.current_char == '(':
                self.advance()
                return Token(LEFTPAR, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(RIGHTPAR, ')')

            if self.current_char == '"':
                self.advance()
                return Token(APOS,'"')

            self.error()

        return Token(EOF, None)


###############################################################################
#                                                                             #
#                                   PARSER                                    #
#                                                                             #
###############################################################################
class AST(object):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Compound(AST):
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Var(AST):
    def __init__(self,token):
        self.token=token
        self.value=token.value

class If(AST):
    def __init__(self, condition, body, rest):
        self.condition = condition
        self.body = body
        self.rest = rest


class While(AST):
    def __init__(self, condition,  body):
        self.condition = condition
        self.body = body
        

class NoOp(AST):
    pass

class Parser(object):
    def __init__(self,lexer):
        self.lexer=lexer
        self.current_token=self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')
    
    def eat(self,token_type):
        
        print(self.current_token.type)
        if self.current_token.type==token_type:
            self.current_token=self.lexer.get_next_token()
        else:
            self.error()

    def program(self):
        node=self.compound_statement()
        return node

    def compound_statement(self):
        nodes = self.statement_list()
        root=Compound()
        for node in nodes:
            root.children.append(node)
        return root

    def statement_list(self):
        node = self.statement()
        results = [node]
        while self.current_token.type != EOF:
            results.append(self.statement())

        return results

    def statement(self):
        if self.current_token.type==ID:
            node=self.assignment_statement()
        elif self.current_token.type==IF:
            node=self.if_statement()
        elif self.current_token.type==WHILE:
            node=self.while_statement()
        elif self.current_token.type == THEN:
            node = self.extra_stmt()
        elif self.current_token.type == END:
            node=self.extra_stmt()
        else:
            node=self.conditional_statement()
        return node
    
    
        

    def assignment_statement(self):
        left = self.variable()
        self.eat(ID)
        print(self.variable())
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def if_statement(self):
        self.eat(IF)
        condition = self.conditional_statement()
        self.eat(THEN)
        body = self.statement_list()
        rest = self.empty()
           
        if self.current_token.type == ELSE:
            self.eat(ELSE)
            rest = self.statement_list()
        
        node = If(condition,body,rest)
        
        return node

    def while_statement(self):
        self.eat(WHILE)
        condition=self.conditional_statement()
        
        self.eat(DO)
    
        body=self.statement_list()
        node=While(condition,body)
        return node
    
    
        
        
    def variable(self):
        node = Var(self.current_token)
        # self.eat(ID)
        return node

    def empty(self):
        return NoOp()

    def elsif_statement(self):
        self.eat(ELSIF)
        elsif_condition=self.conditional_statement()
        elsif_body=self.statement_list()
        rest=self.empty()
        while self.current_token.type==ELSIF:
            rest=self.elsif_statement()
        if self.current_token.type==ELSE:
            self.eat(ELSE)
            rest=self.statement_list()
        node=If(elsif_condition,elsif_body,rest)
        return node

    def conditional_statement(self):
        
        node=self.expr()
        while self.current_token.type in (EQUAL,GRTE,NOT,GREATER,LESE,LEST):
            token=self.current_token()
            self.eat(token.type)
            node=BinOp(node,token,self.expr())
        
        return node
    
    def extra_stmt(self):
        token = self.current_token
        if token.type == END:
            self.eat(END)
        if token.type == THEN:
            self.eat(THEN)
        
        

    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(node,token,self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (MUL,DIV, MOD,EQUAL,NOT,LEST,GREATER,LESE,GRTE):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)
            elif token.type == MOD:
                self.eat(MOD)
            elif token.type == EQUAL:
                self.eat(EQUAL)
            elif token.type == NOT:
                self.eat(NOT)
            elif token.type == LEST:
                self.eat(LEST)
            elif token.type == GREATER:
                self.eat(GREATER)
            elif token.type == LESE:
                self.eat(LESE)
            elif token.type == GRTE:
                self.eat(GRTE)
            node = BinOp(node,token,self.factor())

        return node

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == REAL:
            self.eat(REAL)
            return Num(token)
        elif token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == LEFTPAR:
            self.eat(LEFTPAR)
            node = self.expr()
            self.eat(RIGHTPAR)
            return node
        elif token.type == ID:
            self.eat(ID)
            return Var(token)
        elif token.type == STRING:
            self.eat(STRING)
            return Num(token)
        else:
            node = self.variable()
            return node

    def parse(self):
        node = self.program()
        while self.current_token.type != EOF:
            self.error()
        return node


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    
    GLOBAL_MEMORY = {}
    
    def __init__(self, tree):
        self.tree = tree

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif node.op.type == MOD:
            return self.visit(node.left) % self.visit(node.right)
        elif node.op.type == EQUAL:
            return self.visit(node.left) == self.visit(node.right)
        elif node.op.type == NOT:
            return self.visit(node.left) != self.visit(node.right)
        elif node.op.type == GRTE:
            return self.visit(node.left) >= self.visit(node.right)
        elif node.op.type == LESE:
            return self.visit(node.left) <= self.visit(node.right)
        elif node.op.type == GREATER:
            return self.visit(node.left) > self.visit(node.right)
        elif node.op.type == LEST:
            return self.visit(node.left) < self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_value = self.visit(node.right)
        self.GLOBAL_MEMORY[var_name] = var_value

    def visit_Var(self, node):
        var_name = node.value
        var_value = self.GLOBAL_MEMORY.get(var_name)
        if var_value is None:
            raise NameError(repr(var_name))
        return var_value

    def visit_If(self, node):
        if self.visit(node.condition):
            self.visit(node.body)
        else:
            self.visit(node.rest)

    def visit_While(self, node):
        while self.visit(node.condition):
            self.visit(node.body)

    def visit_list(self, node):
        for child in node:
            self.visit(child)

    def visit_NoOp(self, node):
        pass

    def interpret(self):
        tree = self.tree
        if tree is None:
            return ''
        return self.visit(tree)
        


def main():
    text=" a"
    lex = Lexer(text)
    par = Parser(lex)
    tree = par.parse()
    print(tree)
    inter = Interpreter(tree)
    result = inter.interpret()
    print('Run-time GLOBAL_MEMORY contents:')
    print(inter.GLOBAL_MEMORY)

if __name__ == '__main__':
    main()
