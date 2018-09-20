import requests

r = requests.get("https://www.baidu.com")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

print("============================================")

headers = {
    'Cookies':'d_c0="ALClcZZ7tQ2PTmeDAqbacunh7NQLpzQhTaE=|1528297401"; _zap=1455399c-b848-4276-b53d-6657b5a51bcc; z_c0="2|1:0|10:1528536409|4:z_c0|92:Mi4xVnVzYkFnQUFBQUFBc0tWeGxudTFEU1lBQUFCZ0FsVk5XZXNJWEFETU1SYUVhYjJKdnVQSGRUMUZlNkhmVXFVc1h3|d07178dc0586dde68b4a8cbf47936092c261bbeea08dfbaf57eb62fb5234ae94"; __utmv=51854390.100-1|2=registration_date=20150919=1^3=entry_date=20150919=1; q_c1=4a8ea4dde6734eb889278f1f150b49e5|1537369081000|1528297401000; tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; _xsrf=2021567a-9d4b-46c3-a25d-e149709b7b9f; __utma=51854390.1617423714.1529074135.1537443437.1537454349.5; __utmb=51854390.0.10.1537454349; __utmc=51854390; __utmz=51854390.1537454349.5.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'Host':'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
