
project_name="random-generator-334612";
deployment_file="deployment.json"
gcloud workspace-add-ons deployments replace $project_name --deployment-file=$deployment_file;
gcloud workspace-add-ons deployments uninstall $project_name;
gcloud workspace-add-ons deployments install $project_name;
