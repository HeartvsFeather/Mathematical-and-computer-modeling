import numpy as np
import matplotlib.pyplot as plot

def f(x): # f(x)
    return np.cos(3 * x) + 0.2 * x

def df(x): # derivative of f(x)
    return -3 * np.sin(3 * x) + 0.2

x_plt = np.arange(-5.0, 5.0, 0.05) # x's with 0.05 step
f_plt = [f(x) for x in x_plt] # y(x)'s

fig, ax = plot.subplots() # built graph of f(x)
ax.grid(True)
ax.plot(x_plt, f_plt)
plot.show()

df_plt = [df(x) for x in x_plt] # built graph of df(x) with feathers
get_ipython().run_line_magic('matplotlib', 'notebook')
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

for i in range(1, 1000): # x = x - df(x_null)
    lr = 1 / i # length of i step
    x = x - lr * np.sign(df(x)) # step to right or to left with lr length step
    
    print(f"{'{:.4f}'.format(lr)} | {'{:.4f}'.format(x)} | {'{:.4f}'.format(f(x))} | {'{:.4f}'.format(df(x))}")
    
print(f"\nСпуск градиента нас привел к от точки с координатами ({'{:.2f}'.format(x_null)}, {'{:.2f}'.format(f(x_null))}) к точке c координатами ({'{:.2f}'.format(x)}, {'{:.4f}'.format(f(x))})")
