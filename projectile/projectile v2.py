import tkinter as tk
import math

class ProjectileSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Projectile Motion Simulator")

        # Configuration parameters
        self.canvas_width = 800
        self.canvas_height = 400
        self.x_scale = 15  # pixels per meter
        self.y_scale = 15  # pixels per meter
        self.dt = 0.05  # time step for animation

        # Create widgets
        self.setup_controls(master)
        self.setup_canvas(master)
        self.setup_labels(master)

        # Initialize variables
        self.projectile = None
        self.animation_running = False

    def setup_controls(self, master):
        control_frame = tk.Frame(master)
        control_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Angle slider
        self.angle = tk.Scale(control_frame, from_=0, to=90, orient=tk.HORIZONTAL,
                             label="Launch Angle (degrees)", command=self.update_labels)
        self.angle.set(45)
        self.angle.pack(pady=5)

        # Velocity slider
        self.velocity = tk.Scale(control_frame, from_=1, to=30, orient=tk.HORIZONTAL,
                                label="Initial Velocity (m/s)", command=self.update_labels)
        self.velocity.set(15)
        self.velocity.pack(pady=5)

        # Start button
        self.start_btn = tk.Button(control_frame, text="Start", command=self.start_simulation)
        self.start_btn.pack(pady=10)

    def setup_canvas(self, master):
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height,
                               bg="white", bd=2, relief=tk.GROOVE)
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)

        # Draw ground line
        self.canvas.create_line(0, self.canvas_height - 5,
                               self.canvas_width, self.canvas_height - 5, fill="black")

    def setup_labels(self, master):
        label_frame = tk.Frame(master)
        label_frame.pack(side=tk.LEFT, padx=10)

        self.max_height_label = tk.Label(label_frame, text="Max Height: 0.00 m")
        self.max_height_label.pack(pady=5)

        self.max_distance_label = tk.Label(label_frame, text="Max Distance: 0.00 m")
        self.max_distance_label.pack(pady=5)

    def update_labels(self, event=None):
        if self.animation_running:
            return

        angle = self.angle.get()
        v0 = self.velocity.get()
        theta = math.radians(angle)

        # Calculate max height and distance
        max_height = (v0**2 * math.sin(theta)**2) / (2 * 9.8)
        max_distance = (v0**2 * math.sin(2*theta)) / 9.8

        self.max_height_label.config(text=f"Max Height: {max_height:.2f} m")
        self.max_distance_label.config(text=f"Max Distance: {max_distance:.2f} m")

    def start_simulation(self):
        if self.animation_running:
            return

        self.animation_running = True
        self.start_btn.config(state=tk.DISABLED)

        # Get initial parameters
        angle = self.angle.get()
        v0 = self.velocity.get()
        theta = math.radians(angle)

        # Calculate components and flight time
        vx = v0 * math.cos(theta)
        vy = v0 * math.sin(theta)
        flight_time = (2 * vy) / 9.8

        # Initial position
        x0, y0 = 0, 0
        self.t = 0

        # Create or reset projectile
        if self.projectile:
            self.canvas.delete(self.projectile)
        self.projectile = self.canvas.create_oval(
            self.scale_x(x0)-5, self.scale_y(y0)-5,
            self.scale_x(x0)+5, self.scale_y(y0)+5,
            fill="red"
        )

        # Start animation
        self.animate(flight_time, vx, vy)

    def animate(self, flight_time, vx, vy):
        if self.t > flight_time or not self.animation_running:
            self.animation_running = False
            self.start_btn.config(state=tk.NORMAL)
            return

        # Calculate position
        x = vx * self.t
        y = vy * self.t - 0.5 * 9.8 * self.t**2
        if y < 0: y = 0

        # Update projectile position
        self.canvas.coords(self.projectile,
                          self.scale_x(x)-5, self.scale_y(y)-5,
                          self.scale_x(x)+5, self.scale_y(y)+5)

        self.t += self.dt
        self.master.after(25, lambda: self.animate(flight_time, vx, vy))

    def scale_x(self, x):
        return x * self.x_scale

    def scale_y(self, y):
        return self.canvas_height - (y * self.y_scale)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectileSimulator(root)
    root.mainloop()