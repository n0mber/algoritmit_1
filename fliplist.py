class FlipList:
    
    def push_last(self,x):
        self = [10**5]
        self[len(self)] = x 
        return self

    def push_first(self,x):
        lst = self.insert(0, x)
        return lst

    def pop_last(self):
        lst = self.pop()
        return lst

    def pop_first(self):
        self = self[::-1]
        self.pop()
        lst = self[::-1]
        return lst

    def flip(self):
        lst = self[::-1]
        return lst

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first()) # 1
    f.flip()
    print(f.pop_first()) # 3