import ansible_runner
import sys

# list all host names, groups and IP addresses
out, err, rc = ansible_runner.run_command(
    executable_cmd='ansible-inventory',
    cmdline_args=['--list', '--yaml'],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr
)

# Ping hosts and output results
out, err, rc = ansible_runner.run_command(
    executable_cmd='ansible',
    cmdline_args=['all:localhost', '-m', 'ping'],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr
)