import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from solvers import euler_method, improved_euler_method, rk4_method

# 1. Định nghĩa bài toán
# Bài toán: y' = y - t^2 + 1, 0 <= t <= 2, y(0) = 0.5
# Nghiệm chính xác: y(t) = (t+1)^2 - 0.5 * exp(t)

def f(t, y):
    return y - t**2 + 1

def exact_solution(t):
    return (t + 1)**2 - 0.5 * np.exp(t)

def calculate_error(y_approx, y_exact):
    return np.abs(y_approx - y_exact)

def main():
    # Tham số đầu vào
    x0 = 0
    y0 = 0.5
    x_end = 2.0
    h = 0.2  # Bước nhảy
    
    print(f"GIAI PHUONG TRINH VI PHAN: y' = y - t^2 + 1")
    print(f"Dieu kien dau: y({x0}) = {y0}")
    print(f"Khoang t: [{x0}, {x_end}]")
    print(f"Buoc nhay h = {h}")
    print("-" * 60)

    # 2. Chạy các thuật toán
    t_euler, y_euler = euler_method(f, x0, y0, h, x_end)
    _, y_imp_euler = improved_euler_method(f, x0, y0, h, x_end)
    _, y_rk4 = rk4_method(f, x0, y0, h, x_end)
    
    # 3. Tính toán giá trị chính xác và sai số
    y_exact_vals = exact_solution(t_euler)
    
    err_euler = calculate_error(y_euler, y_exact_vals)
    err_imp = calculate_error(y_imp_euler, y_exact_vals)
    err_rk4 = calculate_error(y_rk4, y_exact_vals)
    
    # 4. Hiển thị bảng kết quả
    data = {
        't': t_euler,
        'Exact': y_exact_vals,
        'Euler': y_euler,
        'Err Euler': err_euler,
        'Imp Euler': y_imp_euler,
        'Err Imp': err_imp,
        'RK4': y_rk4,
        'Err RK4': err_rk4
    }
    
    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    print("\nBANG KET QUA SO SANH:")
    print(df)
    
    # Đánh giá sai số toàn cục (Global Error) - lấy sai số lớn nhất
    print("\nDANH GIA SAI SO TOAN CUC (MAX ERROR):")
    print(f"Euler Method:          {np.max(err_euler):.6f}")
    print(f"Improved Euler Method: {np.max(err_imp):.6f}")
    print(f"Runge-Kutta 4 Method:  {np.max(err_rk4):.6f}")
    
    # 5. Vẽ đồ thị
    plt.figure(figsize=(10, 6))
    
    # Vẽ đường nghiệm chính xác (dùng nhiều điểm hơn cho mượt)
    t_smooth = np.linspace(x0, x_end, 100)
    y_smooth = exact_solution(t_smooth)
    plt.plot(t_smooth, y_smooth, 'k-', label='Exact Solution', linewidth=1.5)
    
    # Vẽ các điểm xấp xỉ
    plt.plot(t_euler, y_euler, 'ro--', label=f'Euler (h={h})', markersize=4)
    plt.plot(t_euler, y_imp_euler, 'bs--', label=f'Improved Euler (h={h})', markersize=4)
    plt.plot(t_euler, y_rk4, 'g^--', label=f'RK4 (h={h})', markersize=4)
    
    plt.title(f"So sanh cac phuong phap giai phuong trinh vi phan (h={h})")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    
    plot_filename = "comparison_plot.png"
    plt.savefig(plot_filename)
    print(f"\nDa luu bieu do vao file: {plot_filename}")
    plt.show()

if __name__ == "__main__":
    main()
