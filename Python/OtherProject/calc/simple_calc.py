#! /usr/bin/env python

from random import randint

class simple_calc:
    def __init__(self):
        self.template = '''
            <table tabindex="65535" class="xdLayout" style="word-wrap: break-word; border-top: medium none; border-right: medium none; width: 700px; border-collapse: collapse; table-layout: fixed; border-bottom: medium none; border-left: medium none"
            bordercolor="#ffffff" border="1" >
                <tbody>
                    %s
                </tbody>
            </table>
        '''
        self.sub_template1 = '''
        <tr style="min-height: 25px" height=100px>
            <td align = 'center'><font size=8px>%s</font></td>
            <td align = 'center'><font size=8px>%s</font></td>
        </tr>
        '''
        self.op_dict = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: x/y,
        }
    
    def xgen(self):
        i = 1
        while True:
            yield i
            i += 1

    def gen_calc(self, op, xparam, yparam, n):
        itemplate = '%i %s %i = (%s)'
        ispace = '&nbsp;' * 5 
        items = []
        for i in range(n):
            items.append(itemplate % (xparam(), op,  yparam(), ispace))
        return items
        
    def render(self, items, nline):
        ss = ''
        for i in range(1, int(nline/2)+1):
            sub_str = self.sub_template1 % (items[(2*i-1)-1], items[(2*i)-1])
            ss += sub_str
        sstr = self.template % ss
        return sstr

    def simple_add(self, xxp, nline):        
        g1, g2 = self.xgen(), self.xgen()
        items = self.gen_calc('+', lambda : xxp, lambda : next(g1), int(nline/2))
        items += self.gen_calc('+', lambda : next(g2), lambda : xxp, int(nline/2))
        return self.render(items, nline)

if __name__ == '__main__':
    scalc = simple_calc()

    # tfile = 'output/simple_calc_%i.html'
    # for i in range(10):
    #     with open(tfile % i, 'w') as f:
    #         f.write(scalc.simple_add(i, 20))
    tfile = 'output/simple_calc.html'
    with open(tfile, 'w') as f:
        for i in range(10+1):
            f.write(scalc.simple_add(i, 20))


    
    
