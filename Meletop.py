import tkinter as tk
import random
import math
import colorsys
import time

# ---------- Pengaturan ----------
WIDTH, HEIGHT = 900, 600
GRAVITY = 0.15
PARTICLES_PER_FIREWORK = 80
PARTICLE_SPEED = (2.5, 6.5)  # rentang kecepatan awal
PARTICLE_LIFE = (50, 110)    # rentang umur (frame)
FPS = 60

# ---------- Util ----------

def hsv_to_hex(h, s, v):
    """Konversi HSV (0..1) ke hex color untuk tkinter."""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return '#{0:02x}{1:02x}{2:02x}'.format(int(r*255), int(g*255), int(b*255))


# ---------- Kelas Particle dan Firework ----------
class Particle:
    def __init__(self, x, y, vx, vy, hue, life, size):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.hue = hue
        self.life = life
        self.age = 0
        self.size = size
        self.id = None  # id pada canvas

    def update(self):
        # perbarui posisi dan kecepatan (termasuk gravitasi)
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy
        self.age += 1

    @property
    def alive(self):
        return self.age < self.life

    def draw(self, canvas):
        # kurangi kecerahan berdasarkan usia
        t = self.age / self.life
        brightness = max(0, 1 - t)
        color = hsv_to_hex(self.hue, 1.0, 0.6 + 0.4 * brightness)
        r = max(1, int(self.size * (1 - 0.6 * t)))
        if self.id is None:
            self.id = canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill=color, outline='')
        else:
            canvas.coords(self.id, self.x - r, self.y - r, self.x + r, self.y + r)
            canvas.itemconfig(self.id, fill=color)

    def remove_from_canvas(self, canvas):
        if self.id is not None:
            canvas.delete(self.id)
            self.id = None


class Firework:
    def __init__(self, x, y, particle_count=PARTICLES_PER_FIREWORK):
        self.x = x
        self.y = y
        self.particles = []
        # pilih warna acak (hue)
        base_hue = random.random()
        for i in range(particle_count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(PARTICLE_SPEED[0], PARTICLE_SPEED[1])
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            life = random.randint(PARTICLE_LIFE[0], PARTICLE_LIFE[1])
            size = random.uniform(2.0, 5.5)
            # sedikit variasi warna
            hue = (base_hue + random.uniform(-0.05, 0.05)) % 1.0
            p = Particle(x, y, vx, vy, hue, life, size)
            self.particles.append(p)

    def update(self):
        for p in self.particles:
            p.update()

    def draw(self, canvas):
        for p in self.particles:
            p.draw(canvas)

    def alive(self):
        return any(p.alive for p in self.particles)

    def cleanup(self, canvas):
        for p in self.particles:
            p.remove_from_canvas(canvas)


# ---------- Aplikasi Tkinter ----------
class FireworksApp:
    def __init__(self, root):
        self.root = root
        root.title('Visual Kembang Api')
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()

        self.fireworks = []
        self.running = True

        # kontrol user
        self.canvas.bind('<Button-1>', self.on_click)
        root.bind('<space>', self.on_space)
        root.bind('q', self.on_quit)

        # teks petunjuk (di pojok)
        self.hint_text_id = self.canvas.create_text(10, 10, anchor='nw', text="Klik kiri untuk menembak. Tekan SPACE untuk acak. Tekan 'q' untuk keluar.", fill='white', font=('Helvetica', 10))

        # jalankan loop animasi
        self._loop()

    def on_click(self, event):
        self.launch_firework(event.x, event.y)

    def on_space(self, event):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 200)
        self.launch_firework(x, y)

    def on_quit(self, event):
        self.running = False
        self.root.quit()

    def launch_firework(self, x, y):
        fw = Firework(x, y)
        self.fireworks.append(fw)

    def _loop(self):
        if not self.running:
            return
        
        # update serta gambar fireworks
        for fw in list(self.fireworks):
            fw.update()
            fw.draw(self.canvas)
            # hapus fireworks yang sudah mati
            if not fw.alive():
                fw.cleanup(self.canvas)
                self.fireworks.remove(fw)

        # jadwalkan frame berikutnya
        self.root.after(int(1000 / FPS), self._loop)


if __name__ == '__main__':
    root = tk.Tk()
    app = FireworksApp(root)
    root.mainloop()
