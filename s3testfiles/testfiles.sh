#!/bin/bash

bucket=pd-rdc-asdfp1

for i in $(seq 1 150); do
       echo "testfile ${i}-$(date)"> "testfile-${i}.txt"
       aws-okta exec rd-infra -- aws s3 cp "testfile-${i}.txt" "s3://${bucket}/"
       if [[ $((i%2)) -eq 0 ]]; then
	       aws-okta exec rd-infra -- aws s3 rm "s3://${bucket}/testfile-${i}.txt"
       fi
       rm "testfile-${i}.txt"
done

