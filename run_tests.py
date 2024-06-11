import subprocess
import logging
import sys
from concurrent.futures import ThreadPoolExecutor

def run_tests(test_path):
    result = subprocess.run([sys.executable, "-m", "pytest", test_path, "--alluredir=./allure_results"], check=True)

def main():    
    test_files = [
        "./Tests/UI_Test",
        "./Tests/API_Test",
        "./Tests/Mobile_Test",
        "./Tests/Accessibility_Test"
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(run_tests, test_file) for test_file in test_files]

        # Wait for all tasks to complete
        for future in futures:
            try:
                future.result(timeout=3600)
            except Exception as e:
                logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
