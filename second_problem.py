import numpy as np
import matplotlib.pyplot as plot

def f(x): # f(x)
    return np.cos(3 * x) + 0.2 * x

def df(x): # derivative of f(x)
    return -3 * np.sin(3 * x) + 0.2

x_plt = np.arange(-5.0, 5.0, 0.01) # x's with 0.05 step
f_plt = [f(x) for x in x_plt] # y(x)'s
df_plt = [df(x) for x in x_plt] # dy(x)'s

# built graph of df(x) with feature
get_ipython().run_line_magic('matplotlib', 'notebook') #feature
fig, ax = plot.subplots()
ax.grid(True)
ax.plot(x_plt, df_plt)
plot.show()

x_null = 0 # at this point start grad descent
y = f(x_null) # y(x_null)
x = x_null
N = 1000 # amount of steps
lr = 1 # length of first step

# definition of colmns
print("Длина шага | Икс | Игрек от икса| Игрек производной от икса|\n")

for i in range(1, N): # x = x - df(x_null)
    lr = 1 / i # length of i step
    
    x = x - lr * np.sign(df(x)) # step to right or to left with lr length step
    
    print(f"{'{:.4f}'.format(lr)} | {'{:.4f}'.format(x)} | {'{:.4f}'.format(f(x))} | {'{:.4f}'.format(df(x))}")

res = x

x = x_null

# built graph of f(x) with feature
fig, ax = plot.subplots()
ax.grid(True)
ax.plot(x_plt, f_plt)

for i in range(1, N):
    lr = 0.05 # length of step if need careful arrows on graph
    
    x_prev = x
    y_prev = f(x)
    
    if x_prev >= x:
        dx = -(x_prev - x)
    else:
        dx = x - x_prev
    if y_prev >= f(x):
        dy = -(y_prev - f(x))
    else:
        dy = f(x) - y_prev
    plot.arrow(x = x_prev, y = y_prev, dx = dx, dy = dy, width= .03)
    
    x = x - lr * np.sign(df(x))
    
print(f"\nСпуск градиента нас привел к от точки с координатами ({'{:.2f}'.format(x_null)}, {'{:.2f}'.format(f(x_null))}) к точке c координатами ({'{:.2f}'.format(res)}, {'{:.2f}'.format(f(res))})")

plot.show() # graph with arrows
