Terrapod Platform 

Terrapod is an IoT + AI-based soil intelligence platform designed to help farmers monitor soil health in real time and receive data-driven fertilizer recommendations.
Problem Statement
Farmers often rely on guesswork or expensive lab tests to understand soil health. This leads to:
- Overuse or underuse of fertilizers
- Reduced crop yield
- Long feedback cycles for soil testing

Terrapod solves this by providing on-field, real-time soil insights.

Solution
Terrapod is a smart soil monitoring device combined with an AI-powered recommendation engine that measures:
- Soil moisture
- Soil temperature
- NPK levels (estimated)
- Organic carbon (low-range estimation)
- Visual soil indicators using an embedded camera

The data is processed to generate actionable fertilizer and irrigation recommendations.

AI Modules Used
- Rule-based nutrient recommendation engine
- Regression models for NPK estimation
- Time-series analysis for moisture trends
- Computer vision (experimental) for soil texture & color analysis
- Decision logic for crop-specific recommendations

System Architecture
1. Terrapod device (ESP32 + sensors + camera)
2. Wireless data transmission
3. Backend processing & AI inference
4. Farmer-facing mobile/web dashboard

Tech Stack
- Hardware: ESP32, soil sensors, camera module
- Backend: Python (Flask/FastAPI – planned)
- AI/ML: Scikit-learn, rule-based logic
- Frontend: Mobile app (planned)
- Cloud: Firebase / AWS (planned)
- 
Project Status
This repository represents the **early prototyping phase** of Terrapod.
Current focus:
- Hardware validation
- AI logic design
- System architecture planning
- 
Future Work
- Sensor calibration
- Model training with real soil data
- Farmer app development
- Pilot deployment with multiple Terrapods
Team
Second-year CSE students building Terrapod as part of a startup prototype and innovation challenge.
