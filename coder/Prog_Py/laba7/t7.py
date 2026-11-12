# import numpy as np
# import matplotlib.pyplot as plt

# days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'] * 2
# day_week = np.array([5.1, 6.3, 4.8, 7.2, 9.5, 8.1, 6.7, 5.9, 7.4, 8.8, 10.2, 9.1, 7.5, 6.2])
# night_week = np.array([-1.2, 0.3, -2.1, 1.5, 3.8, 2.4, 0.9, -0.4, 1.8, 3.2, 4.6, 2.9, 1.1, -0.3])

# x = np.arange(len(days))
# mean_night = night_week.mean()
# mean_day = day_week.mean()
# fig1, ax = plt.subplots(figsize=(11, 4.5))

# ax.plot(x, day_week, night_week, marker='o', marker='s', color='orange', color='blue', linewidth=2, markersize=6, label='Температура')
# ax.axline()

# plt.show()
import numpy as np
import matplotlib.pyplot as plt

days    = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'] * 2
revenue = np.array([12.5, 11.8, 13.2, 14.1, 18.7, 22.4, 19.8,
                    13.1, 12.4, 14.5, 15.2, 19.8, 23.6, 20.5])
x        = np.arange(len(days))
mean_rev = revenue.mean()

fig, ax = plt.subplots(figsize=(11, 4.5))

ax.plot(x, revenue, marker='o', color='steelblue',
        linewidth=2, markersize=7, label='выручка')

ax.axhline(mean_rev, color='gray', linestyle='--', linewidth=1,
           label=f'среднее = {mean_rev:.1f}')

ax.set_title('Выручка кофейни за две недели')
ax.set_xlabel('День недели')
ax.set_ylabel('Выручка, тыс. руб.')
ax.set_xlim(-0.5, 13.5)
ax.set_ylim(5, 30)
ax.set_xticks(x)
ax.set_xticklabels(days, rotation=45)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left')

fig.tight_layout()
fig.savefig('coffee.png', dpi=150)
plt.show()