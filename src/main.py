import os
from count_islands import run_count_islands_script


if __name__ == "__main__":
    file_path = os.getenv("file_path")
    batch_size = os.getenv("batch_size")

    if not file_path:
        print(f"""
              Hello world! 
              The path to the file is: '{file_path}'.
              Use 'docker run -e file_path="path_to_file" ~' 
              to specify the path to the task""")
    else:
        run_count_islands_script(file_path, batch_size)