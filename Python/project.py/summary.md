FITNESS DATA TRACKER
Project No. 74 | Python 3 | B.Tech Computer Science and Engineering
Rungta International Skills University
1. Summary of the Project
Fitness Data Tracker is a menu-driven Python application that records daily steps and calories burned. It checks whether the daily target of 10,000 steps has been achieved, calculates a weekly summary, calculates Body Mass Index (BMI), and displays daily steps in a Matplotlib bar chart.
2. Main Features and Python Concepts
•	Add daily records containing steps and calories burned.
•	Check progress against the 10,000-step daily goal and show the completion percentage.
•	Calculate average steps, total calories, best day, and number of goal-achievement days.
•	Calculate BMI using weight in kilograms and height in metres, and show its category.
•	Display a bar chart of daily steps with a 10,000-step reference line.
•	Validate entries and reject negative steps/calories or non-positive BMI measurements.
Concepts used: Python lists, functions, loops, conditional statements, input validation, arithmetic calculations, and Matplotlib data visualization.
3. Test Cases and Results
Test case	Input	Expected result
Normal input	8,000 steps; 320 calories	Saved; goal No; 80.00%
Boundary input	10,000 steps; 400 calories	Saved; goal Yes; 100.00%
Invalid input	-500 steps; 200 calories	Rejected; record not saved
Weekly summary	8,000; 12,000; 10,000 steps	Average 10,000.00; total calories 1,200; best Day 2; goal days 2/3
BMI	70 kg; 1.75 m	BMI 22.86; Normal
4. Screenshots of Test Cases
These are illustrative screenshots prepared from the sample inputs and expected outputs in the assignment brief. If your instructor requires proof of your own live run, execute the Python program and capture screenshots from your computer.
 
Figure 1: Sample test-case output.
 
Figure 2: Invalid-input validation.
 
Figure 3: Daily steps bar chart and goal line.
5. Difficulties Faced During Development
•	Input validation: Console input is received as text, so it must be converted carefully. Negative or non-numeric values must be rejected without saving an incorrect record.
•	Keeping records aligned: Steps and calories are stored in separate lists. Values at the same index must belong to the same day.
•	Handling empty records: Average and best-day calculations must handle the case where no records have been entered.
•	BMI calculation: Height must be entered in metres, and weight and height must both be positive.
•	Creating the chart: The chart needs correct day labels, axis labels, a title, and a reference line at 10,000 steps.
•	Testing: Normal, boundary, invalid-input, summary, BMI, and chart features need separate checks.
6. Conclusion
The project demonstrates fundamental Python programming and basic data visualization. It covers the main assignment requirements: recording fitness data, checking the daily goal, generating a summary, calculating BMI, validating input, and displaying a bar chart. A current limitation is that records are kept in memory and are cleared when the program exits; CSV or database storage could be added in a future version.
![alt text](<project Image 2026-11-16 at 13.31.42 (1)-1.jpeg>)