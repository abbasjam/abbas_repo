import matplotlib.pyplot as p
ppA=[77,89,100,98,65]
ppB=[89,76,71,76,70]
sub=["OS","C","Python","CG","Java"]
p.xlabel("Subjects")
p.ylabel("Pass%")
p.title("Pass % of Students")
p.plot(sub,ppA,label="I BCA A",color="green",linestyle="dotted",linewidth=4)
p.plot(sub,ppB,label="I BCA B",color="red",linestyle="dashed",linewidth=4)
p.legend()
p.show()

