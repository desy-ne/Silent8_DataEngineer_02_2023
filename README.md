# Silent8_DataEngineer_02_2023

### VERSION 0.1

### Building Docker image & run 
## Build Image
To build docker image use command:
```
docker build -t island_counter-image .
```
## Run Container
To build docker container use command:
```
docker run -e file_path="dej_rade" --name island_counter-container island_counter-image
```

## Future Improvements
* Make file to remove container and image.

* Option to add build and run container with file_path

* Make .md file more readable

* Include requirements.txt if needed to Dockerfile - currently there is no need since there are no external packages being used.