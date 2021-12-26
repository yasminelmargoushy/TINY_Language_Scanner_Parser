ReservedWords = ["if", "then", "else", "end", "repeat", "until", "read", "write"]
SpecialSymbols = ['+', '-', '*', '/', '=', '<', '>', '(', ')', ';']
SpecialSymbolsSTR = ["PLUS", "MINUS", "MULT", "DIV", "EQUAL", "LESSTHAN", "GREATERTHAN", "OPENBRACKET", "CLOSEDBRACKET", "SEMICOLON"]

def Scan(InputTxt, nested):
    InputTxt += " "
    TokenList = []
    state = "Start"
    Token = ""
    OpenComments = 0
    LineNumber = 1
    for x in InputTxt:
        if x == '\n':
            LineNumber +=1
        if state == "Identifier":
            if (x.isalpha()) or (x.isnumeric()):
                Token += x
            else:
                if Token in ReservedWords:
                    TempList = [Token, "Reserved Word", Token.upper(), LineNumber]
                else:
                    TempList = [Token, state, "IDENTIFIER", LineNumber]
                TokenList.append(TempList)
                state = "Start"
                Token = ""
        elif state == "Number":
            if (x.isnumeric()) or (x == '.'):
                Token += x
            else:
                TempList = [Token, state, "NUMBER", LineNumber]
                TokenList.append(TempList)
                state = "Start"
                Token = ""
        elif state == "Comment":
            if nested:
                if x == '{':
                    OpenComments += 1
                elif x == "}":
                    OpenComments -= 1
                    if OpenComments == 0:
                        state = "Start"
                        continue
            else:
                if x == "}":
                    OpenComments = 0
                    state = "Start"
                    continue

        elif state == ":Special Symbol":
            if x == '=':
                Token += x
                TempList = [Token, "Special Symbol", "ASSIGN", LineNumber]
                state = "Start"
                TokenList.append(TempList)
                continue

        if state == "Start":
            if x.isalpha():
                state = "Identifier"
                Token = x
            elif x.isnumeric():
                state = "Number"
                Token = x
            elif x == " " or x == "\t" or x == "\n":
                Token = ""
                state = "Start"
            elif x == '{':
                state = "Comment"
                OpenComments += 1
            elif x == ':':
                state = ":Special Symbol"
                Token = x
            else:
                Token = ""
                state = "Start"
                if x in SpecialSymbols:
                    TempList = [x, "Special Symbol", SpecialSymbolsSTR[SpecialSymbols.index(x)], LineNumber]
                    TokenList.append(TempList)
                else:
                    TempList = [x, "Unexpected Symbol", "ERROR", LineNumber]
                    TokenList.append(TempList)

    return TokenList

def PrintTokens(TokenList):
    StringList = ""
    ERRORflag = False
    ReturnList = []
    for Token in TokenList:
        if Token[1] == "Unexpected Symbol":
            StringList += f"{Token[0]},{Token[2]} \t\t\t ERROR: UNEXPECTED SYMBOL\n"
            ERRORflag = True
        else:
            StringList += f"{Token[0]},{Token[2]} \n"
        ReturnList = [ERRORflag, StringList]
    return ReturnList
