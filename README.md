# CONSERT-Context-Aware-Search

## OBA Quickstart
### 1. Create an OpenAPI (.yaml) file based on the ontology (.owl) file

All the details can be found here: https://oba.readthedocs.io/en/latest/quickstart/

1. Download the binary
2. Create the OBA config file (config.yaml), or use the one we already provide in /openapi-spec
```
$ java -jar oba-*-jar-with-dependencies.jar -c config-schedule.yaml   
```
3. The openapi.yaml file will be found in /outputs/precis-schedule/servers/

### 2. Generate the MVC files for the client/server instances

1. First, install [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator).
2. Take the previously openapi.yaml file and copy/replace it to /openapi-server folder.
3. Now, there is a minor change to do to the .yaml file, to work properly. Open the file, and replace the "id" keywords with any other keyword. In our example, we replaced it with "thingid".

More details here: https://github.com/OpenAPITools/openapi-generator/issues/3304
### 3. Prepare the server instance
```
# Prepare the server-end code
openapi-generator generate -i openapi.yaml -g python-flask -o codegen_server_completed/

# Prepare the client-end code
openapi-generator generate -i openapi.yaml -g python -o codegen_client/
```
The command depends on the way you installed OpenAPI generator. For example, if you install it with NPM, the command is:

```
# Prepare the server-end code
openapi-generator-cli generate -i openapi.yaml -g python-flask -o codegen_server_completed/

# Prepare the client-end code
openapi-generator-cli generate -i openapi.yaml -g python -o codegen_client/
```
4. Now, you can give it a try:
   
To run the API service, change to the directory codegen_server_completed/ and run the following commands:
```
# Install dependencies for the API service
pip install -r requirements.txt

# Start the API service
python -m openapi_server
```
Try the API service in browser at localhost:8080/users/1. You should see the following outputs:

```
{
   "display_name": "Example User",
   "email": "user@example.com",
   "name": "1"
}
```
OpenAPI Generator also provides a UI for your convenience; visit it at localhost:8080/ui

### 4. Prepare the client instance
[Here](https://medium.com/@ratrosy/building-apis-with-openapi-ac3c24e33ee3) can be found details about the client instance. 
