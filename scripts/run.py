"""driver module"""
import sys
import getopt

def main(argv):
    """driver method"""
    try:
        opts, _ = getopt.getopt(argv, "p", ["production"])
    except getopt.GetoptError:
        print("run.py")
        sys.exit(2)
    dev = True
    for opt, _ in opts:
        if opt in ("-p", "--production"):
            print("Running in production mode")
            dev = False
    if dev:
        print("Running in development mode")

if __name__ == "__main__":
    main(sys.argv[1:])
