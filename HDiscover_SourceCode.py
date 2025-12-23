import requests
import math as m

# HDiscover: User Discovery & Ranking System {IN PROGRESS}
# MiniProject - Harshith Chegondi
# 17-Dec'2025 to Present

def fetch_user():
        url = "https://randomuser.me/api/"
        response = requests.get(url) 
        data = response.json()  #convert to json format

        if("results" in data):
                user_data = data["results"][0]
                user_name = user_data["name"]["first"] + " " + user_data["name"]["last"]
                user_gender = user_data["gender"]
                user_lat = float(user_data["location"]["coordinates"]["latitude"])
                user_long = float(user_data["location"]["coordinates"]["longitude"])
                return User(user_data["login"]["uuid"], user_name, user_gender, user_lat, user_long)

        else:
               raise Exception("Error 1: Failed to Fetch User Data")


def fetch_multple(count):
        url = f"https://randomuser.me/api/?results={count}"
        response = requests.get(url)
        data = response.json()

        if( int(count) > 0 and "results" in data):
                user_list = []
                for x in data["results"]:
                        user_list.append(User(x["login"]["uuid"], x["name"]["first"] + " " + x["name"]["last"], x["gender"], float(x["location"]["coordinates"]["latitude"]), float(x["location"]["coordinates"]["longitude"])))
                return user_list
        else:
                raise Exception("Error 2: Failed to Fetch Users Data")


def merge(dist, low, mid, high):
        n1 = mid - low + 1
        n2 = high - mid
        a = [0] * n1
        b = [0] * n2

        for i in range(n1):
                a[i] = dist[low + i]
        for j in range(n2):
                b[j] = dist[mid + 1 + j]

        i = j = 0
        k = low

        while i < n1 and j < n2:
                if a[i][2] <= b[j][2]:
                        dist[k] = a[i]
                        i += 1
                else:
                        dist[k] = b[j]
                        j += 1
                k += 1

        while i < n1:
                dist[k] = a[i]
                i += 1
                k += 1

        while j < n2:
                dist[k] = b[j]
                j += 1
                k += 1

def mergeSort(dist, low, high):
        if low < high:
                mid = (low + high) // 2
                mergeSort(dist, low, mid)
                mergeSort(dist, mid + 1, high)
                merge(dist, low, mid, high)



class User:
        def __init__(self, uuid, name, gender, latitude, longitude):
                self.uuid = uuid
                self.name = name
                self.gender = gender
                self.latitude = latitude
                self.longitude = longitude

        def distance(self, user2):
                return m.sqrt((self.latitude - user2.latitude)**2 + (self.longitude  - user2.longitude)**2)


       
def main():
        try:
                random_user = fetch_user()
                print(f"Picked Random User- \nName: {random_user.name}   Gender: {random_user.gender} \nUUID: {random_user.uuid} \nLocation:- \n 1. Latitude: {random_user.latitude}\n 2. Longitude: {random_user.longitude}")
                print()
                print("How many users data do you wish to request?")
                x = int(input())
                users = fetch_multple(x)

                dist = []
                for i in users:
                        if(random_user.gender != i.gender):
                                dist.append((i.uuid, i.gender, random_user.distance(i)))
                if dist:
                        mergeSort(dist, 0, len(dist)-1)
                for j in range(0,min(100, len(dist))):
                        print(dist[j])

        except Exception as e:
                print(str(e))

if __name__ == "__main__":
        main()