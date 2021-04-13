class Calculator:

    def __init__(self):
        self.stack = []
        self.history = []

    def inp(self, val):
        self.stack.append(val)

    def pop(self):
        try:
            first = self.stack.pop()
            second = self.stack.pop()
            return(first,second)
        except:
            try:
                self.stack.append(first)
                print('--- Only one value available in stack. ---')
            except:
                print('--- No values in stack. ---')
    
    def add(self):
        try:
            first,second = self.pop()
            self.stack.append(first+second)
        except:
            self.history.pop()

    def sub(self):
        try:
            first,second = self.pop()
            self.stack.append(second-first)
        except:
            self.history.pop()
    
    def mul(self):
        try:
            first,second = self.pop()
            self.stack.append(first*second)
        except:
            self.history.pop()
    
    def div(self):
        try:
            first,second = self.pop()
            self.stack.append(second/first)
        except ZeroDivisionError:
            print('--- Cannot divide by 0. ---')
            self.stack.append(second)
            self.stack.append(first)
            self.history.pop()
        except:
            self.history.pop()
    
    def power(self):
        try:
            first,second = self.pop()
            self.stack.append(second**first)
        except:
            self.history.pop()

    def show(self):
        print('\nHistory:', self.history)
        print('Stack:', self.stack)
    
    def hist(self, val):
        try:
            if val == 'clear' and self.history[-1] == 'clear':
                None
            else:
                self.history.append(val)
        except:
            self.history.append(val)
        
    
func = Calculator()

print('Enter number and operants one by one in order.')
print("Type 'clear' to clear the calculator.")
print("Type 'q' to quit.")
while True:
    func.show()
    inp = input('Input: ')
    func.hist(inp)
    if inp.isdigit():
        func.stack.append(int(inp))
    elif inp == '/':
        func.div()
    elif inp == '+':
        func.add()
    elif inp == '-':
        func.sub()
    elif inp == '*':
        func.mul()
    elif inp == '^':
        func.power()
    elif inp == 'clear':
        func.stack = []
    elif inp == 'q':
        break
    else:
        print('--- Invalid Entry ---')
        func.history.pop()