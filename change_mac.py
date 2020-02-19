#!/usr/bin/env python3.8

import subprocess, re, optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change HW MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New HW MAC address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new HW MAC, use --help for more information.")
    return options


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface], universal_newlines=True)
    # print(ifconfig_result)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print(f"Current MAC = {current_mac}")

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to {current_mac}")
else:
    print(f"[-] MAC address was not changed")
