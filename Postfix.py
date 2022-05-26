class stack:

    def __init__(self, max_length):
        self.max_length = max_length
        self.top = -1
        self.capacity = [None] * max_length

    def isFull(self):
        if self.top == self.max_length - 1:
            return True
        return False

    def push(self, data):
        if (self.isFull == True):
            print("Error")
        else:
            self.top +=  1
            self.capacity[self.top] = data
            return data

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def pop(self):
        if (self.isEmpty == True):
            print("Error")
        else:
            data=self.capacity[self.top]
            self.top -= 1
            

            return data


def EvaluateExpression(exp):
    
    st = stack(len(exp))

    for i in exp:
        if i.isdigit():        
            st.push(i)      
        else:
            v1 = st.pop()
            v2 = st.pop()
            
            st.push(str(eval(v2 + i + v1)))
            
    return st.pop()
                


print(float(EvaluateExpression(input())))