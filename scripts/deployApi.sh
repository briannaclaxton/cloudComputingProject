MY_INSTANCE_NAME="cisc5550-instance"
ZONE=us-central1-a

gcloud compute instances delete cisc5550-instance -q

gcloud compute instances create $MY_INSTANCE_NAME \
    --image-family=debian-9 \
    --image-project=debian-cloud \
    --machine-type=g1-small \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=cisc5550-startup-script.sh \
    --zone $ZONE \
    --tags http-server