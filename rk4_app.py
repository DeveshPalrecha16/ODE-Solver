import streamlit as st
import matplotlib.pyplot as plt

# Define the function f(t, y) = dy/dt
def f(t, y):
    return t + y  # Example ODE

# RK4 method for a single first-order ODE
def rk4_method(f, t0, y0, h, t_end):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    steps = int((t_end - t0) / h)

    for step in range(steps):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)

        y = y + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# --- Streamlit App ---

st.title("Runge-Kutta (RK4) ODE Solver")
st.markdown("Solves ODE of the form: `dy/dt = t + y`")

# Input section
st.subheader("Enter Parameters")
t0 = st.number_input("Initial time (t₀)", value=0.0)
y0 = st.number_input("Initial value (y₀)", value=1.0)
t_end = st.number_input("Final time (t)", value=2.0)
h = st.number_input("Step size (h)", value=0.1)

# Solve button
if st.button("Solve ODE"):
    t_vals, y_vals = rk4_method(f, t0, y0, h, t_end)
    
    st.success("Solution computed successfully!")

    # Show result table
    st.subheader("Results Table")
    st.dataframe({"t": t_vals, "y(t)": y_vals})

    # Plot results
    st.subheader("Solution Plot")
    fig, ax = plt.subplots()
    ax.plot(t_vals, y_vals, marker='o', label="y(t)")
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.set_title("Solution of dy/dt = t + y using RK4")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)