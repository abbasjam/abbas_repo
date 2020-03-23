import matplotlib.pyplot as p
ppA=[77,89,100,98,65]
ppB=[89,76,71,76,70]
sub=["OS","C","Python","CG","Java"]
p.xlabel("Subjects")
p.ylabel("Pass%")
p.title("Pass % of Students")
p.plot(sub,ppA,label="I BCA A")
p.plot(sub,ppB,label="I BCA B")
p.legend()
p.show()

