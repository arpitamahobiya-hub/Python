Fitness Data Tracker – PS NO. 74
B.Tech Computer Science and Engineering
Institution: Rungta International Skills University
Language: Python 3 
Repository contents
one.py  - complete console-based application.
readme.md – which contains the content about repository.
summary.md — project overview, sample test evidence, development difficulties and screenshots that is captured sample console outputs and the generated daily-steps chart.

Features
Store daily steps and calories burned in two Python lists.
Check progress against the daily target of 10,000 steps.
Show average steps, total calories, best day, and number of goal-achievement days.
Calculate BMI and show its category.
Plot daily steps with a Matplotlib bar chart and a 10,000-step reference line.
Validate non-negative whole-number entries and positive BMI inputs.
Setup and run
Install Python 3, then install the dependency:
python -m pip install - matplotlib
python one.py
Choose menu options 1–5 in the console. Data is kept in memory while the program is running; it is not permanently saved after exit.
Sample data used for verification
Day 1: 8,000 steps, 320 calories
Day 2: 12,000 steps, 480 calories
Day 3: 10,000 steps, 400 calories
Expected summary:
Average steps: 10000.00
Total calories: 1200
Best day: Day 2 (12000 steps)
Goal days: 2/3
BMI for 70 kg and 1.75 m: 22.86 — Normal
Notes
The project follows the supplied problem statement. The sample output images in screenshots/ are illustrative test-run evidence generated from the same program logic. To reproduce them, run the program and enter the sample values above.
