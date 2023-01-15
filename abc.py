import speedtest
t=speedtest.Speedtest()
print("Finding servers..")
find_server=t.get_servers()
print("Finding best server")
get_best_server=t.get_best_server()
print("found best server")
print("checkng download speed...")
print("checcking upload speed...")
print("chhecking ping resluts")

ds=t.download()
us=t.download()
ping=t.results.ping

ods={ds / 1024 / 1024}
ous={us / 1024 / 1024}
print(f"Your download speed is:{ods} mbps")
print(f"Your upload speed is:{ous} mbps")
print(f"Your ping is {ping}ms")


