from simple_worker_pip import *
import sys

token = "jTxYQDmMx5ZtVeZBT8jVx6oJDLw"
#token = "TSjcQAnNMZKWGdOyCJhxnN64CTk"
host= "174.129.54.171"
port = "8080"
version = "2"

sw = SimpleWorker(host, port, version, token)

projectName = "pip-gen-" + str(int(time.time()))
newProject = sw.postProject(projectName)

projects = sw.getProjects()

print str(projects)

project_id = projects[0]['id']

print "project_id = " + project_id

sw.setProject(project_id)  # make this the default...

details = sw.getProjectDetails(project_id)

print "details:  " + str(details)

# Make a new code (drop): 

name = "helloFromPython-" + str(time.time())
print "creating code (drop) with name:  " + name
ret = sw.postCode(project_id, name, "hello.py", "hello.zip")
time.sleep(1)
print "postCode returned:  " + str(ret)

# For a given project_id, get list of Codes:

codes = sw.getCodes(project_id)

print "codes:  " + str(codes)
for code in codes:
  if code['name'] == name:
    print "newly created coder:  " + str(code)
    code_id = code['id']

code_id = codes[-1]['id']
print "code_id = " + code_id
#sys.exit()

# get details for specific code (drop)
details = sw.getCodeDetails(code_id)
print "code details:  " + str(details)


task_id = sw.postTask(project_id, name)
print "postTask returned:  " + str(ret)

print "About to sleep 20 to let task run..."
time.sleep(20)

logstr = sw.getLog(project_id, task_id)
print "sw.getLog returns:  " + str(logstr)

