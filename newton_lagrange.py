
import numpy as np

#########################################################################################################

def run_newton_method(n_dim, func, grad, hess, start=None, step_size_init=0.01, max_iter=1000, tolerance=1e-8, epsilon=1e-8):

    if start is None:
        start = np.zeros(n_dim)
    x = start
    f_val_prev = None
    for i in range(max_iter):

        f_val = func(x)
        grad_val = grad(x)
        hess_val = hess(x)

        step_size = step_size_init / np.sqrt(1 + i)
        hess_val_s = hess_val + epsilon * np.eye(n_dim)  # add small number term for stability
        x = x + step_size * np.linalg.solve(hess_val_s, -grad_val)
        # note: using solve instead of inv because inv is slow and less stable

        if f_val_prev is not None and np.abs(f_val - f_val_prev) < tolerance:
            break
    return x

#########################################################################################################


def run_augmented_lagrangian_method(n_dim, m_constraints, func, f_grad, f_hess, constraints_vec, constraints_jacobian,
                                    x_feasiable, inner_solver, n_iter=20,
                                    eta_start=1e-7, eta_mult=1.5, eta_max=5e-5, lamb_step_size_init=1e-4, verbose=1):
    # https://en.wikipedia.org/wiki/Augmented_Lagrangian_method#General_method


    lamb = np.zeros(m_constraints)
    x = x_feasiable
    eta = eta_start
    for i in range(n_iter):

        if verbose:
            print('-' * 20 + f'iteration {i}')
            f_val = func(x)
            grad_val = f_grad(x)
            hess_val = f_hess(x)
            constraints_val = constraints_vec(x)
            print(f'f_val={f_val}, grad_val={grad_val}, hess_val={hess_val}, constraints_val={constraints_val}')
            print(f'x={x}')
            print(f'lamb={lamb}')
            print(f'eta={eta}')

        # The augmented lagrangian objective function:
        epsilon = 1e-6
        phi = lambda _x: func(_x) \
                         + eta * np.sum(np.log(np.maximum(0, -constraints_vec(_x)) + epsilon)) \
                         + np.sum(lamb * constraints_vec(_x))

        phi_val = phi(x)
        print(f'phi_val={phi_val}')

        # gradient w.r.t. x is the gradient of the augmented lagrangian
        phi_grad = lambda _x: f_grad(_x) \
                             + eta * (1 / (np.maximum(0, -constraints_vec(_x)) + epsilon)) @ constraints_jacobian(_x) \
                             + lamb @ constraints_jacobian(_x)

        phi_hess = lambda _x: f_hess(_x)

        # Run inner optimization (Newton method), starting from previous
        x = inner_solver(n_dim, phi, phi_grad, phi_hess, start=x)

        # gradient step w.r.t. lamb
        lamb_step_size = lamb_step_size_init / np.sqrt(i + 1)
        lamb = lamb + lamb_step_size * np.maximum(0, constraints_vec(x))

        # update eta
        eta = min(eta * eta_mult, eta_max)

#########################################################################################################

n_dim = 2
quadratic_func = lambda x: 2 * (x[0] - 5) ** 2 + (x[1] - 1) ** 2
quadratic_func_grad = lambda x: np.array([4 * (x[0] - 5), 2 * (x[1] - 1)])
quadratic_func_hess = lambda x: np.array([[4, 0], [0, 2]])

quadratic_func_constr = lambda x: np.array([+x[1] - 1 + 0.5 * x[0],
                                            +x[0] - x[1],
                                            -x[0] - x[1]])
quadratic_func_constr_jacobian = lambda x: np.array([[+0.5, +1],
                                                    [+1, -1],
                                                    [-1, -1]])
m_constraints = 3
x_feasiable = np.array([0, 0])
#
# quadratic_func_constr = lambda x: np.array([x[1] - 1 + 0.5 * x[0],
#                                             x[1] - 1 + 0.5 * x[0]
#                                           ])
# quadratic_func_constr_jacobian = lambda x: np.array([[0.5, 1],
#                                                      [0.5, 1]
#                                                     ])
# m_constraints = 2

run_augmented_lagrangian_method(n_dim, m_constraints, quadratic_func, quadratic_func_grad, quadratic_func_hess,
                                quadratic_func_constr, quadratic_func_constr_jacobian, x_feasiable,
                                run_newton_method)

# x = run_newton_method(n_dim, quadratic_func, quadratic_func_grad, quadratic_func_hess)
# print('x = ', x)
# print('f(x) = ', quadratic_func(x))