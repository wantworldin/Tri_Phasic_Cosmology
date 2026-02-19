import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성 함수
def generate_vector_field(kind='outward'):
    Y, X = np.mgrid[-3:3:20j, -3:3:20j]
    U, V = np.zeros_like(X), np.zeros_like(Y)
    
    for i in range(len(X)):
        for j in range(len(Y)):
            x, y = X[i, j], Y[i, j]
            r = np.sqrt(x**2 + y**2)
            if r == 0: continue
            
            if kind == 'outward':
                # S극 단극자 (발산)
                U[i, j] = x / r**2
                V[i, j] = y / r**2
            elif kind == 'inward':
                # N극 단극자 (수렴)
                U[i, j] = -x / r**2
                V[i, j] = -y / r**2
            elif kind == 'dual':
                # 쌍극자 (순환 - 자웅동체)
                # Dipole formula roughly
                # m = [0, 1] (pointing up)
                # B = (3(m.r)r - m*r^2) / r^5
                dot = y # m.r where m=(0,1)
                U[i, j] = (3 * dot * x) / r**5
                V[i, j] = (3 * dot * y - r**2) / r**5

    return X, Y, U, V

# 그림 그리기
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.patch.set_facecolor('#000000') # 배경 블랙

titles = [
    "1. Outward Force (Phi_out)\n[S-Monopole: Divergence]", 
    "2. Inward Force (Sigma_in)\n[N-Monopole: Convergence]", 
    "3. Dual Force (Psi_dual)\n[Self-Circulating Loop]"
]
kinds = ['outward', 'inward', 'dual']
colors = ['#ffcc00', '#00ffff', '#00ff00'] # Yellow(Out), Cyan(In), Green(Dual)

for ax, kind, title, col in zip(axes, kinds, titles, colors):
    X, Y, U, V = generate_vector_field(kind)
    
    ax.set_facecolor('#000000')
    ax.set_aspect('equal')
    
    # 스트림플롯 (유선) 그리기 - 파동의 흐름 표현
    st = ax.streamplot(X, Y, U, V, color=col, linewidth=1.5, arrowsize=1.5, density=1.2)
    
    # 중심점 표현
    if kind == 'outward':
        ax.add_artist(plt.Circle((0,0), 0.2, color=col))
    elif kind == 'inward':
        ax.add_artist(plt.Circle((0,0), 0.2, color=col))
    elif kind == 'dual':
        # 도넛 모양 중심 (순환의 통로)
        ax.add_artist(plt.Circle((0,0), 0.3, color='white', fill=False, linewidth=2))

    ax.set_title(title, color='white', fontsize=14, pad=20)
    ax.axis('off')

plt.tight_layout()
plt.show()