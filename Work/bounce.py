# bounce.py
#
# Exercise 1.5
height = 100 # meters
loss_rate = 3/5
n_bounces = 10

for n in range(n_bounces):
    height = round(loss_rate * height, 4)
    print(n, height )