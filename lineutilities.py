import argparse
import requests

def DownloadFile(url , local_filename):
    #local_filename = url.split('/')[-1] use when you want to save the file with the same name as in url
    
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


parser = argparse.ArgumentParser()

# Add arguments to the parser
parser.add_argument("url", help = "the Url of file to download")

parser.add_argument("output", help = "by which name do  you want to save the file")

#Parser the arguments
args = parser.parse_args()

#use the arguments in your code
print(args.url)
print(args.output)
DownloadFile(args.url, args.output)

