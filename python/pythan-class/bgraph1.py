import matplotlib.pyplot as p
ppA=[77,89,100,98,65]
sub=["OS","C","Python","CG","Java"]
p.xlabel("Subjects")
p.ylabel("Pass%")
p.title("Pass % of Students")
p.bar(sub,ppA,width=0.5,color=["red","blue","green","yellow","cyan"])
p.legend()
p.show()

