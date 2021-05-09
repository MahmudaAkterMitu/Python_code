res_list = []
globalTime = 0 

while(1):
    print("\n\tPress E/e to exit or Enter the value of n\n")

    n = input("n: ")   
    
    if n == "E" or n == "e":
      print("\n*-* Thank you *-*")
      break
      
    else:
      n = int(n)
      input_list = []
      #input_list = [['1', 'A', '40', 0], ['2', 'B', '50', 0], ['3', 'C', '10', 5]]
      
      # user input
      for i in range(0,n):
        temp_list = []   
        pId      = input("Enter ProcessId: ")
        pName    = input("Enter ProcessName: ")
        duration = int(input("Enter Duration: "))
        AT       = int(input("Enter ArrivalTime: "))
        print("\n")

        temp_list.append(pId)
        temp_list.append(pName)
        temp_list.append(duration)
        temp_list.append(AT)
        input_list.append(temp_list)

      # sorting the processes according to their arrival time.
      input_list.sort(key=lambda x: x[3])
      #print(input_list)     

      # If multiple process arrive at the same time, the shortest process among them gets the schedule first. Handled below:
      # Start
      temp = []
      input_list1 = []
      p = input_list[0][-1]
      for i in input_list:
        if i[-1] == p:
          temp.append(i)
          #print(temp)
        else:
          p = i[-1]
          temp.sort(key=lambda x: x[2])
          temp.append(i)
          for i in temp:
            input_list1.append(i)
          temp = []
      #print(input_list1)
      # End

      # FCFS
      for i in input_list1:   
        res = []
        p = i[-1]
        if int(p) <= globalTime:
          timeline = str(globalTime) + "-" + str(globalTime+int(i[-2]))
          globalTime = globalTime + int(i[-2])
          turnAround = globalTime - int(i[-1])
          res.append(i[-3])
          res.append(timeline)
          res.append(turnAround)
          res_list.append(res)
        else:
          globalTime  = int(i[-1]) 
          timeline = str(globalTime) + "-" + str(globalTime+int(i[-2]))
          globalTime  = globalTime + int(i[-2])
          turnAround = globalTime - int(i[-1])          
          res.append(i[-3])
          res.append(timeline)
          res.append(turnAround)
          res_list.append(res)
      #print(res_list)

      # printing the whole result
      print("\t Sequence Number \t Process Name\tTimeline\t Turn Around")    
      i = 0
      att = 0
      for j in res_list:
        print("\t\t"+str(i+1)+"\t\t\t"+str(j[0])+"  \t "+str(j[1])+"\t\t\t"+str(j[2]))
        att = att + j[2]
        i = i+1
      att = att/len(res_list)
      print("\nAverage TurnAround Time (ATT): "+ str(att))