from template_engine import render
host = "https://6ab3-92-38-32-98.ngrok.io"
"""
Due to JSON manifest of app contains a lot of entries of hostname (e.g. where each endpoints is defined)
it is far more convinient to use a template with placeholders for hostname. Hostname is chaing sometimes
really often (especially when ngrok tunnel is used for test deploy)
"""
if __name__ == '__main__':
    with open('deployment/deployment.json', 'w') as file:
        file.write(render('deployment.json', template_dir='deployment_templates', url_host=host))
    