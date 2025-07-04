class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'
    
    #def __getattribute__(self, attr):                
    #   return 'calling __getattribute__'
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {key: getattr(self, key) + getattr(other, key) for key in vars(self)}
        return self.__class__(**kwargs)
        
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)

# Demonstrating __getattribute__ calls
print(f'Accessing x with dot operator: {v1.x}')
print(f'Accessing x with getattr(): {getattr(v1, "x")}')
#print(v1.z)
#print(getattr(v1, 'z'))