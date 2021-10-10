# Neutrino Thermal Process Analysis Project
# Create neutrino Hertzprung-Russell diagram and Kippenhahn diagram from experimental data 
## General info
![neutrino](https://user-images.githubusercontent.com/71859510/134769495-f85791df-4344-441d-a75a-c956efe02579.PNG)
![neutrino2](https://user-images.githubusercontent.com/71859510/134769602-cb30261e-369f-4413-8c82-39a81002e673.PNG)
* Below are stellar HR and Kippenhahn diagram
![neutrino4](https://user-images.githubusercontent.com/71859510/134769793-1508a798-450a-41d9-8fc5-d079d31c01fb.PNG)
![neutrino5](https://user-images.githubusercontent.com/71859510/134769795-e27e19fc-714e-45fe-8346-3886f0165ec5.PNG)

## Analysis methodology
* Raw data needs some processing to be useful in the public code
* Clean data are added into public code to calculate all thermal processes by neutrino from 5 different masses of stars
* All thermal processes are then plotted using Python
![neutrino3](https://user-images.githubusercontent.com/71859510/134769664-1a7fb176-b744-4322-a035-b70da9340de5.PNG)

## Project status
* Project completed

## Result
* Part 1: Stellar structure
* In order to calculate the neutrino energy loss, we require the stellar structure of very massive stellar models at the end of the evolution. Neutrino energy loss is dominant when the star reach Carbon burning phase. In this work, the star ended at the middle of Carbon burning stage before it exploded into supernova
* Graph below shows the temperature and density vs radius for 120 M⊙ structure, similar pattern for 150 M⊙, 200 M⊙, 300 M⊙ and 500M⊙ structure as well 
![image](https://user-images.githubusercontent.com/71859510/136695275-a96290b6-cf24-4add-928b-fe9b4c5a3be5.png)
* From the graph above, the temperature and density decrease exponentially from the center to the surface of the star. This means that at the core of the stars, the temperature and density are extremely dense and hot due to gravitational contraction and nuclear fusion. 
* From our results, we observed that neutrino energy loss from pair process, Qpair dominates the neutrino energy loss process for all stellar models. We observed the neutrino energy loss is highest for 500M⊙ model because this star is the densest with highest core temperature as compared to other models.  We summarized our result in the table below.
![image](https://user-images.githubusercontent.com/71859510/136695309-05f254d9-8004-44cc-bd69-93c74174de03.png)
* Figure below show the neutrino energy loss for pair and photo production neutrino energy loss with temperature 
![image](https://user-images.githubusercontent.com/71859510/136695327-d424cfd0-a5a1-4cb9-9d40-f1e8c4033d53.png)

* Figure below show the neutrino energy loss for pair and photo production neutrino energy loss with density
![image](https://user-images.githubusercontent.com/71859510/136695343-fa974b39-8d83-4c0a-8486-fbaa27044dd8.png)

* Part 2: Stellar Evolution
* We observed that the initial mass of a star plays a crucial role in determining its evolutionary track. Very massive stars have very high luminosities, and this reflects in the following HR diagram below. We demonstrated the Kippenhahn diagram below which shows the evolution of mass with time. As the star becomes more massive, it undergoes fusion at a much higher rate and use up all its elements at much shorter time, hence the shortest lived star from our calculation is the 500 M⊙ model that reached evolved stage at 2.3 Myr as compared to 120 M⊙ which has longer lifetime which is around 3.0 Myr
* This is Stellar HR diagram that shows evolutionary tracks of 120 M⊙, 150M⊙, 200 M⊙, 300M⊙ and 500 M⊙ models
![image](https://user-images.githubusercontent.com/71859510/136695352-a8a952b6-4b7a-4352-95c1-92db4862c1d8.png)

* This is Kippenhahn diagram that shows mass loss of 120 M⊙, 150M⊙, 200M⊙, 300M⊙ and 500 M⊙ models
![image](https://user-images.githubusercontent.com/71859510/136695363-82f62873-1ef3-432c-92ac-a9752e51e1ff.png)
 
* Neutrino HR diagrams below show us that, at the early stages of evolution, photoneutrino process dominates contribution to neutrino energy loss due to the low temperature and density at early evolution. Approaching the end of the evolution, pair production dominates contribution to neutrino energy loss since temperature and density now increase by a factor of 109K, which is the optimum temperature to trigger the process into producing significant neutrino flux. Following it are Kippenhahn diagrams that show similar observations regarding neutrino energy-loss rates resulting from pair production and photoneutrino processes.
* This is Neutrino HR diagram for 120 M⊙ model in term of neutrino energy-loss rate resulting from pair production and photoneutrino processes.
![image](https://user-images.githubusercontent.com/71859510/136695394-c7b792eb-e57e-42ff-bf3b-a1fd73492a61.png)

* This is Neutrino HR diagram for 150 M⊙ model in term of neutrino energy-loss rate resulting from pair production and photoneutrino processes.
![image](https://user-images.githubusercontent.com/71859510/136695410-a9631db5-c5f0-404f-80d0-0b846e57d32f.png)
 
* This is Neutrino HR diagram for 200 M⊙ model in term of neutrino energy-loss rate resulting from pair production and photoneutrino processes.
![image](https://user-images.githubusercontent.com/71859510/136695425-ebab7dcf-86c0-40ca-adb9-8fbefebca433.png)

* This is Neutrino HR diagram for 300 M⊙ model in term of neutrino energy-loss rate resulting from pair production and photoneutrino processes.
![image](https://user-images.githubusercontent.com/71859510/136695433-fe1375e0-158d-448e-96b4-1989b63cfaa3.png)

* Table below summarized neutrino HR result, which shows neutrino energy loss resulting from pair production and photoneutrino 
processes in massive stars at evolved stage
![image](https://user-images.githubusercontent.com/71859510/136695471-a8af473c-8829-4a1f-b040-4b129f94b8c7.png)

Table below summarized our neutrino Kippenhahn result, which shows neutrino energy loss resulting from pair production and photoneutrino processes in massive stars at final age

![image](https://user-images.githubusercontent.com/71859510/136695482-106e1e62-31e5-4a38-bc62-b8493bf83ff9.png)
* Neutrino Kippenhahn diagram for 120 M⊙ model in term of neutrino energy-loss rate resulting from pair production and photoneutrino processes
![image](https://user-images.githubusercontent.com/71859510/136695502-25cfb038-cd48-4eb9-8a2e-471fe449c74b.png)

## Conclusion
* Precise calculation on neutrino energy loss rate is important in the study of massive stellar evolution because we now understand that neutrino-cooling mechanism plays crucial role in controlling the temperature and density of a massive star’s core, consequently affecting the life and death of the stars. 
* Study of cooling mechanism inside massive stars provide unique insights into supernovae and may help explain more exotic objects, such as pulsars, energetic galactic cores, and black holes. 

## Public code reference 
* Itoh et.al
