@echo off
title Finance Tracker
cd /d "%~dp0"
python -m streamlit run app.py
pause
