class Robot:
    components = []  # Class variable

r1 = Robot()
r2 = Robot()

r1.components.append("arm")  # Affects both r1 and r2
print(r2.components)         # Output: ['arm']

r1.components = ["leg"]      # Shadows the class variable!
print(r2.components)         # Output: ['arm'] (r2 still looks at class variable)
