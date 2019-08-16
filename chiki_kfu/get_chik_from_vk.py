import vk
import time
session = vk.Session(access_token='544191d8544191d8544191d8345427c2bc55441544191d80fefe48d88a429c5fe6f03cb')
vk_api = vk.API(session)

#vk_api.users.get(user_id=1,v=5.101)

devki = []

for n in range(25):
	print(n*4,'%')
	members = vk_api.groups.getMembers(group_id='podslushankfu',sort='id_asc',offset=n*1000,count=1000,v=5.101)
	user = vk_api.users.get(user_ids=members['items'],fields='sex,has_photo,photo_400_orig',v=5.101)
	
	for u in user:
		devka = {}
		try:
			if u['sex']==1 and u['has_photo']==1:
				devka['id']=u['id']
				devka['photo']=u['photo_400_orig']
				devki.append(devka)
		except:
			pass
	time.sleep(1)
f = open('text.txt', 'w')
for devka in devki:
	f.write(str(devka['id'])+' ' + devka['photo']+'\n')


# f = open('text.txt','r')
	# text = f.read()
	# text = text.split('\n')
	# count = 0
	# for t in text:
	# 	data = t.split()
	# 	chika = Chika(vk_link='https://vk.com/id'+data[0],photo_link=data[1],likes=0)
	# 	chika.save()
	# 	print(count)
	# 	count+=1