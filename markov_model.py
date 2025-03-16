#follow this video: https://www.youtube.com/watch?v=i3AkTO9HLXo&list=PLM8wYQRetTxBkdvBtz-gw8b9lcVkdXQKV
import numpy as np
import random
import matplotlib.pyplot as plt

transition_matrix = [[0.2,0.6,0.2],
                     [0.3,0,0.7],
                     [0.5,0,0.5]]

accumulative_matrix = [[sum(transition_matrix[i][:j+1]) for j in range (len(transition_matrix[0]))] for i in range(len(transition_matrix))]
print(accumulative_matrix)

def next_state(current_state):
    l = random.random()
    if l<accumulative_matrix[current_state][0]:return 0
    for i in range(1,len(accumulative_matrix[0])):
        if l>=accumulative_matrix[current_state][i-1] and l<accumulative_matrix[current_state][i]:
            return i
    raise ValueError(f"Random value {l} did not fall within any valid range for state {current_state}")
# # Hàm next_state dựa trên accumulative_matrix # nhanh hơn, hiệu quả hơn
# def next_state(current_state):
#     probabilities = accumulative_matrix[current_state]
#     return np.random.choice(n_states, p=probabilities)

def stat_(n_iter = 100,current_state = 0):
    cnt = [0 for i in range(len(accumulative_matrix))]
    cnt[current_state] += 1
    for i in range(n_iter):
        current_state = next_state(current_state=current_state)
        cnt[current_state] += 1
    cnt = [u/n_iter for u in cnt]
    return cnt

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
def stat_with_graph(n_iter=1000, current_state=0):
    # Số trạng thái cố định từ 0 đến 10 (11 trạng thái)
    n_states = 3
    
    # Tạo accumulative_matrix mẫu nếu chưa có
    # Đây chỉ là ví dụ, bạn có thể thay bằng matrix thực của bạn
    accumulative_matrix = np.random.rand(n_states, n_states)
    accumulative_matrix /= accumulative_matrix.sum(axis=1)[:, np.newaxis]

    # Đảm bảo current_state trong phạm vi 0-10
    current_state = max(0, min(current_state, n_states))
    
    # Khởi tạo danh sách đếm
    cnt = [[0] for _ in range(n_states)]
    cnt[current_state][0] = 1

    

    # Thiết lập figure
    fig, ax = plt.subplots()
    lines = [ax.plot([], [])[0] for _ in range(n_states)]
    ax.set_xlim(0, n_iter)
    ax.set_ylim(0, 1)  # Vì giá trị được chuẩn hóa từ 0-1 sau khi chia

    # Khởi tạo dữ liệu cho animation
    data = [[] for _ in range(n_states)]
    for i in range(n_states):
        data[i].append(cnt[i][0])

    # Hàm khởi tạo cho animation
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    # Hàm cập nhật cho mỗi frame
    def update(frame):
        nonlocal current_state
        if frame > 0:
            current_state = next_state(current_state)
            for i in range(n_states):
                data[i].append(data[i][-1])
            data[current_state][-1] += 1

        x = range(len(data[0]))
        for i in range(n_states):
            y = [v/(j+1) for j, v in enumerate(data[i])]
            lines[i].set_data(x, y)
        
        return lines

    # Tạo animation
    anim = FuncAnimation(fig, update, frames=n_iter,
                        init_func=init, blit=True, interval=100)
    
    plt.title(f'Real-time State Statistics (0-{n_states-1})')
    plt.xlabel('Time')
    plt.ylabel('Normalized Frequency')
    plt.legend([f'State {i}' for i in range(n_states)], 
              loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    plt.show()

def mat_cal_(n_iter = 100, current_state = 0):
    prob = [0 for i in range(len(transition_matrix))]
    prob[current_state] = 1
    nmat = np.array(transition_matrix)
    prob = np.array(prob)
    # print(prob@nmat)
    # exit()
    for i in range(n_iter):
        prob = prob@nmat
    return prob.tolist()

print(mat_cal_())
print(stat_(100000))
stat_with_graph()