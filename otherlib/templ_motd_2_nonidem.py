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

    fd = open(motd_file, 'w')
    fd.write(module.params['message'])
    fd.close()

    result = dict(changed=True)

    module.exit_json(**result)

if __name__ == '__main__':
    main()

