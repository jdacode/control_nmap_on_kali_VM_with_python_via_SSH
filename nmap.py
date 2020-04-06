import paramiko


class Nmap:
    def run_nmap(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('192.168.1.58', username='kali', password='kali')

        stdin, stdout, stderr = client.exec_command('nmap 192.168.1.1')
        result = ""
        for line in stdout:
            print(line.strip('\n'))
            result = result + '<br>' + line
        print(result)
        client.close()
        return result



