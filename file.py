# with open("/tmp/foo.txt") as file:
#     data = file.read()




class Sample:
    def __enter__(self):
        print("In__enter()__")
        return "FOO"
    def __exit__(self, type, value, trace):
        print("In_exit()__")

def get_sample():
    return Sample()


with get_sample() as sample:
        print("sample: ", sample)



