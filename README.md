# Cloud Computing Project - Brianna Boyce
CISC 5550 Cloud Computing Project

A simple todolist example app and API using Flask 

The `scripts` directory contains scripts helpful for startup and destroying. 

This project is setup so that any merge to master will kick off a deployment to Kubernetes. 

To run the full deployment manually from Linux, run `./kuberScript.sh`

To run just the API VM, run `deployApi.sh`

To destroy both the cluster and the VM, run `destory.sh`

If utilizing the Github action, run the deploy script first to setup the API, then merge to master. Deploy scripts will first take down any existing instances before standing up new ones. 
