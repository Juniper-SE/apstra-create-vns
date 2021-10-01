## Security Zones & Virtual Networks Creation/Deletion using Apstra APIs

This script create/delete multiple security zones and virtual networks Via Apstra API calls

## Requirements

Juniper Apstra version 4.0
Ansible: `pip3/pip install ansible==2.10.4`

(Use Ansible version >= 2.10)

## Usage

Follow the steps below to run the scripts
* Edit the group_vars/all/secrets.yml file and include the AIS credentials
* Edit the group_vars/all/sz.yml file to include blueprint name (not the ID) already created in AIS, security zones and VNs to be created.
* Run the scripts

Script to create VNs and SZs:
```
ansible-playbook  pb.create_sz_vn.yml
```

Script to delete VNs and SZs:
```
ansible-playbook  pb.delete_sz_vn.yml
```


## Author Information

Jindu Okoli (jokoli@juniper.net)
