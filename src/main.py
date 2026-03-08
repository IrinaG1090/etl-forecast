import subprocess
import sys
from pathlib import Path

def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"[OK] {script_name} выполнен успешно")
    else:
        print(f"[ERROR] Ошибка в {script_name}: {result.stderr}")
        sys.exit(1)

def main():
    scripts = ["generate_data.py", "etl.py", "features.py", "train.py", "evaluate.py"]
    for script in scripts:
        run_script(script)
    print("\n[SUCCESS] Весь пайплайн успешно выполнен!")

if __name__ == "__main__":
    main()