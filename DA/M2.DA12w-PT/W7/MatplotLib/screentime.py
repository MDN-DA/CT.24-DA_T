import matplotlib.pyplot as plt

day=["Monday","Tuesday","Wednesday","Thursday","Friday"]
yt=[2,1,3,6,3]
twit=[1,1,0,0,2]
chat=[3,1,0,2,1]
raid=[0,4,2,3,3]
taktak=[3,0,1,0,2]
plt.plot(day,yt,label="Youtube")
plt.plot(day,twit,label="Twitter",linestyle="dashed")
plt.plot(day,chat,label="WhatsApp",linestyle="dotted")
plt.plot(day,raid,label="Raid",linestyle="dashdot")
plt.plot(day,taktak,label="TikTok")
plt.title("Screen-time")
plt.xlabel("Day")
plt.ylabel("Hour")
plt.legend()
plt.ylim(bottom=0, top=12)
plt.show()