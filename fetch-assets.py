# Run once (needs internet): downloads your three project images from the old site into assets/p1-p3.jpg
import re,urllib.request as u
h=u.urlopen(u.Request("https://wyrmscalesyndicate.com/en-eur/pages/projects",headers={"User-Agent":"Mozilla/5.0"})).read().decode()
seen=[]
for m in re.findall(r'https://imgproxy\.fourthwall\.dev/[^\s"\')]+\.jpg',h):
    if m not in seen: seen.append(m)
for i,m in enumerate(seen[:3],1): open(f"assets/p{i}.jpg","wb").write(u.urlopen(u.Request(m,headers={"User-Agent":"Mozilla/5.0"})).read()); print("saved p%d"%i)
