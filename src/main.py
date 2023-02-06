import os


if __name__ == "__main__":
    path_to_file = os.getenv("file_path")
    if not path_to_file:
        print(f"""
              Hello world! 
              The path to the file is: '{path_to_file}'.
              Use 'docker run -e file_path="path_to_file" ~' 
              to specify the path to the task""")
    else:
        print("Hello World! Thank you for providing path to file !")