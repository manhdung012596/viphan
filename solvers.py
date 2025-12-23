import numpy as np

def euler_method(f, x0, y0, h, x_end):
    """
    Giải phương trình vi phân y' = f(x, y) bằng phương pháp Euler.
    
    Args:
        f: Hàm vế phải f(x, y)
        x0, y0: Điều kiện ban đầu
        h: Bước nhảy
        x_end: Giá trị x tại điểm cuối cần tính
        
    Returns:
        tuple: (x_values, y_values) - danh sách các điểm x và giá trị y tương ứng
    """
    x_values = np.arange(x0, x_end + h/2, h) # +h/2 để bao gồm điểm cuối do floating point
    y_values = [y0]
    
    y_curr = y0
    # Lặp qua các giá trị x, trừ giá trị cuối cùng vì nó là kết quả của bước nhảy cuối
    for i in range(len(x_values) - 1):
        x_curr = x_values[i]
        
        # Công thức Euler: y_{n+1} = y_n + h * f(x_n, y_n)
        y_next = y_curr + h * f(x_curr, y_curr)
        
        y_values.append(y_next)
        y_curr = y_next
        
    return x_values, np.array(y_values)

def improved_euler_method(f, x0, y0, h, x_end):
    """
    Giải phương trình vi phân y' = f(x, y) bằng phương pháp Euler cải tiến (Heun).
    """
    x_values = np.arange(x0, x_end + h/2, h)
    y_values = [y0]
    
    y_curr = y0
    for i in range(len(x_values) - 1):
        x_curr = x_values[i]
        
        # Dự đoán (Predictor): y_mid = y_n + h * f(x_n, y_n)
        k1 = f(x_curr, y_curr)
        y_predict = y_curr + h * k1
        
        # Hiệu chỉnh (Corrector): y_{n+1} = y_n + (h/2) * [f(x_n, y_n) + f(x_{n+1}, y_predict)]
        k2 = f(x_curr + h, y_predict)
        y_next = y_curr + (h / 2) * (k1 + k2)
        
        y_values.append(y_next)
        y_curr = y_next
        
    return x_values, np.array(y_values)

def rk4_method(f, x0, y0, h, x_end):
    """
    Giải phương trình vi phân y' = f(x, y) bằng phương pháp Runge-Kutta bậc 4.
    """
    x_values = np.arange(x0, x_end + h/2, h)
    y_values = [y0]
    
    y_curr = y0
    for i in range(len(x_values) - 1):
        x_curr = x_values[i]
        
        k1 = f(x_curr, y_curr)
        k2 = f(x_curr + 0.5 * h, y_curr + 0.5 * h * k1)
        k3 = f(x_curr + 0.5 * h, y_curr + 0.5 * h * k2)
        k4 = f(x_curr + h, y_curr + h * k3)
        
        # Công thức RK4
        y_next = y_curr + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        
        y_values.append(y_next)
        y_curr = y_next
        
    return x_values, np.array(y_values)
