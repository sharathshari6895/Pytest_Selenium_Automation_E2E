import os

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', 'Config', 'config.ini')
ui_data_path = os.path.join(current_dir, '..', 'Data', 'ui_data.json')
mobile_data_path = os.path.join(current_dir, '..', 'Data', 'mobile_data.json')
assertion_data_path = os.path.join(current_dir, '..', 'Data', 'asseration_data.json')
api_data_path = os.path.join(current_dir, '..', 'Data', 'api_data.json')
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
ui_test_file = "./Tests/UI_Test"
api_test_file = "./Tests/API_Test/test_api.py"
mobile_test_file = "./Tests/Mobile_Test/test_bigoven.py"
accessibility_test_file = "./Tests/Accessibility_Test/test_accessibility.py"
