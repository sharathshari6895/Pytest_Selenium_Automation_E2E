import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_tests(test_path):
    try:
        logging.info(f"Running tests in {test_path}...")
        result = subprocess.run(["pytest", test_path, "--alluredir=./allure_results"], check=True)
        logging.info(f"Tests in {test_path} finished with return code: {result.returncode}")
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running tests in {test_path}: {e}")
    except FileNotFoundError as e:
        logging.error(f"Executable not found: {e}")

def main():
    # Define test files
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

    logging.info("All test files have been executed.")

if __name__ == "__main__":
    main()
