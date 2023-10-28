# import sys
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDoubleSpinBox
# from PyQt5.QtCore import QTimer
# from PyQt5.QtGui import QPainterPath
# from PyQt5.QtCore import QPointF
# import pyqtgraph as pg
# from pyqtgraph import ArrowItem

# class PhasorApp(QWidget):
#     def __init__(self):
#         super().__init__()

#         start_time = 0  # Set this to the desired start time
#         end_time = 0  # Set this to the desired end time
#         num_samples = 0  # Set this to the desired number of samples

#         # Timer for animation
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.animate)
#         self.time_data = np.linspace(start_time, end_time, num_samples)
#         self.dt = (end_time - start_time) / (num_samples - 1)  # Add this line
#         self.voltage_data = np.zeros_like(self.time_data)
#         self.current_data = np.zeros_like(self.time_data)

#         # UI Initialization
#         self.init_ui()

#     def init_ui(self):
#         # Layout setup
#         layout = QVBoxLayout()

#         # Voltage Input
#         self.voltage_label = QLabel('Voltage (V):')
#         self.voltage_input = QDoubleSpinBox()
#         self.voltage_input.setRange(-1000, 1000)
#         self.voltage_input.setDecimals(3)
#         self.voltage_input.setValue(1.0)
#         layout.addWidget(self.voltage_label)
#         layout.addWidget(self.voltage_input)

#         # Current Input
#         self.current_label = QLabel('Current (A):')
#         self.current_input = QDoubleSpinBox()
#         self.current_input.setRange(-1000, 1000)
#         self.current_input.setDecimals(3)
#         self.current_input.setValue(1.0)
#         layout.addWidget(self.current_label)
#         layout.addWidget(self.current_input)

#         # Frequency Input
#         self.frequency_label = QLabel('Frequency (0.1 < f < 1):')
#         self.frequency_input = QDoubleSpinBox()
#         self.frequency_input.setRange(0.1, 1.0)
#         self.frequency_input.setDecimals(3)
#         self.frequency_input.setValue(0.5)
#         layout.addWidget(self.frequency_label)
#         layout.addWidget(self.frequency_input)

#         # Voltage Phase Input
#         self.voltage_phase_label = QLabel('Voltage Phase (deg):')
#         self.voltage_phase_input = QDoubleSpinBox()
#         self.voltage_phase_input.setRange(0, 360)
#         self.voltage_phase_input.setDecimals(3)
#         layout.addWidget(self.voltage_phase_label)
#         layout.addWidget(self.voltage_phase_input)

#         # Current Phase Input
#         self.current_phase_label = QLabel('Current Phase (deg):')
#         self.current_phase_input = QDoubleSpinBox()
#         self.current_phase_input.setRange(0, 360)
#         self.current_phase_input.setDecimals(3)
#         layout.addWidget(self.current_phase_label)
#         layout.addWidget(self.current_phase_input)


#         # Submit Button
#         self.submit_button = QPushButton('Start Animation')
#         self.submit_button.clicked.connect(self.start_animation)
#         layout.addWidget(self.submit_button)

#         # Phasor & Time Domain Representation Plot
#         self.win = pg.GraphicsLayoutWidget()
#         layout.addWidget(self.win)

#         self.phasor_view = self.win.addPlot(row=1, col=0, title="Phasor Representation")
#         self.time_view = self.win.addPlot(row=1, col=1, title="Time Domain Representation")
#         self.time_view.setRange(xRange=(0, 10))

#         self.setLayout(layout)

#     def start_animation(self):
#         # Get initial values
#         self.voltage_amplitude = self.voltage_input.value()
#         self.current_amplitude = self.current_input.value()
#         self.frequency = self.frequency_input.value()
#         self.voltage_phase = np.deg2rad(self.voltage_phase_input.value())
#         self.current_phase = np.deg2rad(self.current_phase_input.value())

#         # Determine the scale
#         self.max_magnitude = max(abs(self.voltage_amplitude), abs(self.current_amplitude))
#         self.phasor_view.setRange(xRange=(-self.max_magnitude, self.max_magnitude), yRange=(-self.max_magnitude, self.max_magnitude))
#         self.time_view.setRange(yRange=(-self.max_magnitude, self.max_magnitude))

#         # For time and data storage
#         self.t = 0
#         self.time_data = []
#         self.voltage_data = []
#         self.current_data = []

#         # Start the timer to refresh plots periodically (e.g., every 50 milliseconds)
#         self.timer.start(50)

#     def animate(self):
#         # Calculate instantaneous values using the sine and cosine components
#         voltage_x = self.voltage_amplitude * np.cos(2 * np.pi * self.frequency * self.t + self.voltage_phase)
#         voltage_y = self.voltage_amplitude * np.sin(2 * np.pi * self.frequency * self.t + self.voltage_phase)
#         current_x = self.current_amplitude * np.cos(2 * np.pi * self.frequency * self.t + self.current_phase)
#         current_y = self.current_amplitude * np.sin(2 * np.pi * self.frequency * self.t + self.current_phase)

#         # Update the phasor view
#         self.phasor_view.clear()
#         self.phasor_view.plot([0, voltage_x], [0, voltage_y], pen='r')
#         self.phasor_view.plot([0, current_x], [0, current_y], pen='b')

#         # Update the time domain view
#         self.time_data.append(self.t)
#         self.voltage_data.append(voltage_y) # using y-component which is the sine value
#         self.current_data.append(current_y)
#         self.time_view.plot(self.time_data, self.voltage_data, pen='r')
#         self.time_view.plot(self.time_data, self.current_data, pen='b')

#         # Increment time
#         self.t += 0.05

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = PhasorApp()
#     window.show()
#     sys.exit(app.exec_())

import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QPointF
import pyqtgraph as pg
from pyqtgraph import ArrowItem

class PhasorApp(QWidget):
    def __init__(self):
        super().__init__()

        start_time = 0
        end_time = 10  # Example: 10 seconds of data
        num_samples = 1000  # 200 samples over 10 seconds 

        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.time_data = np.linspace(start_time, end_time, num_samples)
        self.dt = (end_time - start_time) / (num_samples - 1)
        self.voltage_data = np.zeros_like(self.time_data)
        self.current_data = np.zeros_like(self.time_data)

        # UI Initialization
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Parameters layout using QGridLayout for better alignment
        param_layout = QGridLayout()

        param_layout.addWidget(QLabel('Voltage (V):'), 0, 0)
        self.voltage_input = self.create_double_spinbox()
        param_layout.addWidget(self.voltage_input, 0, 1)

        param_layout.addWidget(QLabel('Current (A):'), 1, 0)
        self.current_input = self.create_double_spinbox()
        param_layout.addWidget(self.current_input, 1, 1)

        param_layout.addWidget(QLabel('Frequency (0.1 < f < 1):'), 2, 0)
        self.frequency_input = self.create_double_spinbox(0.1, 1.0, 0.5)
        param_layout.addWidget(self.frequency_input, 2, 1)

        param_layout.addWidget(QLabel('Voltage Phase (deg):'), 3, 0)
        self.voltage_phase_input = self.create_double_spinbox(0, 360)
        param_layout.addWidget(self.voltage_phase_input, 3, 1)

        param_layout.addWidget(QLabel('Current Phase (deg):'), 4, 0)
        self.current_phase_input = self.create_double_spinbox(0, 360)
        param_layout.addWidget(self.current_phase_input, 4, 1)

        param_group = QGroupBox("Parameters")
        param_group.setLayout(param_layout)
        main_layout.addWidget(param_group)

        # Button controls
        btn_layout = QHBoxLayout()
        self.go_button = QPushButton('Go!')
        self.go_button.clicked.connect(self.start_animation)
        btn_layout.addWidget(self.go_button)

        self.pause_button = QPushButton('Pause')
        self.pause_button.setCheckable(True)
        self.pause_button.clicked.connect(self.pause_animation)
        btn_layout.addWidget(self.pause_button)

        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self.close)
        btn_layout.addWidget(self.exit_button)

        btn_group = QGroupBox("Controls")
        btn_group.setLayout(btn_layout)
        main_layout.addWidget(btn_group)

        # Phasor & Time Domain Representation Plot
        self.win = pg.GraphicsLayoutWidget()
        main_layout.addWidget(self.win)

        self.phasor_view = self.win.addPlot(row=1, col=0, title="Phasor Representation")
        self.time_view = self.win.addPlot(row=1, col=1, title="Time Domain Representation")
        self.time_view.setRange(xRange=(0, 10))

        self.setLayout(main_layout)

    def create_double_spinbox(self, min_val=-1000, max_val=1000, default_val=1.0):
        spinbox = QDoubleSpinBox()
        spinbox.setRange(min_val, max_val)
        spinbox.setDecimals(3)
        spinbox.setValue(default_val)
        return spinbox

    def start_animation(self):
        # Get initial values
        self.voltage_amplitude = self.voltage_input.value()
        self.current_amplitude = self.current_input.value()
        self.frequency = self.frequency_input.value()
        self.voltage_phase = np.deg2rad(self.voltage_phase_input.value())
        self.current_phase = np.deg2rad(self.current_phase_input.value())

        # Determine the scale
        self.max_magnitude = max(abs(self.voltage_amplitude), abs(self.current_amplitude))
        self.phasor_view.setRange(xRange=(-self.max_magnitude, self.max_magnitude), yRange=(-self.max_magnitude, self.max_magnitude))
        self.time_view.setRange(yRange=(-self.max_magnitude, self.max_magnitude))

        # For time and data storage
        self.t = 0
        self.time_data = []
        self.voltage_data = []
        self.current_data = []

        # Start the timer to refresh plots periodically (e.g., every 50 milliseconds)
        self.timer.start(50)

    def pause_animation(self):
        if self.pause_button.isChecked():
            self.timer.stop()
            self.pause_button.setText('Resume')
        else:
            self.timer.start(50)
            self.pause_button.setText('Pause')

    def animate(self):
        # Calculate instantaneous values using the sine and cosine components
        voltage_x = self.voltage_amplitude * np.cos(2 * np.pi * self.frequency * self.t + self.voltage_phase)
        voltage_y = self.voltage_amplitude * np.sin(2 * np.pi * self.frequency * self.t + self.voltage_phase)
        current_x = self.current_amplitude * np.cos(2 * np.pi * self.frequency * self.t + self.current_phase)
        current_y = self.current_amplitude * np.sin(2 * np.pi * self.frequency * self.t + self.current_phase)

        # Update the phasor view
        self.phasor_view.clear()
        self.phasor_view.plot([0, voltage_x], [0, voltage_y], pen='r')
        self.phasor_view.plot([0, current_x], [0, current_y], pen='b')

        # Update the time domain view
        self.time_data.append(self.t)
        self.voltage_data.append(voltage_y) # using y-component which is the sine value
        self.current_data.append(current_y)
        self.time_view.plot(self.time_data, self.voltage_data, pen='r')
        self.time_view.plot(self.time_data, self.current_data, pen='b')

        # Increment time
        self.t += 0.05

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhasorApp()
    window.show()
    sys.exit(app.exec_())

