# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,40,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,1,1,1,1,1,1,5,1,28,8,
        1,10,1,12,1,31,9,1,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,0,1,2,3,0,
        2,4,0,0,42,0,6,1,0,0,0,2,20,1,0,0,0,4,37,1,0,0,0,6,7,3,2,1,0,7,8,
        5,0,0,1,8,1,1,0,0,0,9,10,6,1,-1,0,10,21,3,4,2,0,11,12,3,4,2,0,12,
        13,5,2,0,0,13,21,1,0,0,0,14,15,3,4,2,0,15,16,5,3,0,0,16,21,1,0,0,
        0,17,18,3,4,2,0,18,19,5,4,0,0,19,21,1,0,0,0,20,9,1,0,0,0,20,11,1,
        0,0,0,20,14,1,0,0,0,20,17,1,0,0,0,21,29,1,0,0,0,22,23,10,5,0,0,23,
        28,3,2,1,6,24,25,10,4,0,0,25,26,5,1,0,0,26,28,3,2,1,5,27,22,1,0,
        0,0,27,24,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,3,
        1,0,0,0,31,29,1,0,0,0,32,38,5,7,0,0,33,34,5,5,0,0,34,35,3,2,1,0,
        35,36,5,6,0,0,36,38,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,38,5,1,0,
        0,0,4,20,27,29,37
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'+'", "'*'", "'?'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CHAR", "WS" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_atom = 2

    ruleNames =  [ "start", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CHAR=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ExprParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr(0)
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStarExpr" ):
                return visitor.visitStarExpr(self)
            else:
                return visitor.visitChildren(self)


    class AskExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAskExpr" ):
                return visitor.visitAskExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConnectExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnectExpr" ):
                return visitor.visitConnectExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class PlusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusExpr" ):
                return visitor.visitPlusExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 10
                self.atom()
                pass

            elif la_ == 2:
                localctx = ExprParser.PlusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.atom()
                self.state = 12
                self.match(ExprParser.T__1)
                pass

            elif la_ == 3:
                localctx = ExprParser.StarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.atom()
                self.state = 15
                self.match(ExprParser.T__2)
                pass

            elif la_ == 4:
                localctx = ExprParser.AskExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.atom()
                self.state = 18
                self.match(ExprParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 27
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ConnectExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 23
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.OrExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 25
                        localctx.op = self.match(ExprParser.T__0)
                        self.state = 26
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CharExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharExpr" ):
                return visitor.visitCharExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = ExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ExprParser.CharExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(ExprParser.CHAR)
                pass
            elif token in [5]:
                localctx = ExprParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(ExprParser.T__4)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(ExprParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




