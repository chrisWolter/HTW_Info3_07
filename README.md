# /lab-testing

Source code for the testing lab in [Info3](http://bkleinen.github.io/info3)

## Use pytest!

the test examples in a_structural_and_specification_tests
are written with pytest. It should require no further expanation
as it is simpler than unittest. 

You can also execute the unittest tests with pytest to get
a better output in the command line.

## Testing with docker

some subdirectories contain a docker_test.sh, which you can use
to run the tests without any further installation (apart from docker.)

it can be used in *nix shells like this:

    ./docker_test.sh

The file contains one docker run command which can also be issued directly. (remove the slashes if you shorten it to one line)

The Dockerfiles for the images are here: https://github.com/bkleinen/docker-images



