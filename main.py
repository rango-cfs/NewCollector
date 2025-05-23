import requests
import re


def fetch_v2ray_links(channel_url):
    vless_links = []
    vmess_links = []
    # ss_links = []

    for link in channel_url:
        response = requests.get(link)
        vless_links.extend(re.findall(r'vless://[^\s]+', response.text))
        vmess_links.extend(re.findall(r'vmess://[^\s]+', response.text))
        # ss_links.extend(re.findall(r'ss://[^\s]+', response.text))

    return vless_links,vmess_links

def extract_links(content):
    vless_links = []
    vmess_links = []
    # ss_links = []
    for link in content:
        vless_links.extend(re.findall(r'vless://[^\s]+', link))
        vmess_links.extend(re.findall(r'vmess://[^\s]+', link))
        # ss_links.extend(re.findall(r'ss://[^\s]+', link))
    return vless_links, vmess_links

def save_links_to_file(vless_links, vmess_links, filename):
    with open(filename, 'w') as file:
        
        file.write("VLESS Links:\n")
        for link in vless_links:
            file.write(link + "")

        file.write("\nVMESS Links:\n")
        for link in vmess_links:
            file.write(link + "\n")


def main():
    channel_url  = ['https://t.me/s/IP_CF_Config','https://t.me/s/nufilter','https://t.me/s/Tunder_vpn']
    content = fetch_v2ray_links(channel_url)
    if content:
        vless_links, vmess_links =  content

        # qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
        # data = "https://raw.githubusercontent.com/rango-cfs/NewCollector/refs/heads/main/v2ray_links.txt"

        # qr.add_data(data)
        # qr.make(fit=True)
        # img = qr.make_image(fill_color="black", back_color="white")
        # img.save("qr_code_v2ray_links.png")


        # save_links_to_file_vless(vless_links, 'v2ray_link_vless.txt')
        # save_links_to_file(vless_links, vmess_links, ss_links, 'v2ray_links.txt')

        file1 = open("v2ray_links.txt", "w+")
    
        file1.write("VLESS Link:\n")
        for vle in vless_links:
            file1.writelines(vle[:-2].replace("amp;", "")
                            .replace('%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws2</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws3</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws4</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws5</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws6</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws2</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws3</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A6%F0%9F%87%B9+ws5<br/><br/>', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws4</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%B3%F0%9F%87%B1+ws</code><br/><br/><tg-emo', "")
                            .replace('%40NUFiLTER+%F0%9F%87%A6%F0%9F%87%B9ws5</code><br/><br/><tg-emo', "")
                            .replace("%40NUFiLTER+%F0%9F%87%A6%F0%9F%87%B9+ws5<br/><br/>", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws7</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+TLS</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A6%F0%9F%87%B9ws3<br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%B3%F0%9F%87%B1+ws2<br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+tls3+mci</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws+%28mtn%29</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+tls+%28mci%29</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws%F0%9F%9F%A1</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+tls%F0%9F%94%B5</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws%F0%9F%9F%A12</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+tls%F0%9F%94%B52</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AATLS2</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+tls%F0%9F%94%B5</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws%F0%9F%9F%A1</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws%F0%9F%9F%A1%F0%9F%94%B5</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws%F0%9F%9F%A1</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+tls%F0%9F%94%B5</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws%F0%9F%9F%A1</code><br/><br/><tg-emo", "")
                            .replace("%40NUFiLTER+%F0%9F%87%BA%F0%9F%87%B8TLS</code></div></div><d", "")
                            .replace("#", "#IP_CF\n"))
            print(file1) 
            

        file1.write("\n")
        file1.write("VMESS Link:\n")
        for vme in vmess_links:  
            file1.writelines(vme[:-58].replace("<", "\n"))
            print(file1) 
        
        
        # file1.write("\n")
        # file1.write("SS Link:\n")
        # for vme in ss_links:
        #     file1.writelines(vme[:-2].replace("amp;", "")
        #                      .replace("</code><br/><br/>•••••••••••••••••••••••••••••••••••<br/>", "\n")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws4</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws5</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws2</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws3</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A6%F0%9F%87%B9+ws5<br/><br/>", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws4</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws6</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws2</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A8%F0%9F%87%AD+ws3</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws4</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%B3%F0%9F%87%B1+ws</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws2</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws3</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws4</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A6%F0%9F%87%B9ws5</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws6</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws7</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+ws2</code><br/><br/><tg-emo", "")
        #                      .replace("%40NUFiLTER+%F0%9F%87%A9%F0%9F%87%AA+TLS</code><br/><br/><tg-emo", "")
        #                      .replace("#", "#IP_CF\n"))
            print(file1) 
            
        file1.close()




if __name__ == "__main__":
    main()
