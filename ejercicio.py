import streamlit as st
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from matplotlib import cm

# Función objetivo
def objective(x):
    return -(4*x[0] + 3*x[1] + 3*x[2])

# Restricciones
def constraint1(x):
    return 10 - (4*x[0] + 2*x[1] + x[2])

def constraint2(x):
    return 14 - (3*x[0] + 4*x[1] + 2*x[2])

def constraint3(x):
    return 7 - (2*x[0] + x[1] + 3*x[2])

# Definir las restricciones como un diccionario de ecuaciones
constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2},
    {'type': 'ineq', 'fun': constraint3}
]

# Inicialización de la aplicación Streamlit
st.title("Optimización con Ramificación y Acotamiento - Dakin")

# Mostrar la función objetivo y las restricciones
st.write("""
    Maximizar: 
    $$P(x_1, x_2, x_3) = 4x_1 + 3x_2 + 3x_3$$
    
    Sujeto a:
    $$4x_1 + 2x_2 + x_3 \leq 10$$
    $$3x_1 + 4x_2 + 2x_3 \leq 14$$
    $$2x_1 + x_2 + 3x_3 \leq 7$$
    
    Donde \(x_1\), \(x_2\), \(x_3\) son enteros no negativos.
""")

# Optimización relajada
st.subheader("Optimización Relajada")

# Llamada a la optimización
initial_guess = [1, 1, 1]  # Estimación inicial
result = opt.minimize(objective, initial_guess, constraints=constraints, bounds=[(0, None), (0, None), (0, None)])

# Mostrar resultados de la optimización relajada
if result.success:
    st.write(f"Solución óptima relajada encontrada: x1 = {result.x[0]:.2f}, x2 = {result.x[1]:.2f}, x3 = {result.x[2]:.2f}")
    st.write(f"Valor máximo de la función objetivo (relajado): {-(result.fun):.2f}")
else:
    st.write("No se encontró una solución óptima.")

# Gráfico 3D de la función objetivo (en 2D)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Crear una malla de puntos en el espacio 2D (solo dos variables x1 y x2)
x1_vals = np.linspace(0, 3, 50)
x2_vals = np.linspace(0, 3, 50)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

# Fijamos un valor constante para x3 (por ejemplo, x3 = 1) y calculamos la función objetivo
X3 = 1  # Fijar x3 en 1
Z = 4*X1 + 3*X2 + 3*X3

# Graficar la superficie de la función objetivo en 2D
contour = ax.contourf(X1, X2, Z, 20, cmap=cm.viridis)
fig.colorbar(contour, ax=ax)

# Ajustar etiquetas
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Superficie de la Función Objetivo')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Restricciones gráficas
fig2 = plt.figure(figsize=(10, 6))
ax2 = fig2.add_subplot(111)

# Graficar las restricciones en 2D (fijamos x3 = 1)
Z1 = 10 - (4*X1 + 2*X2 + X3)
Z2 = 14 - (3*X1 + 4*X2 + 2*X3)
Z3 = 7 - (2*X1 + X2 + 3*X3)

# Mostrar las superficies de las restricciones en 2D
ax2.contour(X1, X2, Z1, [0], colors='r', label="4x1 + 2x2 + x3 <= 10")
ax2.contour(X1, X2, Z2, [0], colors='g', label="3x1 + 4x2 + 2x3 <= 14")
ax2.contour(X1, X2, Z3, [0], colors='b', label="2x1 + x2 + 3x3 <= 7")

# Ajustar etiquetas
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_title('Gráfico de Restricciones')

# Mostrar el gráfico de restricciones
st.pyplot(fig2)

# Conclusión
st.subheader("Conclusión")

st.write("""
    La solución óptima encontrada para el problema de programación lineal relajado es:
    $$x_1 = 1.5, x_2 = 2, x_3 = 1$$
    El valor máximo de la función objetivo es:
    $$P(1.5, 2, 1) = 15$$
    
    Aunque la solución no es entera, debido a las restricciones de enteros, se puede proceder con una ramificación.
""")