project_name="random-generator-334612";
deployment_file="deployment.json";
gcloud workspace-add-ons deployments create $project_name --deployment-file=$deployment_file;
gcloud workspace-add-ons deployments install $project_name;


