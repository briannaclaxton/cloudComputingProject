MY_CLUSTER_NAME="todo-cluster"
MY_IMAGE="briannaboyce/todo:v1"
MY_INSTANCE_NAME="cisc5550-instance"
ZONE=us-central1-a

gcloud compute instances create $MY_INSTANCE_NAME \
    --image-family=debian-9 \
    --image-project=debian-cloud \
    --machine-type=g1-small \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=cisc5550-startup-script.sh \
    --zone $ZONE \
    --tags http-server

export TODO_API_IP=`gcloud compute instances list --filter=$MY_INSTANCE_NAME --format="value(EXTERNAL_IP)"`

docker build -t briannaboyce/todo . 

docker push $MY_IMAGE

gcloud container clusters create $MY_CLUSTER_NAME \
    --num-nodes=2

kubectl create deployment todolist \
	 --image=$MY_IMAGE

kubectl expose deployment todolist \
	--type=LoadBalancer \
	--port 80 \
	--target-port 5000
