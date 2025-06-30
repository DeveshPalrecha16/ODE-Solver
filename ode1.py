def f(t,y):
    return t + y

def rk4(f,t0,y0,h,t_end):
    t=t0
    y=y0
    steps=int((t_end - t0)/h)
    for steps in range(steps+1):
        print(f"Step {steps}: t = {t:.4f}, y = {y:.4f}")

        k1=h*f(t,y)
        k2=h*f(t+h/2,y+k1/2)
        k3=h*f(t+h/2,y+k2/2)
        k4=h*f(t+h,y+k3)
        y += (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        t += h 

def main():
            
    t0 = float(input("Enter initial t (t0): "))
    y0 = float(input("Enter initial y (y0): "))
    t_end = float(input("Enter final t (t_end): "))
    h = float(input("Enter step size (h): "))

    print("\nAssuming dy/dt = t + y\n")
    
    rk4(f, t0, y0, h, t_end)

if __name__ == "__main__":
    main()
    