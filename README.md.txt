# Go Safer 🚦

### A Smart Traffic Awareness App with Speed Control & Route Advisory Simulation

---

## Project Overview

Go Safer is a mobile application designed to combat traffic congestion in Egypt and promote road safety. Our app utilizes **community voting** and **real-time GPS data** to help users identify the least crowded roads and receive alerts when they exceed speed limits.

The application aims to:

* Inform users whether their selected roads are congested.
* Warn users when exceeding road speed limits.
* Provide road safety tips and emergency support.
* Allow complaint reporting on damaged roads or unsafe conditions.

This repository contains:

* A conceptual overview of the project.
* A **Python-based simulation** of the app’s main functionalities using Turtle graphics and audio alerts.

---

## Objectives

1. Traffic Monitoring via Voting
   Users report if a road is busy or not. The app aggregates this data to inform others in real time.

2. Speed Monitoring and Alerts
   The app contains speed limits for all Egyptian roads. Using a GPS speedometer, it notifies drivers if they exceed legal limits.

3. Road Safety Tips
   Users can access driving safety rules, emergency numbers, and submit complaints about road infrastructure.

4. Community-Driven Reporting
   Voting by recent travelers enhances route recommendations.

---

## Simulation Code Description

We created a simulation using Python’s `turtle` and `playsound` libraries to demonstrate the core logic:

* Input 1: Whether the main street is busy.
* Input 2: The speed you are driving.
* Logic:

  * If the road is busy, the turtle takes a different route.
  * If speed > 6 or ≤ 0.5, an alarm sounds and a warning is shown.
  * If speed is valid and the road is free, the turtle moves forward along the main route.

> The simulation illustrates the decision-making flow of the application.

---

## How to Run the Simulation

### Requirements

Install Python 3.x and the required library:

```bash
pip install playsound
```

### Run

```bash
python Simualtion.py
```

You’ll be prompted to:

* Enter if the main street is busy (`busy` or `not busy`)
* Enter your speed (e.g., `5`, `7`, `0.4`)

The turtle will then move accordingly, and a sound will play if you exceed the speed limit.

---

## 🔗 References & Tools

* [Kivy Documentation](https://kivy.org/)
* [Why Traffic Jams Happen](https://www.livescience.com/61862-why-phantom-traffic-jams-happen.html)
* [Play Sound in Python](https://www.geeksforgeeks.org/play-sound-in-python/)
* [Speedometer Widget](https://m.apkpure.com/speedometer-widget/com.horty2.tachimetrowidget20)

---

## Additional Resources

You can access all project files, including PDFs and videos, from this OneDrive folder:  
https://drive.google.com/drive/folders/1NVnNLJLI1cPwYUyNSSYtqgZ8q78y4-F1?usp=sharing
