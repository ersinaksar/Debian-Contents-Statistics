import csv
import gzip
import argparse
import urllib.request

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('architecture', metavar='arch', type=str,
                        help='architecture for which to download contents file')

    args = parser.parse_args()
    url = f"http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{args.architecture}.gz"
  
    urllib.request.urlretrieve(url, f"Contents-{args.architecture}.gz")
    with gzip.open(f"Contents-{args.architecture}.gz", 'rb') as f:
        contents = f.read()
    with open("contents.txt", "w") as f:
        f.write(contents.decode())

    file = "contents.txt"
    with open(file) as f:
        package_file_count = {}
        reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
        for row in reader:
            if ',' in row[1]:
                packages = row[1].split(",")
                for package in packages:
                    #increment the number of files using the package name
                    if package in package_file_count:
                        package_file_count[package] += 1
                    else:
                        package_file_count[package] = 1
            else:
                # If there is only one package, increase the file count using the package name.
                package = row[1]
                # increment file count using package name
                if package in package_file_count:
                    package_file_count[package] += 1
                else:
                    package_file_count[package] = 1
        for package, file_count in sorted(package_file_count.items(), key=lambda item: item[1], reverse=True)[:10]:
            package = package.split('/')[-1]
            print(f"{package} {file_count}")

