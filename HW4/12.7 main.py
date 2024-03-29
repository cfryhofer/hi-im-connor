#Connor Fryhofer 1853826

def get_age():
    age = int(input())
    if(age>=18 and age<=75):
        return age
    else:
        raise ValueError("Invalid age.")

def fat_burning_heart_rate(age):
    return ((70 / 100) * (220 - age))

if __name__ == '__main__':
    try:
        age = get_age()
        print("Fat burning heart rate for a",age,"year-old:",fat_burning_heart_rate(age),"bpm")
    except ValueError as ve:
        print(ve.args[0])
        print("Could not calculate heart rate info.\n")
