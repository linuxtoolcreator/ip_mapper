import subprocess

ip_range = "206.94.180.158/24"  # IP adresi aralığı
cmd = f"nmap -sn {ip_range}"  # nmap komutu
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

ips = []
for line in output.splitlines():
    line = line.strip().decode()
    if "Nmap scan report for" in line:
        ip = line.split()[-1]
        ips.append(ip)

print("Ağdaki IP adresleri: ")
print(ips)

f = open(ips.txt, "w")