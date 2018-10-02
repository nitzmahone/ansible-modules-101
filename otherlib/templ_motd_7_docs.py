#!/usr/bin/python

DOCUMENTATION = '''
---
module: motd
author:  Matt Davis (@nitzmahone)
short_description: Set message of the day
description:
    - Manages message of the day file.
options:
    message:
        description:
            - Message to set.
    state:
        description:
            - Whether motd file should exist or not.
        default: present
        choices: ['present', 'absent']
'''

EXAMPLES = '''
- name: set message of the day 
  motd:
    message: Hello from Ansible!
    state: present
    
- name: ensure no MOTD file exists
  motd:
    state: absent
'''

RETURNS = '''
motd_path:
    description: path to MOTD file used by module
    returned: success
    type: string
'''

import os
from ansible.module_utils.basic import AnsibleModule

motd_file = '/home/mdavis/motd'

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str'),
            state=dict(type='str', choices=['present','absent'], default='present')
        ),
        required_if=([('state', 'present', ['message'])]),
        supports_check_mode=True
    )

    message = module.params['message']
    requested_state = module.params['state']
    changed = False

    exists = os.path.exists(motd_file)

    if exists:
        if requested_state == 'present':
            with open(motd_file, 'r') as fd:
                current_message = fd.read().strip()

            if current_message != message:
                changed = True
        else:
            changed = True
    else:
        if requested_state == 'present':
            changed = True

    # to properly support check mode, do as much as possible
    # without actually making changes
    if changed and not module.check_mode:
        if requested_state == 'present':
            with open(motd_file, 'w') as fd:
                fd.write(module.params['message'])
        else:
            os.remove(motd_file)

    module.exit_json(changed=changed, motd_path=motd_file)

if __name__ == '__main__':
    main()

