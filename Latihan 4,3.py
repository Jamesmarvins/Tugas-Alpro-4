celcius_to_fahrenheit = lambda C: (9/5) * C + 32

celcius_to_reamur = lambda C: 0.8 * C

C = 100
F = celcius_to_fahrenheit(C)
print(f"Input C = {C}. Output F = {F}.")

C = 80
R = celcius_to_reamur(C)
print(f"Input C = {C}. Output R = {R}.")

C = 0
F = celcius_to_fahrenheit(C)
print(f"Input C = {C}. Output F = {F}.")