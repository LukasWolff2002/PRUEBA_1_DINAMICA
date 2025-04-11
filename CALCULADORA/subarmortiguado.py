import sympy as sp

# Declarar símbolos
G1, G2 = sp.symbols('G1 G2')
beta, omega_n, omega_d = sp.symbols('beta omega_n omega_d', positive=True)
u0, v0 = sp.symbols('u0 v0')  # posición y velocidad inicial

# Sistema de ecuaciones en t = 0
eq1 = sp.Eq(G1 + G2, u0)
eq2 = sp.Eq(-beta * omega_n * (G1 + G2) + omega_d * (G1 - G2), v0)

# Resolver el sistema
sol = sp.solve((eq1, eq2), (G1, G2), dict=True)[0]

# Mostrar las soluciones
G1_expr = sol[G1].simplify()
G2_expr = sol[G2].simplify()

print("G1 =")
sp.pprint(G1_expr, use_unicode=True)
print("\nG2 =")
sp.pprint(G2_expr, use_unicode=True)
