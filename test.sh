#!/bin/bash
for i in $(seq -w 1 40)
do
  mkdir "Sujet $i"
  mv "22-NSI-$i.pdf" "Sujet $i"
done