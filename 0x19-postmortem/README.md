
# Postmortem

From 10:15 PM to 11:10 PM GMT, our database server could not serve because all incoming traffics were blocked by a firewall, for this reason our web server could not access the database resulting in users unable to access their data, the root cause of the issue was firewall configuration error.

# Timeline
- 10:08 PM: the configuration begin.
- 10:15 PM: the database stopped serving.
- 10:35 PM: a lot of users started complaining about the issue.
- 10:45 PM: one of our employee started taking a look
- 10:58 PM: found the issue.
- 11:05 PM: fixed the issue.
- 11:10 PM: the database started serving.

# Root cause

the cause of the issue was reinstalling ufw firewall on the server, which essentially blocked all incoming traffics.
and the issue was fixed by allowing a specific ip address in our case the web server to access the database in a specific port.

# Corrective and Preventative Measures

yesterday we were discussing about the issue that occurred and The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times.

- update the file permissions of the servers to only allow certain engineers.
- setup a slave database server so that if the master failed to serve the slave will be up.