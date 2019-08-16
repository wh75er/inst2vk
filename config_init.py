from properties import props

def initializeConfig(filename):
    f = open(filename, 'r')

    for line in f:
        param, value = line.split()
        if param not in props:
            print("config warning: <{}> is unknown parameter(ignoring)".format(param))
            continue

        try:
            props[param] = eval(value)
        except NameError:
            print("config warning: Value <{}> is invalid(You can use only numbers or booleans)(ignoring)".format(value))

    f.close()

if __name__ == "__main__":
    initializeConfig("config")
    print(props)
