#! /usr/bin/env python
import math
import sys

def main():
    op = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    if op == 'v':
        result = s_to_v(arg2, int(arg3))
    elif op == 's':
        result = v_to_s(make_vector(arg2), sys.argv[3:])
    print(result)

def make_vector(str):
    v = list(str[1:len(str)-1])
    for i in range(v.count(',')):
	v.remove(',')
    for i in range(len(v)):
	v[i] = int(v[i])
    return v
    
def test():
    for i in range(2 ** (2 ** 4)):
        v = env(i, 16)
        s = v_to_s(v, ['G1', 'G2', 'G3', 'G4'])
        nv = s_to_v(s, 4)
        print(i, v, v == nv, s)

def v_to_s(v, names):
    tokens = []
    n = math.log(len(v),2)
    if n == len(names):
        x = v.count(1)
        y = v.count(0)
        if x == len(v):
            return '1'
        elif y == len(v):
            return '0'
        elif x <= y:
            for i in range(len(v)):
                if v[i] == 1:
                    vals = env(i, int(n))
                    for j in range(len(vals)):
                        if vals[j] == 1:
                            tokens.append(names[j])
                            tokens.append('&')
                        else:
                            tokens.append('!')
                            tokens.append(names[j])
                            tokens.append('&')
                    tokens.pop()
                    tokens.append('|')
            if len(tokens) > 1:
                tokens.pop()
        else:
            tokens.append('!')
            tokens.append('(')
            for i in range(len(v)):
                if v[i] == 0:
                    vals = env(i, int(n))
                    for j in range(len(vals)):
                        if vals[j] == 1:
                            tokens.append(names[j])
                            tokens.append('&')
                        else:
                            tokens.append('!')
                            tokens.append(names[j])
                            tokens.append('&')
                    tokens.pop()
                    tokens.append('|')
            if len(tokens) > 1:
                tokens.pop()
            tokens.append(')')
        s = t_to_s(tokens)
    return s

def t_to_s(tokens):
    s = ''
    if len(tokens) > 0:
        for i in range(len(tokens) - 1):
            s = s + tokens[i] + ' '
        s = s + tokens[len(tokens) - 1]
    return s

def s_to_v(s, n):
    v = []
    tokens = make_tokens(s) # Build list of clean tokens
    parenthesis = check_parenthesis(tokens)
    if parenthesis == 0:
        return v
    nodes = find_nodes(tokens)
    exp = make_expression(tokens)
    for i in range(2 ** n):
        vals = env(i, n)
        d = dict(zip(nodes, vals))
        r = eval(exp, d)
        if r:
            v.append(1)
        else:
            v.append(0)
    return v            

def make_expression(tokens):
    exp = ''
    for s in tokens:
        exp = exp + s + ' '
    return exp

def env(n, m):
    en = []
    nc = n
    for i in range(m):
        en.append(nc % 2)
        nc = int(nc/2)
    en.reverse()
    return en
    
def make_tokens(s):
    h1 = s.split('(')
    h2 = []
    for i in range(len(h1)-1):
        h2.append(h1[i])
        h2.append(' ( ')
    h2.append(h1[len(h1)-1])
    h1 = []
    h3 = partition_all(h2, ')', ')')
    h4 = partition_all(h3, '!', 'not')
    h5 = partition_all(h4, '&', 'and')
    h6 = partition_all(h5, '|', 'or')
    for i in range(h6.count(' ')):
        h6.remove(' ')
    for i in range(h6.count('')):
        h6.remove('')
    h1 = []
    for s in h6:
        h1.append(s.strip())
    return h1

def partition_all(str_lst, sep, d):
    l = []
    for i in range(len(str_lst)):
        h1 = str_lst[i].split(sep)
        for i in range(len(h1)-1):
            l.append(h1[i])
            l.append(d)
        l.append(h1[len(h1)-1])
    return l

def check_parenthesis(tokens):
    p = 0
    for t in tokens:
        if t == ')':
            p = p - 1
            if p < 0:
                return 0
        elif t == '(':
            p = p + 1
    if p == 0:
        return 1
    else:
        return 0
    
def find_nodes(tokens):
    nl = []
    for t in tokens:
	if not(t == 'not' or t == 'and' or t == 'or' or t == ')' or t == '(' or t == ')' or nl.count(t) > 0):
		nl.append(t)
    return nl

main()
