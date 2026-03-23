import traceback
try:
    from app import *
    print("app.py imported successfully!")
except Exception as e:
    print("Error importing app.py:")
    traceback.print_exc()

try:
    from frontend import *
    print("frontend.py imported successfully!")
except Exception as e:
    print("Error importing frontend.py:")
    traceback.print_exc()
