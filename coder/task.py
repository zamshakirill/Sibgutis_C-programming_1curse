import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# 1. Точка остановки: 2^(t/20) = 1000 => t = 20 * log2(1000)
t_stop = 20 * np.log2(1000)

# 2. Данные
t = np.linspace(0, t_stop, 400)
N = 2 ** (t / 20)

# 3–4. Две панели: обычная шкала слева, логарифмическая справа
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.set_title("Обычная шкала: «незаметно → БУМ!»")
ax1.set_xlabel("Минуты")
ax1.set_ylabel("Бактерий")
ax1.set_xlim(0, t_stop * 1.03)
ax1.set_ylim(0, 1100)
ax1.grid(True, alpha=0.3)

ax2.set_title("Лог-шкала: ровная прямая")
ax2.set_xlabel("Минуты")
ax2.set_ylabel("Бактерий (log)")
ax2.set_yscale("log")
ax2.set_xlim(0, t_stop * 1.03)
ax2.set_ylim(1, 1500)
ax2.grid(True, which="both", alpha=0.3)

# 5. Линия порога 1000 и бледная «тень» всей кривой на обеих панелях
for ax in (ax1, ax2):
  ax.axhline(1000, ls="--", color="red", alpha=0.8, label="Порог 1000")
  ax.plot(t, N, color="green", alpha=0.2, lw=2)

# Анимируемые элементы (активная кривая и текущая точка)
(line1,) = ax1.plot([], [], color="green", lw=2.5)
(pt1,) = ax1.plot([], [], marker="o", color="green", markersize=7)

(line2,) = ax2.plot([], [], color="green", lw=2.5)
(pt2,) = ax2.plot([], [], marker="o", color="green", markersize=7)

info_text = ax1.text(
    0.03,
    0.95,
    "",
    transform=ax1.transAxes,
    va="top",
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
)

last_frame = len(t) - 1


# 6–7. Функция обновления кадров
def update(frame):
  n = frame + 1
  t_cur = t[:n]
  N_cur = N[:n]

  line1.set_data(t_cur, N_cur)
  line2.set_data(t_cur, N_cur)

  pt1.set_data([t[frame]], [N[frame]])
  pt2.set_data([t[frame]], [N[frame]])

  info_text.set_text(f"t = {t[frame]:.1f} мин\nN = {N[frame]:.0f}")

  if frame == last_frame:
    pt1.set_color("red")
    pt1.set_markersize(11)
    pt2.set_color("red")
    pt2.set_markersize(11)

  return line1, pt1, line2, pt2, info_text


# 8. Запуск анимации без повтора
ani = animation.FuncAnimation(
    fig, update, frames=len(t), interval=20, blit=False, repeat=False
)

plt.tight_layout()
plt.show()