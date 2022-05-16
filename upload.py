#uploading image
import requests
url = 'http://localhost:80/upload.php'
files = {'image': open('teacher.png', 'rb')}
requests.post(url, files=files)