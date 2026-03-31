@echo off
:: Direct Python aur Streamlit ka address
set PY_PATH=C:\Users\User\AppData\Local\Microsoft\WindowsApps\python3.13.exe
set STR_PATH=C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\streamlit.exe

:: Folder mein jaana
cd /d "C:\Users\User\Desktop\AgriGuard-AI"

:: Direct Streamlit chalana
"%PY_PATH%" -m streamlit run app.py
pause