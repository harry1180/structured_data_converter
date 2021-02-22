import pandas as pd

header = ["Filename", "term", "coursename", "description", "attempted","earned credits", "points", "grade"]
file1_data = []
def data_dump():
    df1=pd.DataFrame(file1_data)
    df1.to_excel('output_example2.xlsx',index=False)

def mapped_data(in_row={}):
    print('function called') 
    file1_data.append(in_row)
def process_example1():
    with open("Example_1.txt") as file1:
        counter, data_ind=1,1
        while counter  and data_ind<=2:
            temp,temp_dict = file1.readline(), {}
            if len(temp)==1:
                data_ind+=1
            if counter==1:
                term_data=temp.strip()
                if term_data=='Fall Semester 2011 (Freshman)':
                    term_data="fall 2011"
            if counter ==2:
                #extract header
                temp_header=[each.strip() for each in temp.split(" ")]
                #print(temp_header,'temp_header')
            if counter >3 and data_ind<=2:
                data=[each.strip() for each in temp.split(" ")]
                #print(data,'this is the raw data', data_ind)
                if isinstance(float(data[-1]),float) and isinstance(float(data[-3]),float):
                    DeptNo = " ".join(temp.split(" ")[:2]).strip()
                    Course_Title = " ".join(temp.split(" ")[2:-3]).strip()
                    Units,GR,GP=[i.strip() for i in temp.split(" ")[-3:]]
                    #print(Units,'units')
                    
                temp_dict.update({"Filename":file1.name,"term":term_data,"coursename":DeptNo, "description":Course_Title,"attempted":"n/a","earned credits":Units, "points":GP,"grade":GR})
                #print(temp_dict,'this is temp dict with data')
                mapped_data(temp_dict)
    
            counter+=1
def process_example2():
    with open("Example_2.txt") as file1:
        counter, data_ind,term =1,1, ''
        while counter and data_ind<10:
            temp,temp_dict = file1.readline().strip(), {}
            try:
                if len(temp)==0:
                    data_ind+=1
                if len(temp)>20:
                    data_ind=1
                if "-----------" in temp:
                    term = " ".join(temp.split(" ")[:2])
                if term and len(temp)>2 and isinstance(float(temp.split(" ")[-1]),float) and "-" in [i for i in temp.split(" ")][0] and temp.split(" ")[-4] in ("A","B","W"): 
                    temp_list=temp.split(" ")
                    coursename = temp_list[0]
                    attempted = str(temp_list[-3])
                    earned_credits = str(temp_list[-2])
                    points = str(temp_list[-1])
                    grade = temp_list[-4]
                    description = " ".join(temp_list[1:-4])
                    temp_dict.update({"Filename":file1.name,"term":term,"coursename":coursename, "description":description,"attempted":attempted,"earned credits":earned_credits, "points":points,"grade":grade})
                    mapped_data(temp_dict)
    
                counter+=1
            except Exception as e:
                continue
    print(file1_data)
def process_example3():
    with open("Example_3.txt") as file1:
        counter, data_ind,term =1,1, ''
        while counter and data_ind<10:
            temp,temp_dict = file1.readline().strip(), {}
            print(len(temp))
            try:
                if len(temp)==0:
                    data_ind+=1
                elif len(temp)>20:
                    data_ind=1
                if temp.split(" ")[0] in ("Spring","Fall") :
                    term = " ".join(temp.split(" ")[:2])
                if "2011-15 Am." in temp:
                    term = temp.split(" ")[0]
                print(term,'this is term')
                if temp.split(" ")[-1] in ("T","I","E"):
                    if term and len(temp)>2 and isinstance(float(temp.split(" ")[-2]),float) and temp.split(" ")[-1] in ("T","I","E") : 
                        print(temp,'qualified')
                        temp_list=temp.split(" ")
                        coursename = " ".join(temp_list[:2])
                        attempted = "n/a"
                        earned_credits = str(temp_list[-2])
                        points = "n/a"
                        grade = temp_list[-1]
                        description = " ".join(temp_list[2:-2])
                        temp_dict.update({"Filename":file1.name,"term":term,"coursename":coursename, "description":description,"attempted":attempted,"earned credits":earned_credits, "points":points,"grade":grade})
                        mapped_data(temp_dict)
 

                if term and len(temp)>2 and isinstance(float(temp.split(" ")[-1]),float) and temp.split(" ")[-2] in ("A","B","C","W","F","U","Y") : 
                    print(temp,'qualified')
                    temp_list=temp.split(" ")
                    coursename = " ".join(temp_list[:2])
                    attempted = "n/a"
                    earned_credits = str(temp_list[-3])
                    points = str(temp_list[-1])
                    grade = temp_list[-2]
                    description = " ".join(temp_list[2:-3])
                    temp_dict.update({"Filename":file1.name,"term":term,"coursename":coursename, "description":description,"attempted":attempted,"earned credits":earned_credits, "points":points,"grade":grade})
                    mapped_data(temp_dict)
   
                counter+=1
            except Exception as e:
                #print(e)
                continue

process_example1()
process_example2()
process_example3()
print(file1_data)
data_dump()
