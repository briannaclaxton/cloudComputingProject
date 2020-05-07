MY_CLUSTER_NAME="todo-cluster"
MY_INSTANCE_NAME="cisc5550-instance"
ZONE=us-central1-a

gcloud compute firewall-rules delete rule-allow-tcp-5000

gcloud compute instances create $MY_INSTANCE_NAME \
    --image-family=debian-9 \
    --image-project=debian-cloud \
    --machine-type=g1-small \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=cisc5550-startup-script.sh \
    --zone $ZONE \
    --tags http-server

gcloud compute firewall-rules create rule-allow-tcp-5000 --source-ranges 0.0.0.0/0 --target-tags http-server --allow tcp:5000

export TODO_API_IP=`gcloud compute instances list --filter=$MY_INSTANCE_NAME --format="value(EXTERNAL_IP)"`

docker build -t briannaboyce/todo . 

docker push briannaboyce/todo

echo $TODO_API_IP

gcloud container clusters create $MY_CLUSTER_NAME \
    --num-nodes=2

kubectl run todolist \
	 --env="TODO_API_IP=$TODO_API_IP" \
	 --image=briannaboyce/todo \
	 --port=5000

kubectl expose deployment todolist \
	--type=LoadBalancer 

kubectl get service todolist
