#!/bin/bash -xe

argc=$#
argv=($@)


bd(){
	: '
	create image postgresql
	'
	docker build -f Dockerfile.bd -t "$image:$tag" .;
}

app(){
	: '
	create image app
	'	
	docker build -f Dockerfile.app -t "$image:$tag" .; 
}

ng(){
	: '
	create image app
	'	
    docker build -f Dockerfile.ng -t "$image:$tag" .; 
}

image=$1
tag=$2

$3
