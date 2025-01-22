import requests
import re



def fetch_v2ray_links(channel_url):
    response = requests.get(channel_url)
    if response.status_code == 200:
        return response.text
    return None

def extract_links(content):
    vless_links = []
    vmess_links = []
    ss_links = []
    vless_links = re.findall(r'vless://[^\s]+', content)
    vmess_links = re.findall(r'vmess://[^\s]+', content)
    ss_links = re.findall(r'ss://[^\s]+', content)
    return vless_links, vmess_links, ss_links

def save_links_to_file(vless_links, vmess_links, ss_links, filename):
    with open(filename, 'w') as file:
        
        file.write("VLESS Links:\n")
        for link in vless_links:
            file.write(link + "")

        file.write("\nVMESS Links:\n")
        for link in vmess_links:
            file.write(link + "\n")

        file.write("\nSS Links:\n")
        for link in ss_links:
            file.write(link + "\n")

def main():
    channel_url = 'https://t.me/s/IP_CF_Config'
    content = fetch_v2ray_links(channel_url)
    if content:
        vless_links, vmess_links, ss_links =  extract_links(content)



        # save_links_to_file_vless(vless_links, 'v2ray_link_vless.txt')
        # save_links_to_file(vless_links, vmess_links, ss_links, 'v2ray_links.txt')

        file1 = open("v2ray_links.txt", "w+")
    
        file1.write("VLESS Link:\n")
        for vle in vless_links:
            file1.writelines(vle[:-2].replace("amp;", "").replace("#", "#IP_CF\n"))
            print(file1) 
            

        file1.write("\n")
        file1.write("VMESS Link:\n")
        for vme in vmess_links:  
            file1.writelines(vme[:-58].replace("<", "\n"))
            print(file1) 
        
        
        file1.write("\n")
        file1.write("SS Link:\n")
        for vme in ss_links:
            file1.writelines(vme[:-2].replace("amp;", "").replace("#", "#\n").replace("</code><br/><br/>•••••••••••••••••••••••••••••••••••<br/>", "\n"))
            print(file1) 
            
        file1.close()




if __name__ == "__main__":
    main()
