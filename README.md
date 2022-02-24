# tenzor_devops_school
### Tenzor DevOps School. Homework Storage.
Please feel free to discover a Virtual Lab Infrastructure's scheme.
> FileName : scheme.png <br />
![scheme](https://user-images.githubusercontent.com/33868527/155518559-e33facfa-097a-425f-84f8-eae612af975b.png)

#### Also, there is a content of /etc/ansible/ansible.cfg, /etc/ansible/hosts and /etc/hosts down below:
> Ansible Configuration File: /etc/ansible/ansible.cfg
```
# config file for ansible -- https://ansible.com/
# ===============================================

# nearly all parameters can be overridden in ansible-playbook
# or with command line flags. ansible will read ANSIBLE_CONFIG,
# ansible.cfg in the current working directory, .ansible.cfg in
# the home directory or /etc/ansible/ansible.cfg, whichever it
# finds first

[defaults]
host_key_checking = False
callback_whitelist = timer, profile_tasks, profile_roles
remote_user = ansible

[inventory]
###########

[privilege_escalation]
become = True

[paramiko_connection]
#####################

[ssh_connection]
ssh_args = -C -o ControlMaster=auto -o ControlPersist=60s

[persistent_connection]
#######################

[accelerate]
############

[selinux]
######### 

[colors]
########

[diff]
######

```
> Ansible Inventory File: /etc/ansible/hosts
```
[all_nodes]
centos-01
centos-02
ubuntu-01

[centos_nodes]       
centos-01
centos-02

[ubuntu_nodes]       
ubuntu-01
```
> Ansible Manager's Hostname-To-IpAddr resolving file: /etc/hosts
```
##############################################################################
w.x.y.55     master.domain.test      master
w.x.y.56     ansible.domain.test     ansible
w.x.y.57     n-vcsa-01.domain.test   n-vcsa-01
w.x.y.58     gitstore.domain.test    gitstore
#
w.x.y.78     centos-01.domain.test   centos-01
w.x.y.79     centos-02.domain.test   centos-02
w.x.y.80     ubuntu-01.domain.test   ubuntu-01
##############################################################################
```
