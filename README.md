**📸 Face Recognition Attendance System**

**📝 Overview**

The Face Recognition Attendance System is a Python-based application that automates attendance marking using a webcam. It detects faces in real-time and logs date and time in a CSV file.

This project demonstrates computer vision integration with practical applications.

**⚡ Features**

🟢 Real-time face detection using Haar Cascade Classifier.

🗂 Automatic attendance logging in attendance.csv.

🖥 Lightweight and easy to set up.

👁 Visual feedback: detected faces highlighted with rectangles and prompts.

🌐 Cross-platform: works on Windows, macOS, and Linux with Python 3.x.

**🛠 Folder Structure**
Face-Recognition-Attendance-System/
│
├─ hello.py                # Main Python script
├─ attendance.csv          # CSV file storing attendance logs
├─ README.md               # Project documentation
└─ .gitignore              # Files/folders to ignore (desktop.ini, __pycache__, etc.)


Tip: Only code and CSV logs are tracked. System files like desktop.ini are ignored.

**🚀 How It Works**

Launch the application (hello.py) and allow webcam access.

The system scans for faces continuously.

Detected faces are highlighted with rectangles and a prompt:
“Press O to mark attendance”.

Press O to log date & time in attendance.csv.

Press Q to exit the application.

⚠️ Current version does not distinguish between multiple users. For classrooms or offices, integrate a face recognition model.

**⚙️ Installation**
1️⃣ Clone the repository
git clone https://github.com/SajalPorey/face-recognition-attendance-system.git
cd face-recognition-attendance-system

2️⃣ Install dependencies
pip install opencv-python

3️⃣ Run the application
python hello.py

**📊 Usage**

Ensure proper lighting for accurate face detection.

Use a clear, unobstructed view of faces in front of the webcam.

Press O to mark attendance; Q to quit.

Attendance logs are stored in attendance.csv:

Date	Time
2025-12-29	14:05:12
🖼 Screenshots

(Optional: include screenshots of the live feed and CSV output here for visual clarity.)

**🔮 Future Improvements**

Integrate face recognition to differentiate multiple users.

Add a GUI dashboard to visualize attendance.

Enable multi-user support for classrooms or offices.

Include notifications or export options.

**📜 License**

This project is licensed under the MIT License  see the LICENSE file for details.
