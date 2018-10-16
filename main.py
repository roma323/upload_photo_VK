from constants import TOKEN, GROUP_ID, ALBUM_ID
import vk
import time
import requests
import os




def auth(token):
	global API
	sess = vk.Session(access_token=token)
	API = vk.API(sess, v=5.85)

def get_upload_server(album_id,group_id):
	result = API.photos.getUploadServer(album_id=album_id,group_id=group_id)
	return result['upload_url']

def upload(file_name,url):
	with open(file_name,'rb') as f:
		data = f.read()
	r = requests.post(url, files={'photo':(file_name,data)}).json()
	print(r)
	return r


def main():

	auth(TOKEN)
	#Album = API.photos.createAlbum(title=input('Введите название альбома: '), privacy_view=['nobody'])
	os.chdir('Photos')
	photos = os.listdir()
	for photo in photos:
		upload_url = get_upload_server(ALBUM_ID,GROUP_ID)
		data = upload(photo,upload_url)
		r = API.photos.save(group_id=GROUP_ID, album_id=data['aid'],server=data['server'],photos_list=data['photos_list'],hash=data['hash'])
		time.sleep(5)
if __name__ == '__main__':
	main()