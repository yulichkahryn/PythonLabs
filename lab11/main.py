import re
import time
import zipfile


def find_failed_requests():
    zip_log = zipfile.ZipFile('access.log.zip')
    log_file = zip_log.open('access.log.txt')
    date_format = "%d/%b/%Y:%H:%M:%S"
    min_date = time.strptime("23/Mar/2009:06:29:10", date_format)
    max_date = time.strptime("23/Mar/2009:08:13:32", date_format)
    counter = 0

    for line in log_file:
        log = re.search('.*((23/Mar/2009:\d\d:\d\d:\d\d).*(4\d\d) (\d+))', str(line))
        if log:
            date = time.strptime(log.group(2), date_format)
            if min_date <= date <= max_date:
                counter += 1
                print(line)
    print(counter)

    zip_log.close()


def main():
    print("Printing all failed requests... ")
    find_failed_requests()


if __name__ == '__main__':
    main()
