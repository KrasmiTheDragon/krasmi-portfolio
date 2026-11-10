import json,os,urllib.request as u,urllib.parse as p,datetime
def J(url,h=None,d=None): return json.load(u.urlopen(u.Request(url,data=d,headers=h or {})))
S=json.load(open('assets/stats.json'));ch=False
def twitch():
    c,s=os.environ['TWITCH_ID'],os.environ['TWITCH_SECRET']
    t=J('https://id.twitch.tv/oauth2/token',d=p.urlencode({'client_id':c,'client_secret':s,'grant_type':'client_credentials'}).encode())['access_token']
    h={'Client-Id':c,'Authorization':'Bearer '+t}
    b=J('https://api.twitch.tv/helix/users?login=krasmi',h)['data'][0]['id']
    return J('https://api.twitch.tv/helix/channels/followers?broadcaster_id='+b,h)['total']
def yt(hd): return int(J('https://www.googleapis.com/youtube/v3/channels?part=statistics&forHandle='+p.quote(hd)+'&key='+os.environ['YT_KEY'])['items'][0]['statistics']['subscriberCount'])
def bsky(a): return J('https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor='+a)['followersCount']
for r in S['rows']:
    k=r.get('a')
    if not k: continue
    try: r['f']=twitch() if k=='twitch' else yt(k[3:]) if k[:3]=='yt:' else bsky(k[5:]); ch=True
    except Exception as e: print('skip',k,e)
if ch: S['fu']=datetime.date.today().isoformat()
json.dump(S,open('assets/stats.json','w'),ensure_ascii=False,indent=1)
