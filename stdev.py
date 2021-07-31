import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)

firststdevstart, firststdevend = mean-stdev, mean+stdev
twostdevstart, twostdevend = mean-2*stdev, mean+2*stdev
threestdevstart, threestdevend = mean-3*stdev, mean+3*stdev

listofdatafirststdev = [res for res in data if res > firststdevstart and res < firststdevend]
listofdatatwostdev = [res for res in data if res > twostdevstart and res < twostdevend]
listofdatathreestdev = [res for res in data if res > threestdevstart and res < threestdevend]

print("Mean of the reading score is: "+str(mean))
print("Median of the reading score is: "+str(median))
print("Mode of the reading score is: "+str(mode))
print("Standard deviation of the reading score is: "+str(stdev))
print("{}% of data lies within one standard deviation".format(len(listofdatafirststdev)*100.0/len(data)))
print("{}% of data lies within two standard deviation".format(len(listofdatatwostdev)*100.0/len(data)))
print("{}% of data lies within three standard deviation".format(len(listofdatathreestdev)*100.0/len(data)))