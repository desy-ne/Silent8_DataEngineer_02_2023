# Silent8_DataEngineer_02_2023

### VERSION 0.2

### Remove, Build Docker image & run 

## Removing docker image
At the beginning it is best to make sure docker files are removed. Use this command:

```
docker rm island_counter-container && docker rmi island_counter-image
```

## Build Image
To build docker image use command:
```
docker build -t island_counter-image .
```
## Run Container
To build docker container use command:
```
docker run -e file_path="./tests/test_file" --name island_counter-container island_counter-image
```

## All commands combined together to have faster build
```
docker rm island_counter-container && docker rmi island_counter-image
```

```
docker build -t island_counter-image . && docker run -e file_path="./tests/test_file" --name island_counter-container island_counter-image
```
## Future Improvements
* Make file to remove container and image.

* Option to add build and run container with file_path

* Make .md file more readable

* Include requirements.txt if needed to Dockerfile - currently there is no need since there are no external packages being used.