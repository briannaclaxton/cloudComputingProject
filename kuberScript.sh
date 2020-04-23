MY_CLUSTER_NAME="todo-cluster"
MY_IMAGE="briannaboyce/todo:v1"

gcloud container clusters create $MY_CLUSTER_NAME \
    --num-nodes=2

kubectl create deployment todolist \
	 --image=$MY_IMAGE

kubectl expose deployment todolist \
	--type=LoadBalancer \
	--port 80 \
	--target-port 5000
