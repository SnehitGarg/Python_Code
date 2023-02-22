class Evaluate:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
 # This array is used a stack
        self.array = []
 # check if the stack is empty
    def isEmpty(self):
         return True if self.top == -1 else False
 # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
 # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
             self.top -= 1
             return self.array.pop()
        else:
            return "$"
    def push(self, op):
        self.top += 1
        self.array.append(op)
    def evaluatePostfix(self, exp):
        for i in exp:
            if i.isdigit():
                 self.push(i) 
            else:
                  val1 = self.pop()
                  val2 = self.pop()
                  self.push(str(eval(val2 + i + val1)))
        return int(self.pop())
exp = "231*+9-"
obj = Evaluate(len(exp))
print ("postfix evaluation: %d"%(obj.evaluatePostfix(exp))) 