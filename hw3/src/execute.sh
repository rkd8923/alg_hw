#!/bin/bash
args1=$1
echo `javac *.java -d .`
echo `java alg_hw3.SCC $args1`
exit 0
