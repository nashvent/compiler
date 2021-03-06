#!/usr/bin/env python
import sys
from Parser.functions import parse_bnf, pprint_table, remove_left_recursion, remove_left_factoring
from queue import LifoQueue
from anytree import Node, RenderTree

def do_the_whole_thing(grammar_text, epsilon='ε', eof='$', output=None, verbose=True):
    file = None
    if output:
        file = open(output, 'w')
        sys.stdout = file

    vprint = print if verbose else lambda *a, **key: None  # Only print if verbose is True

    vprint("Original:")
    g = parse_bnf(grammar_text, epsilon=epsilon, eof=eof)
    vprint(g)

    vprint("\nAfter removing left-recursion:")
    g = remove_left_recursion(g)
    vprint(g)

    vprint("\nAfter removing left-factoring:")
    g = remove_left_factoring(g)
    vprint(g)

    vprint()
    for nt in g.nonterminals:
        vprint('FIRST({}) = {}'.format(nt, g.first(nt)))

    vprint()
    follow = [(nt, g.follow(nt)) for nt in g.nonterminals]

    for nt, f in follow:
        vprint('FOLLOW({}) = {}'.format(nt, f))

    vprint()
    table, ambiguous = g.parsing_table()
    vprint("Parsing Table: ")
    if ambiguous:
        vprint("El lenguaje de entrada no es LL(1) debido a que se encontraron ambigüedades.")

    vprint()
    pprint_table(g, table)

    if file:
        file.close()




class Stack(LifoQueue):
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[len(self.queue) - 1]


def parse_words(grammar, words):
    grammar = parse_bnf(grammar)
    table, ambiguous = grammar.parsing_table(is_clean=True)
    if ambiguous:
        raise Warning("Ambiguous grammar")

    error_list = []

    words.append("$")
    word = words.pop(0)
    stack = Stack()

    stack.put(("$", None))
    root = Node(grammar.start)
    stack.put((grammar.start, root))

    top_stack = stack.peek()
    while True:
        print(f"Current_word:{word},  Stack:{stack.queue}")
        if top_stack[0] == "$" and word == "$":
            if not error_list:
                return True, root, None
            else:
                return False, root, error_list

        if grammar.is_terminal(top_stack[0]):
            if top_stack[0] == word:
                print(f"Consume input: {word}")
                stack.get()
                word = words.pop(0)
            else:
                error_list.append(f"Expected {top_stack[0]}")
                while word != top_stack[0]:
                    if word == "$":
                        return False, root, error_list
                    word = words.pop(0)
        else:
            rule = table.get((top_stack[0], word))
            stack.get()
            if rule:
                print(f"Rule: {rule}")
                symbols = rule.body[::-1]
                for symbol in symbols:
                    node = Node(symbol, parent=top_stack[1])
                    if symbol != "ε":
                        stack.put((symbol, node))
            else:
                error_list.append(f"Unexpected character:{word}. Expected: {grammar.first(top_stack[0])}")
                follow = grammar.follow(top_stack[0]) + ["$"]
                print(f"Error! Sync set: {follow}")
                while word not in follow:
                    print(f"Skipped: {word}")
                    word = words.pop(0)
        top_stack = stack.peek()
