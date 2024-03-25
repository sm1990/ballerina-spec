import requests
import sys
import shutil
import os

response = requests.get("https://api.github.com/repos/ballerina-platform/ballerina-spec/releases/latest")
print('1')
updated_spec = open("updated_spec.md", 'a')

spec_version = response.json()["name"]
release_date = response.json()["published_at"][0:10]
release_note = response.json()["body"]
print('3')
with open(sys.argv[1],'r') as read_obj:
    print('4')
    for line in read_obj.readlines():
        print('5')
        if "| ------- | ------------ | ----------- |" in line:
            print('6')
            updated_spec.write(line)
            updated_spec.write('| <a target="_blank" href="/spec/lang/'+spec_version+'/">'+spec_version+'</a> | '+release_date+' | '+release_note+' |\n')
            continue
        updated_spec.write(line)
print('7')
os.remove(sys.argv[1])
shutil.copy("updated_spec.md",sys.argv[1])
