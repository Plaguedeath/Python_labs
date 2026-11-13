import sys


def main():

    file_path = sys.argv[1]
    cities_temp = {}

    with open(file_path, 'rb') as file:  
        for line in file:  
           
            city, temp = line.split(b';')
            temp = float(temp)
            
            stats = cities_temp.get(city)
            if stats is None:
                cities_temp[city] = [temp, temp, temp, 1]
            else:
                if temp < stats[0]:
                    stats[0] = temp
                stats[1] += temp
                if temp > stats[2]:
                    stats[2] = temp
                stats[3] += 1
        
        
        cities_temp=dict(sorted(cities_temp.items()))
        for key in cities_temp:
                value=round(cities_temp[key][1]/cities_temp[key][3],1)
                print (f"{key.decode('utf-8')};{cities_temp[key][0]};{value:.1f};{cities_temp[key][2]}")

if __name__ == "__main__":
    main()
