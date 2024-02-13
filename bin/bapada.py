
import os

from scripts.main import main

if __name__ == "__main__":
    main()

try:
    # clean up environment at the end of execution
    os.system("pyclean .")
except:
    print("pyclean . \nFailed execution. Exiting...")




