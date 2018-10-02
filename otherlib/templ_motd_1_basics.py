#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(),
            state=dict()
        )
    )

    result = dict(changed=False)

    module.exit_json(**result)

if __name__ == '__main__':
    main()

