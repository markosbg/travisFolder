from datetime import datetime
# print('Marko')
def main():
    sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
    with open("README.md", "a") as myfile:
        myfile.write('\n'+sttime)


if __name__ == '__main__':
    main()
