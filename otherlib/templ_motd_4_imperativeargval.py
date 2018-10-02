#!/usr/bin/python

import os
from ansible.module_utils.basic import AnsibleModule

motd_file = '/home/mdavis/motd'

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(),
            state=dict()
        )
    )

    message = module.params['message']
    requested_state = module.params['state']

    if requested_state is None:
        requested_state = 'present'

    if requested_state not in ['present','absent']:
        module.fail_json(msg='"state" must be one of "present" or "absent"')

    if requested_state == 'present' and message is None:
        module.fail_json(msg='"message" must be specified when "state" is "present"')

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

    if changed:
        if requested_state == 'present':
            with open(motd_file, 'w') as fd:
                fd.write(module.params['message'])
        else:
            os.remove(motd_file)

    result = dict(changed=changed)

    module.exit_json(**result)

if __name__ == '__main__':
    main()

